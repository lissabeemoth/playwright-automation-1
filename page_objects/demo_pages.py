from playwright.sync_api import Page
import allure


class DemoPages:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def open_page_after_wait(self, wait_time: int):
        self.page.fill('.waitPageTime', str(wait_time))
        with self.page.expect_navigation(wait_until='load', timeout=(wait_time + 1) * 1000):
            self.page.click('.waitPage', no_wait_after=True)

    @allure.step
    def check_wait_page(self):
        return 'Wait Page' == self.page.text_content('h3')

    @allure.step
    def open_page_and_wait_ajax(self, wait_time: int):
        self.page.fill('.waitAjaxRequests', str(wait_time))
        self.page.click('.waitAjax')
        self.page.wait_for_load_state('networkidle')

    @allure.step
    def get_ajax_responses_count(self):
        return len(self.page.query_selector_all('css=.ajaxResponses > p'))


