# ФИО: Быковский Андрей Максимович
# Дата: 15.11.2026
# Время: 19:00
#
# Описание изменений:
# Добавил обработчик нажатия кнопки, который меняет её текст.
# После нажатия программа проверяет, что новый текст появился
# на странице.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.set_content("""
        <button onclick="this.textContent = 'Signed in'">
            Sign in
        </button>
    """)

    page.get_by_role("button", name="Sign in").click()

    assert page.get_by_text("Signed in").is_visible()

    print("Проверка пройдена! Кнопка изменила текст.")

    browser.close()

# Что изменилось и зачем?
# Добавил обработчик onclick, который меняет надпись на кнопке после нажатия.
# Добавил assert, чтобы проверить, что текст действительно изменился.
# Изменил сообщение о результате проверки.
# Зачем: теперь программа не просто нажимает кнопку, но и проверяет результат взаимодействия с ней.

# Результат выполнения

# Команда: python examples/day_3_modified.py

# Ожидаемый результат: Проверка пройдена! Кнопка изменила текст.

# Результат: screenshots/day_3_modifed_terminal.png