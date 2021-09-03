import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.home_page import HomePage
from test_data.data_home_page import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("Entering first name data. Value is: " + get_data["first_name"])
        home_page.get_textbox_name().send_keys(get_data["first_name"])
        log.info("Entering email data. Value is: " + get_data["email"])
        home_page.get_textbox_email().send_keys(get_data["email"])
        log.info("Entering password data. Value is: " + get_data["password"])
        home_page.get_textbox_password().send_keys(get_data["password"])
        home_page.get_sample_checkbox().click()
        log.info("Entering gender data. Value is: " + get_data["gender"])
        self.dropdown_select_by_text(home_page.get_dropdown_gender(), get_data["gender"])
        home_page.get_submit_button().click()
        actual_message = home_page.get_system_message().text
        assert "Success" in actual_message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_data_from_excel("test_case_2"))
    def get_data(self, request):
        return request.param


