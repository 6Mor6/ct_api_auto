# CT-Lance API Tests

Автотесты для API проекта CT-Lance.

## Стек
- Python 3.12
- pytest
- requests
- allure

## Запуск
```bash
pip install -r requirements.txt
pytest



ct-lance-api-tests/
├── tests/           # сами тесты
├── api/             # API client слой (появится на Шаге 4)
├── data/            # тестовые данные, генераторы
├── utils/           # вспомогательные утилиты
├── conftest.py      # корневые фикстуры (появится на Шаге 3)
├── pytest.ini       # конфиг pytest (Шаг 2)
├── requirements.txt # зависимости
├── .gitignore
└── README.md
