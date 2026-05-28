from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class GrantCreate(BaseModel):
    document_id: UUID
    grantee_id: UUID
    permission: str
    expires_at: datetime


class GrantResponse(BaseModel):
    id: UUID
    document_id: UUID
    grantor_id: UUID
    grantee_id: UUID
    permission: str
    expires_at: datetime
    revoked_at: datetime | None