import subprocess
import time
from appium import webdriver
from appium.options.common import AppiumOptions
from utils.android_utils import android_get_desired_capabilities


class DriverConfiguration:

    @staticmethod
    def run_appium_browser():
        subprocess.Popen(
            ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            shell=True
        )
        time.sleep(5)

    def create_android_browser(self):
        self.run_appium_browser()
        options = AppiumOptions().load_capabilities(android_get_desired_capabilities())
        browser = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        browser.implicitly_wait(20)
        return browser


driver_instance = DriverConfiguration()
