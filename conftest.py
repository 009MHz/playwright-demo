import pytest
import os
import asyncio
import allure
from utils.browser_config import Config
from playwright.async_api import async_playwright

runner = Config()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test', help='Specify the test environment')
    parser.addoption('--mode', help='Specify the execution mode: local, grid, pipeline', default='local')
    parser.addoption('--headless', action='store_true', default=False, help='Run tests in headless mode')
    parser.addoption('--browsers', action='store', default='chromium',
                     help='Comma-separated list of browsers to run tests on: chromium, firefox, webkit')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))


@pytest.fixture(scope="session")
async def playwright():
    async with async_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
async def browser(playwright, request):
    browsers = request.config.getoption('browsers').split(',')
    for browser_type in browsers:
        await runner.setup_browser(playwright, browser_type)
        yield runner.browsers[browser_type]


@pytest.fixture()
async def page(browser):
    page_instance = await runner.setup_page()
    yield page_instance
    await runner.capture_handler()
    await page_instance.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        screenshot_path = os.path.join("reports/screenshots", f"{item.name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

        try:
            page = item.funcargs.get('page') or item.funcargs.get('auth_page')
            if page:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(page.screenshot(path=screenshot_path, full_page=True))
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")


def pytest_generate_tests(metafunc):
    browsers = metafunc.config.getoption('browsers').split(',')
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize('browser', browsers, scope='session', indirect=True)


@pytest.fixture(autouse=True)
def _browser_per_test(request, browser):
    if request.cls is not None:
        request.cls.browser = browser
