from framework.CommonMethods.common_methods import CommonMethods


class LoginPage(CommonMethods):

    def __init__(self, driver):
        super().__init__(driver)

    def positive_login_flow(self, credentials):
        self.click_element_by_id(self.locators.log_in_button())
        self.fill_and_submit_log_in_form(credentials)
        self.verify_log_in()
        self.log_out()

    def negative_login_flow(self, credentials):
        self.click_element_by_id(self.locators.log_in_button())
        self.fill_and_submit_log_in_form(credentials)
        self.waiter(1)
        self.verify_error_popup()
        self.click_element_by_id(self.locators.back_button())
        self.waiter(2)

    def log_out(self):
        self.click_element_by_id(self.locators.hamburger_button())
        self.click_element_by_id(self.locators.settings_button())
        self.click_element_by_xpath(self.locators.sing_out_button())

    def fill_and_submit_log_in_form(self, credentials):
        self.input_by_xpath(self.locators.email_field(), credentials[0])
        self.input_by_xpath(self.locators.password_field(), credentials[1])
        self.click_element_by_xpath(self.locators.confirm_log_in_button())

    def verify_log_in(self):
        element = self.find_element_by_id(self.locators.verification_text_id())
        text_to_verify = element.text
        assert text_to_verify == self.data.verification_text,\
            f"Data on page {text_to_verify} not similar to verification data{self.data.verification_text}"

    def verify_error_popup(self):
        element = self.find_element_by_id(self.locators.error_popup())
        assert element, "Error popup did not appear"
