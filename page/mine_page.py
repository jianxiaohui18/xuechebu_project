import page
from base.base_page import BasePage


class MinePage(BasePage):
    log_reg_btn = page.log_reg_btn

    def click_log_reg_btn(self):
        self.click_func(self.log_reg_btn)
