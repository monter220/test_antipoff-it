from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse

from core.db import get_async_session
from crud import history_crud, cadastr_crud
from schemas import HistoryDB, CadastrGet, CadastrCreate


router = APIRouter()


@router.get(
    '/history',
    response_model=list[HistoryDB],
    response_model_exclude_none=True,
)
async def get_history(
        session: AsyncSession = Depends(get_async_session),
):
    return await history_crud.get_multi(session=session)


@router.get(
    '/ping',
)
async def get_ping(
        session: AsyncSession = Depends(get_async_session),
):
    # bool(random.getrandbits(1))
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
    return RedirectResponse(
        f'/result/{result}', status_code=status.HTTP_303_SEE_OTHER)


@router.get(
    '/result/{result}',
    response_model_exclude_none=True,
)
async def get_query(
        result,
        session: AsyncSession = Depends(get_async_session),
):
    return f'Ответ на ваш запрос {result}'
