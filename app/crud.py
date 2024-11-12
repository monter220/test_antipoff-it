from typing import TypeVar
from sqlalchemy import select, false
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.models import History, Cadaster


ModelType = TypeVar('ModelType', bound=Base)


async def historydata(
    session: AsyncSession,
    endpoint: str,
    type: str,
    obj: str,
):
    event = dict.fromkeys(['endpoint', 'type', 'data'])
    event['endpoint'] = endpoint
    event['type'] = type
    event['data'] = obj
    session.add(History(**event))


class CrudBase:

    def __init__(self, model):
        self.model = model


class CadastrCRUD(CrudBase):

    async def create(
        self,
        obj_in,
        session: AsyncSession,
        endpoint: str,
        type: str,
    ):
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        await historydata(session, endpoint, type, str(obj_in_data))
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj.result


class HistoryCRUD(CrudBase):

    async def get_multi(
            self,
            session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model))
        await historydata(session, '/history', 'get', '')
        await session.commit()
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in: str,
        session: AsyncSession,
        endpoint: str,
        type: str,
    ):
        await historydata(session, endpoint, type, obj_in)
        await session.commit()


cadastr_crud = CadastrCRUD(Cadaster)
history_crud = HistoryCRUD(History)
