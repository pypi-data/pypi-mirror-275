from attrs import frozen


@frozen
class Config:
    schema: str
    dsn: str
    user: str
    password: str


@frozen
class CtrlJob:
    job_name: str
    stream_name: str
    priority: int | None
    cmd_line: str | None
    src_sys_id: int | None
    phase: str | None
    table_name: str | None
    job_category: str
    job_type: str | None
    toughness: str | None
    cont_anyway: int
    max_runs: int
    always_restart: int
    status_begin: int | None
    waiting_hr: int | None
    deadline_hr: int | None
    engine_id: int
    job_desc: str | None
    author: str | None
    note: str | None


@frozen
class CtrlJobDependency:
    job_name: str
    parent_job_name: str
    rel_type: str | None


@frozen
class CtrlJobTableRef:
    job_name: str
    database_name: str
    table_name: str
    lock_type: str


@frozen
class CtrlStream:
    stream_name: str
    stream_desc: str | None
    note: str | None


@frozen
class CtrlStreamDependency:
    stream_name: str
    parent_stream_name: str
    rel_type: str | None


@frozen
class CtrlStreamPlanRef:
    stream_name: str
    runplan: str
    country_cd: str | None
