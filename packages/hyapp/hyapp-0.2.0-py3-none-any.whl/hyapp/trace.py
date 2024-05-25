import uuid
from contextvars import ContextVar

# See also: https://github.com/snok/asgi-correlation-id
TRACE_ID_VAR: ContextVar[str | None] = ContextVar("trace_id", default=None)


def new_trace_id(
    subprefix: str, prefix: str = "00", total_len: int = 16, parent: str | None = None, parent_sep: str = "__"
) -> str:
    uuid_len = total_len - len(prefix) - len(subprefix)
    result = prefix + subprefix + uuid.uuid4().hex[:uuid_len]
    if parent:
        result = f"{parent}{parent_sep}{result}"
    return result
