from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, "button[value='Добавить в корзину']") # Добавить товар в корзину
    GO_BASKET = (By.CSS_SELECTOR, "[class=icon-shopping-cart]") # Корзина

    BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")  # Добавленная книга
    BOOK_NAME_ADD = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")   # Добавляемая книга

    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")  # Добавленная книга
    BOOK_PRICE_ADD = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")  # Добавляемая книга


