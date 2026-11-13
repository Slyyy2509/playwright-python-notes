# ФИО: Быковский Андрей Максимович
# Дата: 2026-11-12
# Время: 17:22
# Описание: Этот пример взят из документации Playwright
# он запускает браузер Chromium, открывает сайт playwright.dev,
# получает заголовок страницы и выводит его в консоль
# после выполнения браузер закрывается

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    browser.close()