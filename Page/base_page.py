# Это базовая страница, с которой начинаем работу с сайтом. Тут описываются вспомогательные методы для работы с драйвером

from selenium.common.exceptions import \
    NoSuchElementException  # Импортировали исключение(сообщение об ошибке) при получении которого получаем ошибку


class BasePage():
    # добавим конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__.
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
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
