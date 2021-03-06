# Это базовая страница, с которой начинаем работу с сайтом. Тут описываются вспомогательные методы для работы с драйвером
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import \
    NoSuchElementException  # Импортировали исключение(сообщение об ошибке) при получении которого получаем ошибку
import math


class BasePage():
    # Конструктор объявляется ключевым словом __init__.
    # В него в мы передаем экземпляр драйвера и url адрес.Внутри конструктора сохраняем эти данные как аттрибуты класса
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # Метод открывает нужную страницу в браузере, используя метод get().
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how,
                           what):  # Прописали, что при получении "Такого" исключения выдавать ошибку см. main_page
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
