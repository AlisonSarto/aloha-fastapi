from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
class Sealing(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
