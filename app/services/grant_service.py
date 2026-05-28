from datetime import datetime, timedelta
from uuid import UUID
import app.models
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.grant import Grant
from app.schemas.grant import GrantCreate


async def create_grant(
    session: AsyncSession,
    payload: GrantCreate
):

    # Expiry validation
    if payload.expires_at <= datetime.now() + timedelta(minutes=1):
        raise HTTPException(
            status_code=400,
            detail="Expiry must be at least 1 minute in future"
        )

    # Check duplicate active grant
    query = select(Grant).where(
        Grant.document_id == payload.document_id,
        Grant.grantee_id == payload.grantee_id,
        Grant.revoked_at.is_(None),
        Grant.expires_at > datetime.now()
    )

    result = await session.execute(query)

    existing_grant = result.scalar_one_or_none()

    if existing_grant:
        raise HTTPException(
            status_code=409,
            detail="Active grant already exists"
        )

    grant = Grant(
        document_id=payload.document_id,

        # Alice as grantor
        grantor_id=UUID("11111111-1111-1111-1111-111111111111"),

        grantee_id=payload.grantee_id,
        permission=payload.permission,
        expires_at=payload.expires_at
    )

    session.add(grant)

    await session.commit()

    await session.refresh(grant)

    return grant



async def get_all_grants(
    session: AsyncSession
):

    query = select(Grant)

    result = await session.execute(query)

    return result.scalars().all()

async def get_grant_by_id(
    session: AsyncSession,
    grant_id: UUID
):

    query = select(Grant).where(
        Grant.id == grant_id
    )

    result = await session.execute(query)

    grant = result.scalar_one_or_none()

    if not grant:
        raise HTTPException(
            status_code=404,
            detail="Grant not found"
        )

    return grant

async def revoke_grant(
    session: AsyncSession,
    grant_id: UUID
):

    grant = await get_grant_by_id(
        session,
        grant_id
    )

    if grant.revoked_at:
        raise HTTPException(
            status_code=400,
            detail="Grant already revoked"
        )

    grant.revoked_at = datetime.now()

    await session.commit()

    await session.refresh(grant)

    return grant

async def check_grant_active(
    session: AsyncSession,
    grant_id: UUID
):

    grant = await get_grant_by_id(
        session,
        grant_id
    )

    active = (
        grant.revoked_at is None
        and grant.expires_at > datetime.now()
    )

    return {
        "grant_id": grant.id,
        "active": active
    }
