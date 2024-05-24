import contextlib
import logging
import os
import pathlib
import typing

import oracledb

from genpypress.pdc import model

logger = logging.getLogger(__name__)


def config(
    schema: str,
    env: str | None = None,
) -> model.Config:
    """Return a config based on env variables:

    Args:
        env (str | None): name of the environment

    Returns:
        model.Config: config based on environment variables:
        when env is none:
            TO2_PDC_DSN
            TO2_PDC_USER
            TO2_PDC_PASSWORD
        when env is not NONE:
            f"TO2_PDC{env}_DSN"
            f"TO2_PDC{env}_USER"
            f"TO2_PDC{env}_PASSWORD"

    Raises:
        KeyError: when environment variables are not set.
    """
    if not env:
        env_key = "PDC"
    else:
        env_key = f"PDC{env.upper()}"
    keys = [
        f"TO2_{env_key}_DSN",
        f"TO2_{env_key}_USER",
        f"TO2_{env_key}_PASSWORD",
    ]
    try:
        dsn, user, password = [os.environ[k] for k in keys]
    except KeyError:
        err = f"Set these variables: {keys}"
        raise KeyError(err)

    return model.Config(schema=schema, dsn=dsn, user=user, password=password)


@contextlib.contextmanager
def ora_session(cfg: model.Config) -> typing.Generator[oracledb.Connection, None, None]:
    """returns a oracledb.Connnection

    Args:
        cfg (model.Config): see function config


    Yields:
        Iterator[typing.Generator[oracledb.Connection, None, None]]: a conection
    """
    with oracledb.connect(
        user=cfg.user,
        password=cfg.password,
        dsn=cfg.dsn,
    ) as sess:
        yield sess


@contextlib.contextmanager
def ora_cursor(
    cfg: model.Config | None,
) -> typing.Generator[oracledb.Cursor, None, None]:
    """Yields an oracledb cursor, based on a config.

    Args:
        cfg (model.Config | None): see function config.

    Yields:
        oracle cursor.
    """
    with ora_session(cfg) as sess:
        with sess.cursor() as curr:
            yield curr


def _get_parent_directories(path: pathlib.Path) -> list[pathlib.Path]:
    """Returns a list of all parent directories for a pathlib.Path object.

    Args:
        path: The pathlib.Path object.

    Returns:
        A list of all parent directories.
    """
    directories = []
    current_path = path
    while current_path != current_path.parent:
        logger.info(f"appending: {current_path}")
        directories.append(current_path)
        current_path = current_path.parent

    return directories


def _locate_client() -> pathlib.Path | None:
    """Returns a directory where Oracle client is installed.
    - if ORACLE_HOME env variable is defined, return it as the path
    - otherwise, try to locate the client by looking up one of:
        - oci.dll, sqlplus.exe, oci.msg, libocci.so.12.2
    - try these directories:
        - parent of TNS_ADMIN dir, if the env variable is defined
        - directories on PATH

    Returns:
        _p.Path | None: path to the client
    """
    try:
        pth = os.environ["ORACLE_HOME"]
        pth = pathlib.Path(pth)
        return pth
    except KeyError:
        pass

    dirs_to_try: list[pathlib.Path] = []
    files_to_try = ["oci.dll", "sqlplus.exe", "oci.msg", "libocci.so.12.2"]
    try:
        dirs_to_try.extend(
            _get_parent_directories(pathlib.Path(os.environ["TNS_ADMIN"]))
        )
    except KeyError:
        pass

    try:
        for pth in os.environ["PATH"].split(";"):
            dirs_to_try.append(pathlib.Path(pth))
    except KeyError:
        pass

    for pth in dirs_to_try:
        logger.info(str(pth))
        for file in files_to_try:
            if (pth / file).is_file():
                return pth

    logger.warning("failed to switch to thick client")
    logger.warning(
        "see https://python-oracledb.readthedocs.io/en/latest/user_guide/initialization.html#enablingthick for mode details"
    )
    return None


def _switch_to_thick_client():
    client_dir = _locate_client()
    if client_dir:
        oracledb.init_oracle_client(lib_dir=str(client_dir))


_switch_to_thick_client()


_PDC_TABLES = {
    model.CtrlJob: "CTRL_JOB",
    model.CtrlJobDependency: "CTRL_JOB_DEPENDENCY",
    model.CtrlJobTableRef: "CTRL_JOB_TABLE_REF",
    model.CtrlStream: "CTRL_STREAM",
    model.CtrlStreamDependency: "CTRL_STREAM_DEPENDENCY",
    model.CtrlStreamPlanRef: "CTRL_STREAM_PLAN_REF",
}


def from_pdc(
    type_: typing.Type[
        typing.Union[
            model.CtrlJob,
            model.CtrlJobDependency,
            model.CtrlJobTableRef,
            model.CtrlStream,
            model.CtrlStreamDependency,
            model.CtrlStreamPlanRef,
        ]
    ],
    cfg: model.Config,
) -> list[
    model.CtrlJob,
    model.CtrlJobDependency,
    model.CtrlJobTableRef,
    model.CtrlStream,
    model.CtrlStreamDependency,
    model.CtrlStreamPlanRef,
]:
    """Returns content of one of the supported tables.

    Args:
        type_: one of supported types from pdc.model

    Returns:
        list of all records for the type
    """
    table = _PDC_TABLES[type_]
    sql = f"select * from {cfg.schema}.{table}"
    with ora_cursor(cfg) as cur:
        handle = cur.execute(sql)
        names = [d[0].lower() for d in cur.description]
        ret_list = [type_(**dict(zip(names, row))) for row in handle]
    return ret_list
