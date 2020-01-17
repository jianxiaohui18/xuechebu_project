import time

import allure
import pytest

from conftest import BASE_DIR
from page.page_factory import PageFactory
from read_data.read_login_data import read_data
from utils import init_driver


class TestLogin(object):
    @pytest.fixture(autouse=True)
    def before(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

        yield
        time.sleep(2)
        self.driver.quit()
    @pytest.mark.parametrize('type,username,pwd,expect',read_data())
    def test_login(self,type,username,pwd,expect):
        if type:

            # 点击我的
            self.page_factory.first_page().click_mine_btn()
            # 点击登录按钮
            self.page_factory.mine_page().click_log_reg_btn()
            # 输入用户名
            self.page_factory.login_page().input_username(username)
            #输入密码
            self.page_factory.login_page().input_password(pwd)
            #点击登录
            self.page_factory.login_page().click_login_btn()
            #点击弹出框
            self.page_factory.login_page().click_alter_btn()

            # #正向
            # self.page_factory.login_page().login_func(username,pwd)
            # #获取用户名
            # username_text = self.page_factory.mine_page().get_username_text()
            # # print(username_text)
            # #断言
            # assert username_text in expect
        else:
            #反向
            # 点击我的
            self.page_factory.first_page().click_mine_btn()
            # 点击登录按钮
            self.page_factory.mine_page().click_log_reg_btn()
            # 输入用户名
            self.page_factory.login_page().input_username(username)
            # #输入密码
            self.page_factory.login_page().input_password(pwd)
            # #点击登录
            self.page_factory.login_page().click_login_btn()

            # 截图
            image_name = BASE_DIR + '/image/info_{}.png'.format(time.strftime('%Y%m%d_%H%M%S'))
            self.driver.get_screenshot_as_file(image_name)
            # 注意: 需要打开生成截图文件, 再写入 allure 报告
            with open(image_name, 'rb') as f:
                # 注意: 写入语法必须保证在 with open() 方法的作用域范围内
                allure.MASTER_HELPER.attach('info', f.read(), allure.MASTER_HELPER.attach_type.PNG)


            # #获取弹出信息
            toast_msg = self.page_factory.login_page().get_toast_message(expect)
            print(toast_msg)
            #断言
            assert expect in toast_msg



