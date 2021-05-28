
from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):     # Указываем, что это класс-наследник от BasePage
    """Нажимаем Добавить в корзину"""
    def add_product(self):
        button_add_product = self.browser.find_element(*MainPageLocators.ADD_PRODUCT)  #
        button_add_product.click()

    """Нажимаем Перейти в корзину"""
    def go_basket(self):
        button_basket = self.browser.find_element(*MainPageLocators.GO_BASKET)
        button_basket.click()

    """Сравниваем названия купленной и покупаемой книг"""

    def book_name_add_and_in_basket(self):
        name_book_add = self.browser.find_element(*MainPageLocators.BOOK_NAME_ADD)
        name_book_add_text = name_book_add.text
        name_book_in_basket = self.browser.find_element(*MainPageLocators.BOOK_MESSAGE)
        name_book_in_basket_text = name_book_in_basket.text
        assert name_book_add_text == name_book_in_basket_text, f"Книга, добавленная в корзину и та, что добавилась в корзину - разные"
        if name_book_add_text == name_book_in_basket_text:
            print("В корзине правильная книга, с правильным названием")

    """Сравниваем стоимость купленной и покупаемой книг"""

    def book_price_add_and_in_basket(self):
        price_book_add = self.browser.find_element(*MainPageLocators.BOOK_PRICE_ADD)
        price_book_add_text = price_book_add.text
        price_book_in_basket = self.browser.find_element(*MainPageLocators.BOOK_PRICE_BASKET)
        price_book_in_basket_text = price_book_in_basket.text
        assert price_book_add_text == price_book_in_basket_text, f"Стоимость книг добавляемой и добавленной отличаются"
        if price_book_add_text == price_book_in_basket_text:
            print("В корзине правильная книга, с правильной ценой")






