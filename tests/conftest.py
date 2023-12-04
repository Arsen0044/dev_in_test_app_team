import pytest
from framework.driver_configuration import driver_instance


@pytest.fixture(scope='session')
def create_android_driver():
    driver = driver_instance.create_android_browser()
    yield driver
    driver.quit()

