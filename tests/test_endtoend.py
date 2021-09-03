import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.checkout_page import CheckOutPage
from page_object.confirm_page import ConfirmPage
from page_object.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        log.info("Getting all the item names")
        self.driver.implicitly_wait(10)

        phone_list = checkout_page.grab_phone_names()

        for phone in phone_list:
            log.info(phone.text)
            if phone.text == "Blackberry":
                checkout_page.select_phone_name().click()

        checkout_page.get_checkout_button().click()

        cart_checkout = CheckOutPage.get_cart_checkout_button(ConfirmPage(self.driver))

        log.info("Entering country name - sample value: Ind")
        cart_checkout.get_country_textbox().send_keys('Ind')

        time.sleep(10)

        '''wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))'''
        self.verify_link_presence('India')

        cart_checkout.get_selected_country().click()

        cart_checkout.get_agree_checkbox().click()

        cart_checkout.get_purchase_button().click()

        actual_message = cart_checkout.get_message().text
        expected_message = "Success!"
        log.info("Text received from the software is: " + actual_message)
        assert expected_message == actual_message

