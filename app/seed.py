import asyncio
from uuid import UUID

from sqlalchemy import insert

from app.db.session import engine
from app.models.user import User
from app.models.document import Document


async def seed():
    async with engine.begin() as conn:

        await conn.execute(
            insert(User),
            [
                {
                    "id": UUID("11111111-1111-1111-1111-111111111111"),
                    "name": "Alice"
                },
                {
                    "id": UUID("22222222-2222-2222-2222-222222222222"),
                    "name": "Bob"
                },
                {
                    "id": UUID("33333333-3333-3333-3333-333333333333"),
                    "name": "Carol"
                }
            ]
        )

        await conn.execute(
            insert(Document),
            [
                {
                    "id": UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"),
                    "title": "Q1 Report"
                },
                {
                    "id": UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"),
                    "title": "Product Roadmap"
                },
                {
                    "id": UUID("cccccccc-cccc-cccc-cccc-cccccccccccc"),
                    "title": "Budget 2026"
                }
            ]
        )


asyncio.run(seed())