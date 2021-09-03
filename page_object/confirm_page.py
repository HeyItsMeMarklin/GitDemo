from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    cart_checkout_button = (By.XPATH, '//button[contains(text(),"Checkout")]')
    country_textbox = (By.XPATH, '//input[@id="country"]')
    country_name = (By.LINK_TEXT, "India")
    agree_checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchase_button = (By.XPATH, '//input[@type="submit"]')
    message = (By.CSS_SELECTOR, '[class*="alert-success"] strong')

    def get_country_textbox(self):
        return self.driver.find_element(*ConfirmPage.country_textbox)

    def get_selected_country(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def get_agree_checkbox(self):
        return self.driver.find_element(*ConfirmPage.agree_checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_message(self):
        return self.driver.find_element(*ConfirmPage.message)
