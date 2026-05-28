from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "grants_svc"}

    id = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    name = mapped_column(
        String,
        nullable=False
    )