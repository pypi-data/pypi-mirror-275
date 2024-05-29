# TODO: refactor (or just delete everything)
import ibis
from ibis import (
    _,  # noqa
    NA as NULL,  # noqa
    asc,  # noqa
    udf,  # noqa
    now,  # noqa
    case,  # noqa
    time,  # noqa
    date,  # noqa
    uuid,  # noqa
    where,  # noqa
    range,  # noqa
    today,  # noqa
    to_sql,  # noqa
    schema,  # noqa
    ifelse,  # noqa
    random,  # noqa
    window,  # noqa
    struct,  # noqa
    literal,  # noqa
    options,  # noqa
    coalesce,  # noqa
    examples,  # noqa
    selectors,  # noqa
    timestamp,  # noqa
    row_number,  # noqa
    read_csv,  # noqa
    read_json,  # noqa
    read_delta,  # noqa
    read_parquet,  # noqa
)  # noqa
from ibis.backends.duckdb import *  # noqa: F403

options.interactive = True


def connect(*args, **kwargs):
    return ibis.duckdb.connect(*args, **kwargs)


connect.__doc__ = ibis.duckdb.connect.__doc__


def col(name: str):
    return ibis._[name]


col.__doc__ = ibis._.__doc__

con = connect()  # magic connection
ibis.set_backend(con)


def sql(query: str, con: ibis.BaseBackend = con):
    return con.sql(query)


sql.__doc__ = ibis.backends.sql.__doc__


def list_tables(con: ibis.BaseBackend = con):
    return con.list_tables()


list_tables.__doc__ = ibis.BaseBackend.list_tables.__doc__


def table(name: str, con: ibis.BaseBackend = con):
    return con.table(name)


table.__doc__ = ibis.BaseBackend.table.__doc__


# TODO: should these from_* methods create tables on `con`?
def from_pyarrow(arrow_object):
    """
    Convert a PyArrow object to an DuckFrames DataFrame.
    """
    return ibis.memtable(arrow_object)


def from_pandas(df):
    """
    Convert a pandas DataFrame to a DuckFrames DataFrame.
    """
    return ibis.memtable(df)


def from_polars(pl_table):
    """
    Convert a polars DataFrame to a DuckFrames DataFrame.
    """
    return ibis.memtable(pl_table)
