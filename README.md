## :green_book: Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы заказа бургеров в Stellar Burgers

### :computer: Использованный стек технологий

* Pytest
* Unittest

### :pushpin: Реализованные сценарии

Созданы юнит-тесты, покрывающие классы: `Bun`, `Ingredient`, `Burger`, `Database`.

Процент покрытия 100% (отчет: `htmlcov/index.html`).

### :books: Структура проекта

- `Diplom_1` - проект, содержащий код программы.
- `tests` - пакет, содержащий тесты, разделенные по классам: `test_bun.py`, `test_ingredient.py`, `test_burger.py`
  , `test_database.py`.

### :running: Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов из корня проекта `Diplom_1` и создание HTML-отчета о покрытии**

> `$ pytest --cov --cov-report=html`
