from pytest import mark
import allure

ddt = {
    'argnames': 'name,description',
    'argvalues': [('hello', 'world'),
                    ('hello', ''),
                    ('123', 'world')],
    'ids': ['general test', 'test no description', 'test with digits']
}


@allure.title('New test case creation')
@mark.parametrize(**ddt)
def test_new_testcase(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exist(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)


@allure.title('Test case not exist')
def test_testcase_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    assert not desktop_app_auth.test_cases.check_test_exist('hjgjhgjvghgchgvh')


