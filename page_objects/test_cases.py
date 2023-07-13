from playwright.sync_api import Page
import allure


class TestCases:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_test_exist(self, test_name: str):
        return self.page.query_selector(f'css=tr >> text=\"{test_name}\"') is not None

    @allure.step
    def delete_test_by_name(self, test_name: str):
        row = self.page.query_selector(f'*css=tr >> text=\"{test_name}\"')
        row.query_selector('.deleteBtn').click()
