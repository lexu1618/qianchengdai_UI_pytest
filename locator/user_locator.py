"""
====================================
Author：樵夫
Time：2020/5/25    20:14
====================================
"""
from selenium.webdriver.common.by import By


class UserLocator:
    #   用户余额
    user_amount_ele = (By.XPATH, "//li[@class='color_sub']")