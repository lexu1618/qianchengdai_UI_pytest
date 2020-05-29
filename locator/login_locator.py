"""
====================================
Author：樵夫
Time：2020/5/21    9:35
====================================
"""
from selenium.webdriver.common.by import By


class LoginLocator:
    """
    登录页面元素定位
    """
    #   用户名
    phone_ele = (By.XPATH, "//input[@name='phone']")
    #   密码
    pwd_ele = (By.XPATH, "//input[@name='password']")
    #   登录按钮
    login_btn = (By.XPATH, "//button[text()='登录']")
    #   文本框错误信息
    error_info = (By.XPATH, "//div[@class='form-error-info']")
    #   弹框错误信息
    alert_info = (By.XPATH, "//div[@class='layui-layer-content']")
    #   记住手机号
    re_mobile = (By.XPATH, '//input[@name="remember_me"]')
