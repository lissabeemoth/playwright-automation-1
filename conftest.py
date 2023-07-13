import logging
import allure
# from settings import *
from pytest import fixture, hookimpl
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.application import App


@fixture(autouse=True, scope='session')
def preconditions():
    logging.info('precondition started')
    yield
    logging.info('postcondition started')


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop_app(get_playwright):
    app = App(get_playwright, base_url='http://127.0.0.1:8000')
    app.goto('/')
    yield app
    app.close()


@fixture
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login('alice', 'Qamania123')
    yield app


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    result = outcome.get_result()
    # setup>>call>>teardown
    setattr((item, f'result_{result.when}', result))


@fixture(scope='function', autouse=True)
def make_screenshots(request):
    yield
    if request.node.result_call.failed:
        for arg in request.node.funcargs.values():
            if isinstance(arg, App):
                allure.attach(body=arg.page.screenshot(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)


def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')

