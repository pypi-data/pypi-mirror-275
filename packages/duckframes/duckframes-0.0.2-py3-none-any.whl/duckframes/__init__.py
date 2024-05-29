import ibis
from ibis import *  # noqa: F403

ibis.options.interactive = True


def connect(*args, **kwargs):
    return ibis.duckdb.connect(*args, **kwargs)


connect.__doc__ = ibis.duckdb.connect.__doc__


def sql(query: str, con: ibis.BaseBackend = ibis.duckdb.connect()):
    return con.sql(query)


sql.__doc__ = ibis.backends.sql.__doc__
