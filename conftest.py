"""
====================================
Author：樵夫
Time：2020/5/29    21:13
Email：1161909073@qq.com
Company：烽台科技（北京）有限公司
====================================
"""
import pytest
from common.handlelog import log
from common.handleconfig import config
from selenium import webdriver
from page.index_page import IndexPafe
from page.invest_page import InvestPage
from page.login_page import LoginPage
from page.user_page import UserPage


@pytest.fixture(scope="class")
def invest_fixcure():
    log.info("开始执行投标的用例")
    driver = webdriver.Chrome(options=get_option())
    driver.maximize_window()
    #   获取登录页面
    login_page = LoginPage(driver)
    #   登录
    login_page.login(user=config.get("test_data", "user"), pwd=config.get("test_data", "pwd"))
    #   获取首页
    index_page = IndexPafe(driver)
    #   点击抢投标
    index_page.click_toubiao()
    #   获取投标页面
    invest_page = InvestPage(driver)
    #   获取用户页面
    user_page = UserPage(driver)
    yield invest_page, user_page
    driver.quit()
    log.info("投标用例执行完毕")


@pytest.fixture(scope="class")
def login_fixcure():
    log.info("开始执行登录的用例")
    driver = webdriver.Chrome(options=get_option())
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.click_re_mobile()
    index_page = IndexPafe(driver)
    yield login_page, index_page
    driver.quit()
    log.info("登录用例执行完毕")


def get_option():
    if config.get("env", "headless") == "True":
        """设置浏览启动的选项：无头模式"""
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        return opt
    else:
        return None