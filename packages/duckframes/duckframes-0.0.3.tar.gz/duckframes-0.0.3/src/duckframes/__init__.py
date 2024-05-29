import ibis
from ibis import *  # noqa: F403

ibis.options.interactive = True


def connect(*args, **kwargs):
    return ibis.duckdb.connect(*args, **kwargs)


connect.__doc__ = ibis.duckdb.connect.__doc__


def sql(query: str, con: ibis.BaseBackend = ibis.duckdb.connect()):
    return con.sql(query)


sql.__doc__ = ibis.backends.sql.__doc__


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
