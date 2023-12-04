import pytest
from data.data_container import DataContainer
from framework.page_objects.login_page import LoginPage


class TestLogin:
    data = DataContainer()
    credentials_list = data.credentials

    @pytest.mark.parametrize('credentials', credentials_list)
    def test_user_login(self, credentials, create_android_driver):
        login = LoginPage(create_android_driver)
        if isinstance(credentials, tuple):
            login.positive_login_flow(credentials)
        else:
            login.negative_login_flow(credentials)
