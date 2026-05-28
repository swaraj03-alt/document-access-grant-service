from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime

from app.db.base import Base


class Grant(Base):
    __tablename__ = "grants"
    __table_args__ = {"schema": "grants_svc"}

    id = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    document_id = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grants_svc.documents.id"),
        nullable=False
    )

    grantor_id = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grants_svc.users.id"),
        nullable=False
    )

    grantee_id = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("grants_svc.users.id"),
        nullable=False
    )

    permission = mapped_column(
        String,
        nullable=False
    )

    expires_at = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    revoked_at = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )