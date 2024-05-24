import contextlib
import os
import sys
from typing import Tuple

import teradatasql
from attrs import frozen

# od verze 3.9 je k dispozici collections.abc.Generator, ve starších verzích typing.Generator
_version = (sys.version_info.major * 100) + sys.version_info.minor
if _version > 309:
    from collections.abc import Generator
else:
    from typing import Generator


def _one_of(keys: list[str], default=None) -> str | None:
    for k in keys:
        try:
            val = os.environ[k]
            return val
        except KeyError:
            continue
    return default


@frozen
class Config:
    tdpid: str
    user: str
    password: str
    logmech: str


def config(env: str | None = None) -> Config:
    """returns a connection configuration based on env variables.

    Args:
        env (str | None): optional name of the environment
        if env is None, following variables are used:
            TO2_DOMAIN_USER, TO2_DOMAIN_PASSWORD (with LDAP auth)
        otherwise, following env variables are used:
            TO2_TERA{env}_USER, TO2_TERA{env}_PASSWORD, TO2_TERA{env}_LOGMEC

    Returns:
        Config: configuration for connect string
    """
    if env is None:
        return Config(
            tdpid=_one_of(["TERADATA_HOSTNAME"], default="edwprod.cz.o2"),
            user=os.environ["TO2_DOMAIN_USER"],
            password=os.environ["TO2_DOMAIN_PASSWORD"],
            logmech="LDAP",
        )
    return Config(
        tdpid=_one_of(["TERADATA_HOSTNAME"], default="edwprod.cz.o2"),
        user=os.environ[f"TO2_TERA{env}_USER"],
        password=os.environ[f"TO2_TERA{env}_PASSWORD"],
        logmech=_one_of([f"TO2_TERA{env}_LOGMEC"], default="TD2"),
    )


DEFAULT_HOSTNAME = _one_of(["TERADATA_HOSTNAME"], default="edwprod.cz.o2")
DEFAULT_USER = _one_of(["TERADATA_USER", "TO2_DOMAIN_USER"], default=None)
DEFAULT_PASSWORD = _one_of(["TERADATA_PASSWORD", "TO2_DOMAIN_PASSWORD"], default=None)
DEFAULT_LOGMECH = _one_of(["TERADATA_LOGMECH"], default="LDAP")


class ParameterError(ValueError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def select(
    sql: str,
    env: str | None = None,
    *,
    data: Tuple = None,
) -> list[dict]:
    """Connect to Teradata,e xecute query, and return all rows as list of dictionaries.
    Keys to the dictionary is always name of the column.

    Args:
        sql (str): the query
        env (str | None, optional): name of the configuration, see config
        data (Tuple, optional): data given to the query

    Returns:
        list[dict]: dataset
    """

    cfg = config(env)
    with teradatasql.connect(
        host=cfg.tdpid,
        user=cfg.user,
        password=cfg.password,
        logmech=cfg.logmech,
    ) as sess:
        with sess.cursor() as cur:
            if data is None:
                rows = [r for r in cur.execute(sql)]
            else:
                rows = [r for r in cur.execute(sql, data)]
            headers = [d[0].lower() for d in cur.description]
    result = [dict(zip(headers, row)) for row in rows]
    return result


@contextlib.contextmanager
def connect_teradata(
    hostname: str = DEFAULT_HOSTNAME,
    username: str = DEFAULT_USER,
    password: str = DEFAULT_PASSWORD,
    logmech: str | None = DEFAULT_LOGMECH,
    tmode: str = "TERA",
) -> Generator[teradatasql.TeradataConnection, None, None]:
    """Simple context manager, which can connect to Teradata using "sensible defaults".

    Args:
        hostname (str): hostname, defaults to DEFAULT_HOSTNAME ("edwprod.cz.o2")
        username (str): defaults to os.environ['TO2_DOMAIN_USER']
        password (str): defaults to os.environ['TO2_DOMAIN_PASSWORD']
        logmech (str, optional): defaults to "LDAP".
        tmode (str): ANSI or TERA; defaults to TERA

    Returns:
        teradatasql.TeradataConnection

    Throws:
        any error supported by the teradatasql module
    """
    if username is None:
        raise ParameterError(
            "username: should not be None. You can set it as ENV variable: TERADATA_USER, TO2_DOMAIN_USER"
        )
    if password is None:
        raise ParameterError("password: should not be None")
    with teradatasql.connect(
        host=hostname, user=username, password=password, logmech=logmech
    ) as session:
        yield session
