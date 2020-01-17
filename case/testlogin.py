import time

import pytest

from page.page_factory import PageFactory
from utils import init_driver


class TestLogin(object):
    @pytest.fixture(autouse=True)
    def before(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

        yield
        time.sleep(2)
        self.driver.quit()
    def test_login(self):
        #点击我的
        self.page_factory.first_page().click_mine_btn()
        #点击登录按钮
        self.page_factory.mine_page().click_log_reg_btn()
        #输入用户名
        # self.page_factory.login_page().input_username('18779128978')
        # #输入密码
        # self.page_factory.login_page().input_password('199305038023jxh')
        # #点击登录
        # self.page_factory.login_page().click_login_btn()
        # #点击弹出框
        # self.page_factory.login_page().click_alter_btn()

        self.page_factory.login_page().login_func('18779128978','199305038023jxh')


