import os

from fastapi import APIRouter, Header, HTTPException, status
from sqlmodel import SQLModel

from database.connection import get_session
import controllers.sealing as sealing


router = APIRouter()
routes = router
ADMIN_WIPE_KEY = os.getenv("ADMIN_WIPE_KEY", "")


@router.get("/")
def home():
    return {"status": "online"}


router.get("/sealing")(sealing.all)
router.post("/sealing")(sealing.register)


@router.delete("/admin/database")
def wipe_database(x_admin_key: str | None = Header(default=None, alias="X-Admin-Key")):
    if x_admin_key != ADMIN_WIPE_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid admin key",
        )

    with get_session() as session:
        for table in reversed(SQLModel.metadata.sorted_tables):
            session.exec(table.delete())
        session.commit()

    return {"status": "database wiped"}

