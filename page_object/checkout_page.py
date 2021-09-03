from selenium.webdriver.common.by import By

from page_object.confirm_page import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    displayed_phones = (By.XPATH, '//div[@class="card-body"]/h4/a')
    select_phone = (By.XPATH, '//div[@class="card-body"]/h4/a/parent::h4/parent::div/parent::div/div[2]/button')
    checkout_button = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    cart_checkout_button = (By.XPATH, '//button[@class="btn btn-success"]')

    def grab_phone_names(self):
        return self.driver.find_elements(*CheckOutPage.displayed_phones)

    def select_phone_name(self):
        return self.driver.find_element(*CheckOutPage.select_phone)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)

    def get_cart_checkout_button(self):
        self.driver.find_element(*CheckOutPage.cart_checkout_button).click()
        cart_checkout = ConfirmPage(self.driver)
        return cart_checkout
