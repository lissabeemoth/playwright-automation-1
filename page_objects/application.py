import logging
import allure
from playwright.sync_api import Playwright
from playwright.sync_api import Request, Route
from .test_cases import TestCases
from .demo_pages import DemoPages


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)
        self.demo_pages = DemoPages(self.page)

    @allure.step
    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    @allure.step
    def navigate_to(self, menu: str):
        self.page.click(f"css=header >> text=\"{menu}\"")
        self.page.wait_for_load_state()

    @allure.step
    def login(self, login: str, password: str):
        self.page.get_by_label("Username:").fill(login)
        self.page.get_by_label("Password:").fill(password)
        self.page.get_by_role("button", name="Login").click()

    @allure.step
    def create_test(self, test_name: str, test_description: str):
        self.page.locator("#id_name").fill(test_name)
        self.page.get_by_label("Test description").fill(test_description)
        self.page.get_by_role("button", name="Create").click()

    @allure.step
    def intercept_request(self, url: str, payload: str):
        def handler(route: Route, request: Request):
            route.fulfill(status=200, body=payload)

        self.page.route(url, handler)

    @allure.step
    def stop_intercept_request(self, url: str):
        self.page.unroute(url)

    @allure.step
    def refresh_dashboard(self):
        self.page.click('input')

    @allure.step
    def get_total(self):
        return self.page.text_content('.total >> span')

    @allure.step
    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()