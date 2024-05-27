from asgi_user_agents.datastructures import UADetails
from asgi_user_agents.types import ASGIApp, Receive, Scope, Send


class UAMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self._app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] in ("http", "websocket"):
            scope["ua"] = UADetails(scope)

        await self._app(scope, receive, send)
