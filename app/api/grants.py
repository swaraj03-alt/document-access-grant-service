from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.schemas.grant import GrantCreate, GrantResponse
from app.services.grant_service import create_grant
from uuid import UUID

from app.services.grant_service import (
    create_grant,
    get_all_grants,
    get_grant_by_id,
    revoke_grant,
    check_grant_active
)


router = APIRouter(
    prefix="/grants",
    tags=["Grants"]
)


@router.post(
    "",
    response_model=GrantResponse
)

@router.get(
    "",
    response_model=list[GrantResponse]
)
async def list_grants(
    session: AsyncSession = Depends(get_db)
):
    return await get_all_grants(session)

@router.get(
    "/{grant_id}",
    response_model=GrantResponse
)
async def get_grant(
    grant_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    return await get_grant_by_id(
        session,
        grant_id
    )

@router.delete(
    "/{grant_id}",
    response_model=GrantResponse
)
async def revoke_existing_grant(
    grant_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    return await revoke_grant(
        session,
        grant_id
    )

@router.get(
    "/{grant_id}/check"
)
async def check_grant(
    grant_id: UUID,
    session: AsyncSession = Depends(get_db)
):
    return await check_grant_active(
        session,
        grant_id
    )


async def create_new_grant(
    payload: GrantCreate,
    session: AsyncSession = Depends(get_db)
):
    return await create_grant(session, payload)