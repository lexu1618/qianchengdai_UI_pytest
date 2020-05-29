"""
====================================
Author：樵夫
Time：2020/5/15    21:22
====================================
"""
import pytest
from selenium import webdriver
from data.case_data import LoginCase
from page.login_page import LoginPage
from page.index_page import IndexPafe
from common.handlelog import log


class TestLogin:

    @pytest.mark.parametrize("case", LoginCase.success_case_data)
    def test_login_pass(self, case, login_fixcure):
        login_page, index_page = login_fixcure
        login_page.login(case["mobile"], case["pwd"])
        res = index_page.my_use_info()
        try:
            assert case["expected"] == res
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
            index_page.click_quit()
            login_page.page_refresh()

    @pytest.mark.parametrize("case", LoginCase.error_info_case_data)
    def test_login_error_info(self, case, login_fixcure):
        login_page, index_page = login_fixcure
        login_page.page_refresh()
        login_page.login(case["mobile"], case["pwd"])
        res = login_page.get_error_info()
        try:
            assert case["expected"] == res
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.parametrize("case", LoginCase.error_alert_case_data)
    def test_login_alert_info(self, case, login_fixcure):
        login_page, index_page = login_fixcure
        login_page.page_refresh()
        login_page.login(case["mobile"], case["pwd"])
        res = login_page.get_tips_info()
        try:
            assert case["expected"] == res
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
