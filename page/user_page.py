"""
====================================
Author：樵夫
Time：2020/5/25    20:17
====================================
"""
from common.base_page import BasePage
from locator.user_locator import UserLocator


class UserPage(BasePage):

    def get_user_amount(self):
        """获取用户余额"""
        str = self.get_element_text(UserLocator.user_amount_ele, "用户页面_获取用户余额")
        amount = str.replace("元", "")
        return amount
