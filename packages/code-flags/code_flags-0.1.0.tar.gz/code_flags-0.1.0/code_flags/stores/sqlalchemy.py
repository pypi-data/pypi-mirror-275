from typing import TypeAlias

from sqlalchemy import String, create_engine, delete, select
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    mapped_column,
    sessionmaker,
)

from code_flags.utils import Singleton

from .store import Store

Flag: TypeAlias = str
Value: TypeAlias = bool

Base = declarative_base()


class FlagEntry(Base):
    __tablename__ = 'flags'

    flag: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[bool]


class SQLAlchemyStore(Store, Singleton):
    def __init__(
        self,
        db_uri: str = 'sqlite:///flags.db',
    ):
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        self.session_factory = sessionmaker(bind=engine)

    def save(self, flag: Flag, value: Value) -> None:
        """Save a flag in the SQLAlchemy store backend with the value received"""
        with self.session_factory() as session:
            with session.begin():
                entry = FlagEntry(flag=flag, value=value)
                session.add(entry)

    def save_bulk(self, flags: dict[Flag, Value]) -> None:
        """Save all flags passed from the parameter."""
        with self.session_factory() as session:
            with session.begin():
                entries = [
                    FlagEntry(flag=flag, value=value)
                    for flag, value in flags.items()
                ]
                session.bulk_save_objects(entries)

    def get(self, flag: Flag) -> Value | None:
        """Get the flag saved or None if the flag is not found."""
        with self.session_factory() as session:
            stmt = select(FlagEntry).where(FlagEntry.flag == flag).limit(1)
            entry = session.execute(stmt).scalars().first()
            return entry.value if entry else None

    def get_all(self) -> dict[Flag, Value]:
        """Get all flags stored."""
        with self.session_factory() as session:
            flags = {
                entry.flag: entry.value
                for entry in session.query(FlagEntry).all()
            }
            return flags

    def clear(self) -> None:
        """Clear all flags stored."""
        with self.session_factory() as session:
            with session.begin():
                session.execute(delete(FlagEntry))
