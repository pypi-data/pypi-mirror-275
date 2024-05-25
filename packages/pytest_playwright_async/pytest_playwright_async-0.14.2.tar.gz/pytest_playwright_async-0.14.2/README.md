# Playwright Async Pytest -- ASYNC Pytest plugin for Playwright

[![pypi](https://img.shields.io/pypi/v/pytest_playwright_async.svg)](https://pypi.python.org/pypi/pytest_playwright_async)

There an official playwright plugin for pytest: [PyPI](https://pypi.org/project/pytest-playwright/) / [playwright-pytest](https://github.com/microsoft/playwright-pytest) / [intro](https://playwright.dev/python/docs/intro).
But if you need an async version, here is it!

## Installation

```shell
pip install pytest-playwright-async
```

## Example

[Here](https://github.com/m9810223/playwright-async-pytest/blob/master/tests/test_playwright.py) you can find more examples.

```py
# conftest.py
import asyncio

import pytest_asyncio


@pytest_asyncio.fixture(scope='session')
def event_loop():  # https://pytest-asyncio.readthedocs.io/en/latest/reference/fixtures.html#fixtures
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
```

```py
# test_playwright.py
import pytest
from playwright.async_api import Page


@pytest.mark.asyncio
async def test_page_async(page_async: Page):
    await page_async.goto('https://playwright.dev/')
    assert (
        await page_async.title()
        == 'Fast and reliable end-to-end testing for modern web apps | Playwright'
    )
```
