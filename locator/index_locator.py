"""
====================================
Author：樵夫
Time：2020/5/21    9:35
====================================
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    """
    首页页面元素定位
    """
    #   用户信息
    user_info = (By.XPATH, "//a[contains(text(),'我的帐户')]")
    #   退出登录
    quit_btn = (By.XPATH, "//a[text()='退出']")
    #   投标按钮
    invest_btn = (By.XPATH, "(//a[@class='btn btn-special'])[1]")
