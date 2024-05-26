from typing import cast

import httpx
import parametrize_from_file as pff
import pytest
from quart import Quart, jsonify, request

from asgi_user_agents import UADetails

app = Quart(__name__)


@app.route("/")
async def home() -> str:
    ua = UADetails(cast(dict, request.scope))
    data = {
        "ua_string": ua.ua_string,
        "os": ua.os,
        "os.family": ua.os.family,
        "os.version": ua.os.version,
        "os.version_string": ua.os.version_string,
        "browser": ua.browser,
        "browser.family": ua.ua.browser.family,
        "browser.version": ua.ua.browser.version,
        "browser.version_string": ua.ua.browser.version_string,
        "device": ua.device,
        "device.family": ua.device.family,
        "device.brand": ua.device.brand,
        "device.model": ua.device.model,
        "is_provided": ua.is_provided,
        "is_tablet": ua.is_tablet,
        "is_mobile": ua.is_mobile,
        "is_touch_capable": ua.is_touch_capable,
        "is_pc": ua.is_pc,
        "is_bot": ua.is_bot,
        "is_email_client": ua.is_email_client,
    }
    return jsonify(data)


@pytest.mark.asyncio
@pff.parametrize(path="assets/test_middleware.json")
async def test_user_agent_data(ua_string: str, response_data: dict) -> None:
    async with httpx.AsyncClient(app=app) as client:
        response = await client.get(
            "http://testserver/", headers={"User-Agent": ua_string}
        )
        data = response.json()
        assert data["ua_string"] == response_data["ua_string"]
        assert data["os"] == response_data["os"]
        assert data["os.family"] == response_data["os.family"]
        assert data["os.version"] == response_data["os.version"]
        assert data["os.version_string"] == response_data["os.version_string"]
        assert data["browser"] == response_data["browser"]
        assert data["browser.family"] == response_data["browser.family"]
        assert data["browser.version"] == response_data["browser.version"]
        assert data["browser.version_string"] == response_data["browser.version_string"]
        assert data["device"] == response_data["device"]
        assert data["device.family"] == response_data["device.family"]
        assert data["device.brand"] == response_data["device.brand"]
        assert data["device.model"] == response_data["device.model"]
        assert data["is_provided"] is response_data["is_provided"]
        assert data["is_tablet"] is response_data["is_tablet"]
        assert data["is_mobile"] is response_data["is_mobile"]
        assert data["is_touch_capable"] is response_data["is_touch_capable"]
        assert data["is_pc"] is response_data["is_pc"]
        assert data["is_bot"] is response_data["is_bot"]
        assert data["is_email_client"] is response_data["is_email_client"]
