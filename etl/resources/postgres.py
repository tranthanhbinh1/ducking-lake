from contextlib import contextmanager
from dagster import ConfigurableResource, InitResourceContext
from pydantic import PrivateAttr
from sqlalchemy import Engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from infrastructure.db.postgres import (
    establish_postgres_engine,
    get_postgres_session_factory,
)


class PostgresResource(ConfigurableResource):
    username: str
    password: str
    hostname: str
    db_name: str
    port: int = 5432
    _engine: Engine = PrivateAttr()
    _conn: Connection = PrivateAttr()
    _session: Session = PrivateAttr()

    @contextmanager
    def yield_for_execution(self, context: InitResourceContext):
        # keep connection open for the duration of the execution
        # set up the connection attribute, so it can be used in the execution

        self._engine = establish_postgres_engine(
            self.username,
            self.password,
            self.hostname,
            self.db_name,
            self.port,
            # Advanced connection handling for Postgres
            # pool_size=config.POSTGRESQL_POOL_SIZE,
            # max_overflow=config.POSTGRESQL_MAX_OVERFLOW,
        )

        self._conn = self._engine.connect()

        LocalSession = get_postgres_session_factory(self._engine)
        self._session = LocalSession()

        try:
            # yield, allowing execution to occur
            yield self
        finally:
            self._session.close()
            self._conn.close()

    @property
    def engine(self):
        return self._engine

    @property
    def conn(self):
        return self._conn

    @property
    def session(self):
        return self._session
