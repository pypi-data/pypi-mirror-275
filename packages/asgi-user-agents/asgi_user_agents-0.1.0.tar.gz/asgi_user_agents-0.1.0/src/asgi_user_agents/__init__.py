from contextlib import suppress

from asgi_user_agents.datastructures import UADetails as UADetails
from asgi_user_agents.middleware import UAMiddleware as UAMiddleware

with suppress(ImportError):
    from asgi_user_agents.requests import UARequest as UARequest

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "UAMiddleware",
    "UADetails",
    "UARequest",
]
