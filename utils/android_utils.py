from config import file_path


def android_get_desired_capabilities():

    return {
        'autoGrantPermissions': True,
        'automationName': "uiautomator2",
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': "Android",
        'platformVersion': "11",
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': "emulator-5554",
        'app': f"{file_path}",
        'appWaitForLaunch': False,
        'appPackage': "com.ajaxsystems",
        'appActivity': "com.ajaxsystems.ui.activity.LauncherActivity"
    }
