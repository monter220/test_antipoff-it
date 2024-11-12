import time
import random

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse

from core.db import get_async_session
from crud import history_crud, cadastr_crud
from schemas import HistoryDB, CadastrGet, CadastrCreate


router = APIRouter()


@router.get(
    '/history',
    tags=['writes into the history table'],
    summary='Получение истории операций',
    response_model=list[HistoryDB],
    response_model_exclude_none=True,
)
async def get_history(
        session: AsyncSession = Depends(get_async_session),
):
    return await history_crud.get_multi(session=session)


@router.get(
    '/ping',
    tags=['writes into the history table'],
    summary='Проверка доступности сервиса',
)
async def get_ping(
        session: AsyncSession = Depends(get_async_session),
):
    answer = 'Сервис доступен'
    await history_crud.create(
        session=session,
        endpoint='/ping',
        type='get',
        obj_in=answer
    )
    return answer


@router.post(
    '/query',
    tags=['writes into the history table'],
    summary='Отправка запроса',
    response_model=CadastrGet,
)
async def post_query(
        query: CadastrCreate,
        session: AsyncSession = Depends(get_async_session),
):
    result = await cadastr_crud.create(
        obj_in=query,
        session=session,
        endpoint='/query',
        type='/post'
    )
    time.sleep(random.randint(0,60))
    return RedirectResponse(
        f'/result/{result}', status_code=status.HTTP_303_SEE_OTHER)


@router.get(
    '/result/{result}',
    tags=["don't writes into the history table"],
    summary='Получение ответа на запрос',
    response_model_exclude_none=True,
)
async def get_query(
        result,
        session: AsyncSession = Depends(get_async_session),
):
    return f'Ответ на ваш запрос {result}'
