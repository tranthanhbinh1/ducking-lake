import json
from datetime import datetime

from sqlalchemy import (
    Engine,
    create_engine,
)
from sqlalchemy.orm import scoped_session, sessionmaker

from patterns import SingletonWrapper


class PostgresEngineSingleton(SingletonWrapper):
    pass


class PostgresDatabaseSingleton(SingletonWrapper):
    pass


def json_serializer(d):
    def _default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    return json.dumps(d, default=_default)


def init_postgres_engine(
    username: str,
    password: str,
    host: str,
    port: int,
    db: str,
    pool_size: int = 5,
    max_overflow: int = 10,
    debug: bool = False,
):
    return create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{db}",
        json_serializer=json_serializer,
        pool_size=pool_size,
        max_overflow=max_overflow,
        echo=debug,
    )


def init_postgres_connection(*args, **kwargs):
    return init_postgres_engine(*args, **kwargs).connect()


def establish_postgres_connection(*args, **kwargs):
    return PostgresDatabaseSingleton(init_postgres_connection, *args, **kwargs)


def establish_postgres_engine(*args, **kwargs):
    return PostgresEngineSingleton(init_postgres_engine, *args, **kwargs)


def get_postgres_session_factory(engine: Engine):
    return sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_postgres_scoped_session(engine: Engine):
    return scoped_session(get_postgres_session_factory(engine))
