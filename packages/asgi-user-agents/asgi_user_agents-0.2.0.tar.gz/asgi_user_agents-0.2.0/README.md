# asgi-user-agents

[![CI](https://github.com/hasansezertasan/asgi-user-agents/actions/workflows/ci.yml/badge.svg)](https://github.com/hasansezertasan/asgi-user-agents/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![Coverage](https://img.shields.io/codecov/c/github/hasansezertasan/asgi-user-agents)](https://codecov.io/gh/hasansezertasan/asgi-user-agents)
[![PyPI - Version](https://img.shields.io/pypi/v/asgi-user-agents.svg)](https://pypi.org/project/asgi-user-agents)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asgi-user-agents.svg)](https://pypi.org/project/asgi-user-agents)
[![License](https://img.shields.io/github/license/hasansezertasan/asgi-user-agents.svg)](https://github.com/hasansezertasan/asgi-user-agents/blob/main/LICENSE)
[![Latest Commit](https://img.shields.io/github/last-commit/hasansezertasan/asgi-user-agents)](https://github.com/hasansezertasan/asgi-user-agents)

[![Downloads](https://pepy.tech/badge/asgi-user-agents)](https://pepy.tech/project/asgi-user-agents)
[![Downloads/Month](https://pepy.tech/badge/asgi-user-agents/month)](https://pepy.tech/project/asgi-user-agents)
[![Downloads/Week](https://pepy.tech/badge/asgi-user-agents/week)](https://pepy.tech/project/asgi-user-agents)

[User Agents][python-user-agents] integration for [ASGI](https://asgi.readthedocs.io/en/latest/) applications. Works with Starlette, FastAPI, Quart, Litestar -- or any other web framework supporting ASGI that exposes the ASGI `scope`.

-----

## Table of Contents

- [asgi-user-agents](#asgi-user-agents)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [How does it work?](#how-does-it-work)
  - [Usage](#usage)
  - [API Reference](#api-reference)
    - [`UAMiddleware`](#uamiddleware)
    - [`UADetails`](#uadetails)
    - [`UARequest`](#uarequest)
  - [Development](#development)
  - [Author](#author)
  - [Credits](#credits)
  - [Analysis](#analysis)
  - [License](#license)

## Installation

**NOTE**: This is alpha software. Please be sure to pin your dependencies.

> Latest Release

```bash
pip install asgi-user-agents
```

> Development Version

```bash
pip install git+https://github.com/hasansezertasan/asgi-user-agents.git
```

## How does it work?

It simply adds a `ua` attribute to the request scope. This attribute is an instance of the `UADetails` class which abstracts the `UserAgent` class from the `user-agents` package 📄.

## Usage

It's pretty simple. Just add the middleware to your ASGI application and access the `ua` attribute from the request scope.

```python
from asgi_user_agents import UAMiddleware
from asgi_user_agents import UARequest as Request
from fastapi.applications import FastAPI
from starlette.middleware import Middleware
from starlette.responses import JSONResponse, Response


app = FastAPI(middleware=[Middleware(UAMiddleware)])


@app.get("/")
async def index(request: Request) -> Response:
    ua = request.scope["ua"]
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
    return JSONResponse(data)

```

## API Reference

### `UAMiddleware`

An ASGI middleware that sets `scope["ua"]` to an instance of [`UADetails`](#uadetails) (`scope` refers to the ASGI scope).

```python
app = UAMiddleware(app)
```

### `UADetails`

A helper that provides shortcuts for accessing [`User-Agent` request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).

```python
ua = UADetails(scope)
```

- `ua: UserAgent` - The `UserAgent` instance from the `user-agents` package.
- `ua_string: str` - The user agent string.
- `is_provided: bool` - `True` if the user agent string is provided.
- `os: OperatingSystem` - The operating system details of the user agent. It's a named tuple with the following fields:
  - `family: str` - The family of the operating system.
  - `version: str` - The version of the operating system.
  - `version_string: str` - The version of the operating system as a string.
- `browser: Browser` - The browser details of the user agent. It's a named tuple with the following fields:
  - `family: str` - The family of the browser.
  - `version: str` - The version of the browser.
  - `version_string: str` - The version of the browser as a string.
- `device: Device` - The device details of the user agent. It's a named tuple with the following fields:
  - `family: str` - The family of the device.
  - `brand: str` - The brand of the device.
  - `model: str` - The model of the device.
- `is_tablet: bool` - `True` if the request was made by a tablet.
- `is_mobile: bool` - `True` if the request was made by a mobile device.
- `is_touch_capable: bool` - `True` if the request was made by a touch-capable device.
- `is_pc: bool` - `True` if the request was made by a PC.
- `is_bot: bool` - `True` if the request was made by a bot.
- `is_email_client: bool` - `True` if the request was made by an email client.

### `UARequest`

For Starlette-based frameworks, use this instead of the standard `starlette.requests.Request` so that code editors understand that `request.scope["ua"]` contains an `UADetails` instance:

```python
from asgi_user_agents import UARequest as Request

async def home(request: Request):
    reveal_type(request.scope["ua"])  # Revealed type is 'UADetails'
```

## Development

Clone the repository and cd into the project directory:

```bash
git clone https://github.com/hasansezertasan/asgi-user-agents
cd asgi-user-agents
```

Install hatch, you can follow the instructions [here](https://hatch.pypa.io/latest/install/), or simply run the following command:

```bash
pipx install hatch
```

Initialize the environment and install the dependencies:

```bash
hatch shell
```

Initialize pre-commit hooks by running the following command:

```bash
pre-commit install
```

Make your changes on a new branch and run the tests:

```bash
hatch test -a
```

Make sure that the code is typed, linted, and formatted correctly:

```bash
hatch run types:all
```

Stage your changes and commit them:

```bash
git add .
git commit -m "Your message"
```

Push your changes to the repository:

```bash
git push
```

Create a pull request and wait for the review 🤓.

## Author

- [Hasan Sezer Taşan](https://www.github.com/hasansezertasan), It's me 👋.

## Credits

- This project wouldn't be possible without the [user-agents][python-user-agents] package 🙏.
- The project structure is inspired by the [asgi-htmx](https://github.com/florimondmanca/asgi-htmx) 🚀 package and contains some code snippets from it 😅 (even this file).

## Analysis

- [Snyk Python Package Health Analysis](https://snyk.io/advisor/python/asgi-user-agents)
- [Libraries.io - PyPI](https://libraries.io/pypi/asgi-user-agents)
- [Safety DB](https://data.safetycli.com/packages/pypi/asgi-user-agents)
- [PePy Download Stats](https://www.pepy.tech/projects/asgi-user-agents)
- [PyPI Download Stats](https://pypistats.org/packages/asgi-user-agents)
- [Pip Trends Download Stats](https://piptrends.com/package/asgi-user-agents)

## License

`asgi-user-agents` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

<!-- Links -->
[python-user-agents]: https://github.com/selwin/python-user-agents
