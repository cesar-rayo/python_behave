from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    CONTACT_LINK = (By.ID, 'contact-link')

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.driver.get("http://automationpractice.com/")

    def click_contact(self):
        contact_link = self.driver.find_element(*self.CONTACT_LINK)
        contact_link.click()
        return self.driver
