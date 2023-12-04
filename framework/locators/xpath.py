class XpathLocators:

    @staticmethod
    def email_field():
        value = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'
        return value

    @staticmethod
    def password_field():
        value = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
        return value

    @staticmethod
    def confirm_log_in_button():
        value = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
        return value

    @staticmethod
    def sing_out_button():
        value = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View'
        return value
