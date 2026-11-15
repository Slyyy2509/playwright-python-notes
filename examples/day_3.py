# ФИО: Быковский Андрей Максимович
# Дата: 15.11.2026
# Время: 19:00
# Описание:
# программа создаёт тестовую HTML-страницу с кнопкой Sign in.
# С помощью get_by_role находит кнопку по её роли и названию,
# затем нажимает на неё.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.set_content('<button>Sign in</button>')

    page.get_by_role("button", name="Sign in").click()

    print("Кнопка найдена и нажата!")

    browser.close()

# Что изменено и зачем
# Команда page.set_content() создаёт HTML-содержимое страницы. Мы добавляем кнопку, чтобы было с чем работать.
# Команда page.get_by_role() Ищет элемент по его роли и доступному имени.
# - button — тип элемента (кнопка).
# - name="Sign in" — название кнопки.
# .click() — Нажимает на найденный элемент. Playwright перед нажатием проверяет, что элемент доступен для взаимодействия.

# Результат выполнения

# Команда: python examples/day_3.py

# Результат: screenshots/day_3_terminal.png