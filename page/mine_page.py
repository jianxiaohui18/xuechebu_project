import page
from base.base_page import BasePage


class MinePage(BasePage):
    log_reg_btn = page.log_reg_btn
    username_text = page.username_text
    def click_log_reg_btn(self):
        self.click_func(self.log_reg_btn)
    def get_username_text(self):
        return self.find_element_func(self.username_text).text
