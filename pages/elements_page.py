from locators.elements_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Ivan Ivanov')
        self.element_is_visible(self.locators.EMAIL).send_keys('mail@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Moscow')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Munich')
        self.element_is_visible(self.locators.SUBMIT).click()


