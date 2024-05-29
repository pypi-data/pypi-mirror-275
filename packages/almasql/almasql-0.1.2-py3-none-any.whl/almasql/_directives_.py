import typing

import jinja2

if typing.TYPE_CHECKING:
    from . import _query_


jinja2environment = jinja2.Environment()


def custom_directive[T: typing.Any](source: T) -> T:
    jinja2environment.globals[source.__name__] = source
    return source


def get_query() -> '_query_.query':
    query = jinja2environment.globals.get('query')
    if query is None:
        raise RuntimeError('query is not defined')
    return query


@custom_directive
def _(v: str) -> str:
    query = get_query()
    k = query.bind_parameter(v)
    return f":{k}"


_separator = ', '


@custom_directive
def unpack(x: typing.Iterable[str]) -> str:
    return _separator.join([_(i) for i in x])


@custom_directive
def set(x: typing.Mapping) -> str:
    return "SET " + _separator.join([f"{i} = {_(x[i])}" for i in x])


@custom_directive
def values(x: typing.Mapping) -> str:
    return f"({_separator.join(x)}) VALUES ({unpack(x.values())})"
