import logging
import pytest
import os
import asyncio
import allure
from utils.browser_config import Config
from playwright.async_api import async_playwright
from dotenv import load_dotenv

runner = Config()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test', help='Specify the test environment')
    parser.addoption('--mode', help='Specify the execution mode: local, grid, pipeline', default='local')
    parser.addoption('--headless', action='store_true', default=False, help='Run tests in headless mode')
    parser.addoption(
        '--browsers',
        action='store',
        help="Specify browsers (comma-separated): chromium,firefox,webkit"
    )


def pytest_configure(config):
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))
    os.environ["screenshot"] = config.getoption('screenshot')

    single_mode = config.getoption('browser')
    multi_mode = config.getoption('browsers')

    if isinstance(single_mode, list) and len(single_mode) == 1:
        # logging.info(f"Single browser retrieved: {single_mode}")
        os.environ["browser"] = single_mode[0]
    elif not single_mode:
        os.environ["browser"] = "chromium"
    else:
        os.environ["browser"] = single_mode

    if multi_mode:
        for i in multi_mode.split(','):
            # logging.info(f"Retrieved multi browser: {i}")
            os.environ["browser"] = i

    load_dotenv(".env")


@pytest.fixture()
async def playwright():
    async with async_playwright() as playwright:
        yield playwright


@pytest.fixture()
async def browser(playwright):
    await runner.setup_browser(playwright)
    yield runner.browser
    await runner.browser.close()


@pytest.fixture()
async def page(browser):
    page_instance = await runner.setup_page()
    yield page_instance
    # await runner.capture_handler()
    await page_instance.close()


@pytest.fixture()
async def user_auth(browser):
    page_instance = await runner.setup_auth_page("user")
    yield page_instance
    await page_instance.close()


@pytest.fixture()
async def basic_auth(browser):
    page_instance = await runner.setup_auth_page("basic")
    yield page_instance
    await page_instance.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    screenshot_mode = os.environ.get("screenshot", "off")

    # Reporter Flag based on CLI
    if screenshot_mode == "on":
        extract_attachment = rep.when == "call"
    elif screenshot_mode == "only-on-failure":
        extract_attachment = rep.when == "call" and rep.failed
    else:
        extract_attachment = False

    if extract_attachment:
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
                        name=item.name,
                        attachment_type=allure.attachment_type.PNG
                    )
        except Exception as e:
            logging.error(f"Failed to take screenshot for {item.name}: {e}")


def pytest_generate_tests(metafunc):
    multi_browser = metafunc.config.getoption('browsers')
    if multi_browser:
        browsers = multi_browser.split(',')
        if 'browser' in metafunc.fixturenames:
            metafunc.parametrize('browser', browsers, indirect=True)


@pytest.fixture(autouse=True)
def _browser_per_test(request, browser):
    if request.cls is not None:
        request.cls.browser = browser
