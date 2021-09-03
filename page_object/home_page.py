from selenium.webdriver.common.by import By

from page_object.checkout_page import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, '//a[contains(text(), "Shop")]')
    name = (By.XPATH, '//div[@class="container"]/form/div[1]/input')
    email = (By.XPATH, '//div[@class="container"]/form/div[2]/input')
    password = (By.XPATH, '//div[@class="container"]/form/div[3]/input')
    sample_checkbox = (By.XPATH, '//input[@id="exampleCheck1"]')
    submit = (By.CSS_SELECTOR, '[type="submit"]')
    dropdown = (By.CSS_SELECTOR, '[id="exampleFormControlSelect1"]')
    message = (By.XPATH, '//div[@class="container"]/div[2]')

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page

    def get_textbox_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_textbox_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_textbox_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_sample_checkbox(self):
        return self.driver.find_element(*HomePage.sample_checkbox)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_dropdown_gender(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_system_message(self):
        return self.driver.find_element(*HomePage.message)
