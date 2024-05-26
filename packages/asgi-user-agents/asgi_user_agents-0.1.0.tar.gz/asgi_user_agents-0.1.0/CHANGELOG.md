# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

* Nothing yet.

## [0.1.0] - 2024-05-26

* Initial release.

## Added

* CI/CD Pipelines added. by [@hasansezertasan](https://github.com/hasansezertasan) in [#1](https://github.com/hasansezertasan/asgi-user-agents/pull/1)
* Update branch names on CI/CD Pipelines. by [@hasansezertasan](https://github.com/hasansezertasan) in [#2](https://github.com/hasansezertasan/asgi-user-agents/pull/2)
* Add `Scope`, `Message`, `Receive`, `Send`, and `ASGIApp` types from `starlette.types` for type hinting. by [@hasansezertasan](https://github.com/hasansezertasan) in [#3](https://github.com/hasansezertasan/asgi-user-agents/pull/3)
* Add `UADetails` data structure that provides information about the user agent extracted from the request headers. by [@hasansezertasan](https://github.com/hasansezertasan) in [#4](https://github.com/hasansezertasan/asgi-user-agents/pull/4)
* Add `UARequest` that facilitates type hinting `request.scope["ua"]` in Starlette-based frameworks. by [@hasansezertasan](https://github.com/hasansezertasan) in [#5](https://github.com/hasansezertasan/asgi-user-agents/pull/5)
* Add `UAMiddleware` that automatically adds an `UADetails` instance as `scope["ua"]`. by [@hasansezertasan](https://github.com/hasansezertasan) in [#6](https://github.com/hasansezertasan/asgi-user-agents/pull/6)
* Add `py.typed` file to indicate that the package supports type hinting. by [@hasansezertasan](https://github.com/hasansezertasan) in [#7](https://github.com/hasansezertasan/asgi-user-agents/pull/7)
* Add `__init__.py` and `__about__.py` files to the `src/asgi_user_agents` directory to make it a package. by [@hasansezertasan](https://github.com/hasansezertasan) in [#8](https://github.com/hasansezertasan/asgi-user-agents/pull/8)
* Add tests for the `UADetails`, `UARequest`, and `UAMiddleware` classes with over 90% coverage. by [@hasansezertasan](https://github.com/hasansezertasan) in [#9](https://github.com/hasansezertasan/asgi-user-agents/pull/9)
* Add `README.md` with usage instructions, development guide, and simple API reference. by [@hasansezertasan](https://github.com/hasansezertasan) in [#10](https://github.com/hasansezertasan/asgi-user-agents/pull/10)
* Add `CHANGELOG.md` to document the changes in the project. by [@hasansezertasan](https://github.com/hasansezertasan) in [#11](https://github.com/hasansezertasan/asgi-user-agents/pull/11)
* Update `CHANGELOG.md` to include the changes in the project. by [@hasansezertasan](https://github.com/hasansezertasan) in [#12](https://github.com/hasansezertasan/asgi-user-agents/pull/12)

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.1.0/
[semantic versioning]: https://semver.org

<!-- Versions -->
[unreleased]: https://github.com/hasansezertasan/chrome-version/compare/0.1.0...HEAD
[0.1.0]: https://github.com/hasansezertasan/chrome-version/releases/tag/0.1.0
