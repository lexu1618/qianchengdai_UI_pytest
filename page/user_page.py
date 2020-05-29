"""
====================================
Author：樵夫
Time：2020/5/25    20:17
====================================
"""
from selenium.webdriver.remote.webdriver import WebDriver

from locator.user_locator import UserLocator


class UserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(15)

    def get_user_amount(self):
        """获取用户余额"""
        str = self.driver.find_element(*UserLocator.user_amount_ele).text
        amount = str.replace("元", "")
        return amount
