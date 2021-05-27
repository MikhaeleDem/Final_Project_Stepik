from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Общий селектор для тестов ссылки страницы логина


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # Общий селектор для тестов с формой заполнения логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Общий селектор для тестов с формой регистрации