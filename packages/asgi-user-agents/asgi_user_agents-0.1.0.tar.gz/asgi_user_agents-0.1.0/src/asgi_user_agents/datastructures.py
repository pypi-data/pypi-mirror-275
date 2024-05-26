from __future__ import annotations

from typing import Optional
from urllib.parse import unquote

from user_agents.parsers import Browser, Device, OperatingSystem, UserAgent

from asgi_user_agents.types import Scope


class UADetails:
    def __init__(self, scope: Scope) -> None:
        self._scope = scope
        self._ua: UserAgent

    def _get_header(self, name: bytes) -> Optional[str]:
        return _get_header(self._scope, name)

    @property
    def _ua_string(self) -> Optional[str]:
        return self._get_header(b"User-Agent") or ""

    @property
    def ua(self) -> UserAgent:
        if not hasattr(self, "_ua"):
            self._ua = UserAgent(self._ua_string)
        return self._ua

    @property
    def ua_string(self) -> str:
        return self.ua.ua_string

    @property
    def is_provided(self) -> bool:
        return bool(self.ua_string)

    @property
    def os(self) -> OperatingSystem:
        return self.ua.os

    @property
    def browser(self) -> Browser:
        return self.ua.browser

    @property
    def device(self) -> Device:
        return self.ua.device

    @property
    def is_tablet(self) -> bool:
        return self.ua.is_tablet

    @property
    def is_mobile(self) -> bool:
        return self.ua.is_mobile

    @property
    def is_touch_capable(self) -> bool:
        return self.ua.is_touch_capable

    @property
    def is_pc(self) -> bool:
        return self.ua.is_pc

    @property
    def is_bot(self) -> bool:
        return self.ua.is_bot

    @property
    def is_email_client(self) -> bool:
        return self.ua.is_email_client


def _get_header(scope: Scope, key: bytes) -> Optional[str]:
    key = key.lower()
    value: Optional[str] = None
    should_unquote = False

    for k, v in scope["headers"]:
        if k.lower() == key:
            value = v.decode("latin-1")
        if k.lower() == b"%s-uri-autoencoded" % key and v == b"true":
            should_unquote = True

    if value is None:
        return None

    return unquote(value) if should_unquote else value
