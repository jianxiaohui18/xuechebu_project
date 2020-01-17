"""
PO 文件基类
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # def find_element_func(self, location):
    #     """元素定位方法"""
    #     # return self.driver.find_element(location[0], location[1])
    #     return self.driver.find_element(*location)  # *location 拆包操作

    def find_element_func(self, location, timeout=5, poll=.5):
        """
        元素定位方法
        :param location: 元素定位信息
        :param timeout: 超时时长
        :param poll: 执行间隔
        :return: 元素对象
        """
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*location))
        return element

    def click_func(self, location, timeout=5, poll=.5):
        """
        元素点击方法
        :param element: 元素对象
        :return: 无
        """
        element = self.find_element_func(location)
        element.click()

    def input_func(self, location, text):
        """
        元素输入方法
        :param element: 元素对象
        :param text: 文本信息
        :return: 无
        """
        element = self.find_element_func(location)
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def get_toast_message(self, text, timeout=2, poll=.2):
        toast_str = By.XPATH, '//*[contains(@text,"{}")]'.format(text)
        element = self.find_element_func(toast_str, timeout, poll)
        return element.text
