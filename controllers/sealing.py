from sqlmodel import select

from database.connection import get_session
from database.models import Sealing


def register():
    with get_session() as session:

        sealing = Sealing()

        session.add(sealing)
        session.commit()
        session.refresh(sealing)

        return sealing


def all():
    with get_session() as session:
        return session.exec(
            select(Sealing)
        ).all()


def count():
    with get_session() as session:
        return len(
            session.exec(
                select(Sealing)
            ).all()
        )