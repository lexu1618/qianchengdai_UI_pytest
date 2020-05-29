"""
====================================
Author：樵夫
Time：2020/5/24    3:16
====================================
"""
"""
前置条件：
登录
账户有钱


1、正常投标
2、错误输入，文本框提示：请输入10的整数倍
3、错误输入，弹窗提示：请正确填写投注金额
4、勾选全投，输入框展示：剩余可投款/100
"""

import pytest
from selenium import webdriver
from page.index_page import IndexPafe
from page.login_page import LoginPage
from page.invest_page import InvestPage
from page.user_page import UserPage
from common.handlelog import log
from common.handleconfig import config
from data.case_data import InvestCase
from decimal import Decimal


@pytest.fixture(scope="class")
def invest_fixcure():
    log.info("开始执行投标的用例")
    driver = webdriver.Chrome()
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


class TestInvest:

    @pytest.mark.parametrize('case', InvestCase.error_ele_case_data)
    def test_invest_ele_error(self, case, invest_fixcure):
        invest_page, user_page = invest_fixcure
        #   输入金额
        invest_page.input_invest_money(case["amount"])
        #   获取预期结果
        expected = case["expected"]
        res = invest_page.get_invest_btn_info()
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestCase.error_alert_case_data)
    def test_invest_alert_error(self, case, invest_fixcure):
        invest_page, user_page = invest_fixcure
        #   输入金额
        invest_page.input_invest_money(case["amount"])
        #   获取预期结果
        expected = case["expected"]
        #   点击投资
        invest_page.click_invest_btn()
        #   获取弹窗提示信息
        res = invest_page.get_alert_error_info()
        #   手动关闭弹框
        invest_page.click_close_alert_error_info()
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestCase.success_case_data)
    def test_invest_success(self, case, invest_fixcure):
        invest_page, user_page = invest_fixcure
        invest_page.page_refresh()
        #   获取投资前余额
        start_amount = invest_page.get_user_amount()
        #   输入金额
        invest_page.input_invest_money(case["amount"])
        #   点击投资
        invest_page.click_invest_btn()
        #   获取页面提示成功信息
        res = invest_page.get_invest_info()
        #   获取预期结果
        expected = case["expected"]
        #   点击查看投资成功的信息，跳转用户页面
        invest_page.click_invest_success_info()
        #   获取用户页面余额
        invest_amount = user_page.get_user_amount()
        try:
            assert expected == res
            assert Decimal(start_amount) - Decimal(invest_amount) == Decimal(case["amount"])
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
