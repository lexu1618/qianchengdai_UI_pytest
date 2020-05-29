"""
====================================
Author：樵夫
Time：2020/5/24    3:42
Email：1161909073@qq.com
Company：烽台科技（北京）有限公司
====================================
"""
from selenium.webdriver.common.by import By


class InvestLocator:
    """投标页面信息"""
    #   投标金额输入框
    invest_ele = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")
    #   全投选择框
    invest_all_ele = (By.XPATH, "//input[@class='set-all']")
    #   投标按钮
    invest_btn = (By.XPATH, "//button[@class='btn btn-special height_style']")
    #   投标成功提示框
    invest_success = (By.XPATH, "//div[text()='投标成功！']")
    #   投标成功点击查看更多
    click_success_info = (By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']")
    #   错误信息弹窗框
    alert_error_ele = (By.XPATH, "//div[@class='text-center']")
    #   关闭错误信息弹窗框
    re_alert_error = (By.XPATH, "//a[@class='layui-layer-btn0']")
