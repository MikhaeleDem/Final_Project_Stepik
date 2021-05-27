from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):     # Указываем, что это класс-наследник от BasePage
    def go_to_login_page(self):  # Проверяем кликабельность
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)  # *MainPageLocators.LOGIN_LINK указываем, что селектор для теста находится в locators
        login_link.click()