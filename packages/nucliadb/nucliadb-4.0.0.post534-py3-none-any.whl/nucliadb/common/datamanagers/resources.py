# Copyright (C) 2021 Bosutech XXI S.L.
#
# nucliadb is offered under the AGPL v3.0 and as commercial software.
# For commercial licensing, contact us at info@nuclia.com.
#
# AGPL:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from typing import AsyncGenerator, Optional

import backoff

from nucliadb.common.datamanagers.utils import get_kv_pb
from nucliadb.common.maindb.driver import Transaction
from nucliadb.common.maindb.exceptions import ConflictError, NotFoundError

# These should be refactored
from nucliadb.ingest.orm.resource import KB_RESOURCE_SLUG, KB_RESOURCE_SLUG_BASE
from nucliadb.ingest.orm.resource import Resource as ResourceORM
from nucliadb.ingest.orm.utils import get_basic, set_basic
from nucliadb_protos import noderesources_pb2, resources_pb2, writer_pb2
from nucliadb_utils.utilities import get_storage

from .utils import with_transaction

KB_MATERIALIZED_RESOURCES_COUNT = "/kbs/{kbid}/materialized/resources/count"
KB_RESOURCE_SHARD = "/kbs/{kbid}/r/{uuid}/shard"
KB_RESOURCE_ALL_FIELDS = "/kbs/{kbid}/r/{uuid}/allfields"


@backoff.on_exception(
    backoff.expo, (Exception,), jitter=backoff.random_jitter, max_tries=3
)
async def _iter_resource_slugs(*, kbid: str) -> AsyncGenerator[str, None]:
    async with with_transaction() as txn:
        async for key in txn.keys(
            match=KB_RESOURCE_SLUG_BASE.format(kbid=kbid), count=-1
        ):
            yield key.split("/")[-1]


@backoff.on_exception(
    backoff.expo, (Exception,), jitter=backoff.random_jitter, max_tries=3
)
async def _get_resource_ids_from_slugs(kbid: str, slugs: list[str]) -> list[str]:
    async with with_transaction() as txn:
        rids = await txn.batch_get(
            [KB_RESOURCE_SLUG.format(kbid=kbid, slug=slug) for slug in slugs]
        )
    return [rid.decode() for rid in rids if rid is not None]


async def iterate_resource_ids(*, kbid: str) -> AsyncGenerator[str, None]:
    """
    Currently, the implementation of this is optimizing for reducing
    how long a transaction will be open since the caller controls
    how long each item that is yielded will be processed.

    For this reason, it is not using the `txn` argument passed in.
    """
    batch = []
    async for slug in _iter_resource_slugs(kbid=kbid):
        batch.append(slug)
        if len(batch) >= 200:
            for rid in await _get_resource_ids_from_slugs(kbid=kbid, slugs=batch):
                yield rid
            batch = []
    if len(batch) > 0:
        for rid in await _get_resource_ids_from_slugs(kbid=kbid, slugs=batch):
            yield rid


@backoff.on_exception(
    backoff.expo, (Exception,), jitter=backoff.random_jitter, max_tries=3
)
async def get_resource_shard_id(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[str]:
    shard = await txn.get(KB_RESOURCE_SHARD.format(kbid=kbid, uuid=rid))
    if shard is not None:
        return shard.decode()
    else:
        return None


@backoff.on_exception(
    backoff.expo, (Exception,), jitter=backoff.random_jitter, max_tries=3
)
async def get_resource(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[ResourceORM]:
    """
    Not ideal to return Resource type here but refactoring would
    require a lot of changes.

    At least this isolated that dependency here.
    """
    # prevent circulat imports -- this is not ideal that we have the ORM mix here.
    from nucliadb.ingest.orm.knowledgebox import KnowledgeBox as KnowledgeBoxORM

    kb_orm = KnowledgeBoxORM(txn, await get_storage(), kbid)
    return await kb_orm.get(rid)


async def resource_exists(txn: Transaction, *, kbid: str, rid: str) -> bool:
    basic = await get_basic(txn, kbid, rid)
    return basic is not None


@backoff.on_exception(
    backoff.expo, (Exception,), jitter=backoff.random_jitter, max_tries=3
)
async def get_resource_index_message(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[noderesources_pb2.Resource]:
    # prevent circulat imports -- this is not ideal that we have the ORM mix here.
    from nucliadb.ingest.orm.knowledgebox import KnowledgeBox as KnowledgeBoxORM

    kb_orm = KnowledgeBoxORM(txn, await get_storage(), kbid)
    res = await kb_orm.get(rid)
    if res is None:
        return None
    return (await res.generate_index_message()).brain


async def calculate_number_of_resources(txn: Transaction, *, kbid: str) -> int:
    """
    Calculate the number of resources in a knowledgebox.

    This is usually not very fast at all.

    Long term, we could think about implementing a counter; however,
    right now, a counter would be difficult, require a lot of
    refactoring and not worth much value for the APIs we need
    this feature for.

    Finally, we could also query this data from the node; however,
    it is not the source of truth for the value so it is not ideal
    to move it to the node.
    """
    return await txn.count(KB_RESOURCE_SLUG_BASE.format(kbid=kbid))


async def get_number_of_resources(txn: Transaction, *, kbid: str) -> int:
    """
    Return cached number of resources in a knowledgebox.
    """
    raw_value = await txn.get(KB_MATERIALIZED_RESOURCES_COUNT.format(kbid=kbid))
    if raw_value is None:
        return -1
    return int(raw_value)


async def set_number_of_resources(txn: Transaction, kbid: str, value: int) -> None:
    await txn.set(
        KB_MATERIALIZED_RESOURCES_COUNT.format(kbid=kbid), str(value).encode()
    )


async def get_broker_message(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[writer_pb2.BrokerMessage]:
    resource = await get_resource(txn, kbid=kbid, rid=rid)
    if resource is None:
        return None

    resource.disable_vectors = False
    resource.txn = txn
    bm = await resource.generate_broker_message()
    return bm


async def get_resource_basic(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[resources_pb2.Basic]:
    raw_basic = await get_basic(txn, kbid, rid)
    if not raw_basic:
        return None
    basic = resources_pb2.Basic()
    basic.ParseFromString(raw_basic)
    return basic


async def get_resource_uuid_from_slug(
    txn: Transaction, *, kbid: str, slug: str
) -> Optional[str]:
    encoded_uuid = await txn.get(KB_RESOURCE_SLUG.format(kbid=kbid, slug=slug))
    if not encoded_uuid:
        return None
    return encoded_uuid.decode()


async def modify_slug(txn: Transaction, *, kbid: str, rid: str, new_slug: str) -> str:
    basic = await get_resource_basic(txn, kbid=kbid, rid=rid)
    if basic is None:
        raise NotFoundError()
    old_slug = basic.slug

    uuid_for_new_slug = await get_resource_uuid_from_slug(txn, kbid=kbid, slug=new_slug)
    if uuid_for_new_slug is not None:
        if uuid_for_new_slug == rid:
            # Nothing to change
            return old_slug
        else:
            raise ConflictError(f"Slug {new_slug} already exists")
    key = KB_RESOURCE_SLUG.format(kbid=kbid, slug=old_slug)
    await txn.delete(key)
    key = KB_RESOURCE_SLUG.format(kbid=kbid, slug=new_slug)
    await txn.set(key, rid.encode())
    basic.slug = new_slug
    await set_basic(txn, kbid, rid, basic)
    return old_slug


async def set_resource_shard_id(txn: Transaction, *, kbid: str, rid: str, shard: str):
    await txn.set(KB_RESOURCE_SHARD.format(kbid=kbid, uuid=rid), shard.encode())


async def get_all_field_ids(
    txn: Transaction, *, kbid: str, rid: str
) -> Optional[resources_pb2.AllFieldIDs]:
    key = KB_RESOURCE_ALL_FIELDS.format(kbid=kbid, uuid=rid)
    return await get_kv_pb(txn, key, resources_pb2.AllFieldIDs)


async def set_all_field_ids(
    txn: Transaction, *, kbid: str, rid: str, allfields: resources_pb2.AllFieldIDs
):
    key = KB_RESOURCE_ALL_FIELDS.format(kbid=kbid, uuid=rid)
    await txn.set(key, allfields.SerializeToString())


async def has_field(
    txn: Transaction, *, kbid: str, rid: str, field_id: resources_pb2.FieldID
) -> bool:
    fields = await get_all_field_ids(txn, kbid=kbid, rid=rid)
    if fields is None:
        return False
    for resource_field_id in fields.fields:
        if field_id == resource_field_id:
            return True
    return False
