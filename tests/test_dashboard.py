import json
import allure


@allure.title('Test dashboard data')
def test_dashboard_data(desktop_app_auth):
    payload = json.dumps({"total": 0, "passed": 0, "failed": 0, "norun": 0})
    desktop_app_auth.intercept_request('**/getstat/', payload)
    #desktop_app_auth.intercept_request('http://127.0.0.1:8000/getstat/', payload)
    desktop_app_auth.refresh_dashboard()
    desktop_app_auth.stop_intercept_request('**/getstat/')
    assert desktop_app_auth.get_total() == '0'

