# QA Тест для GitHub API

## Запуск
- Установить python 3.12
- Создать виртуальное окружение для проекта командой `python3 -m venv .venv`
- Запустить виртуальное окружение:
  - Для unix систем `source .venv/bin/activate`
- Скачать зависимости `pip install -r requirements.txt`
- В файле .env поставить свои значения:
   - `MY_KEY` - ставим ключ, который сгенирируем в github
   - `NAME_REPOSITORY` - ставим название репозитория
   - `NAME_OWNER` - ставим свой ник в github
- Запустить тест `pytest test_api.py`
