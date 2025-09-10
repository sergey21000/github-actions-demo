

# Github Actions Demo

Знакомство с GitHub Actions на примере следующих Workflow: 
- Workflow для автоматизации тестирования Python кода, проверки кода на безопасность и на соответствие PEP8, проверки аннотитаций типов (`code-check.yml`)
- Workflow для демонстрации базовой работы с переменными (`variables-demo.yml`)


**Стек технологий**  
- [pytest](https://github.com/pytest-dev/pytest) для тестирования
- [mypy](https://github.com/python/mypy) для проверки типов
- [flake8](https://github.com/pycqa/flake8) для проверки PEP8
- [bandit](https://github.com/PyCQA/bandit) для проверки безопасности кода


**Структура проекта**
```yaml
github-actions-demo/
│
├── .github/
│   └── workflows/                  # автоматизация GitHub Actions
│       ├── code-check.yml          # CI: проверка стиля, типов и тестов
│       └── variables-demo.yml      # демо: переменные, матрицы, ОС
│
├── src/                            # исходный код
│   └── calculator.py               # калькулятор с аннотацией типов
│
├── tests/                          # тесты
│   │── __init__.py                 # чтобы tests был модулем и видел другие модули
│   │── conftest.py                 # хранилище фикстур
│   └── test_calculator.py          # модульные тесты (pytest)
│
└── requirements.txt                # зависимости: flake8, pytest, mypy, bandit
└── README.md                       # описание проекта и инструкции по запуску
```


# Локальный запуск

**1) Клонирование репозитория**  

```shell
git clone https://github.com/sergey21000/github-actions-demo.git
cd github-actions-demo
```

**2) Создание и активация виртуального окружения (опционально)**

- *Linux*
  ```shell
  python3 -m venv env
  source env/bin/activate
  ```

- *Windows CMD*
  ```shell
  python -m venv env
  env\Scripts\activate
  ```

- *Windows PowerShell*
  ```powershell
  python -m venv env
  env\Scripts\activate.ps1
  ```

**3) Установка зависимостей**  

```shell
pip install -r requirements.txt
```

**4) Запуск**  

<ins>Запуск тестов</ins>
```shell
pytest -v
```

<ins>Запуск проверки типов</ins>
```shell
mypy src/ --ignore-missing-imports
```

<ins>Запуск проверки PEP8</ins>
```shell
flake8 src/ --show-source
```

<ins>Запуск проверки безопасности кода</ins>
```shell
bandit -r src/
```
После проверки можно скачать отчеты bandit (в разделе `Artifacts` из Workflow run)


# Запуск через Github Actions

Workflow для тестирования, проверки типов и PEP8 (`code-check.yml`) запсукается автоматически при пуше (отправке кода в репозиторий) или вручую  
Workflow для демонстрации работы с переменными окружения запускается вручную

---
**Запуск Workflow:**
- Создать свой репозиторий на GitHub или форкунть (скопировать себе) текущий (`Fork` -> `Create Fork`)
- Перейти в `Actions` 
- слева нажать на нужный Workflow и справа нажать `Run workflow`, при условии что в `yml` настроен на ручной запуск (в нем прописано условие `on: workflow_dispatch
`)  

Если же в `yml` файле прописано например `on: push: branches: main`, то он будет запускаться автоматически при пуше (отправке изменений в репозиторий) в ветку main  
Для проверки кода нужно добавить новый Python файл в папку `src/` или отредактировать текущий и закоммитить изменения

Для загрузки результатов запуска Workflow (артефактов) перейти в `Actions` -> выбрать нужный run -> внизу будет раздел `Artifacts` и значок загрузки архива (при условии что сохранение артефактов прописано в `yml` файле и он отработал успешно)

---
**Создание нового Workflow:**
- Перейти в `Actions`
- создать новый Workflow, нажав на `set up a workflow yourself` если это первый Workflow иначе `New workflow` -> `set up a workflow yourself`
- написать новое название `yml` файлу (опционально) например `code-check.yml`, затем записать в него содержимое Workflow
- нажать `Commit Changes` -> подтвердить `Commit Changes`

Или просто создать вручную файл на странице репозитория -> `Add file` -> `Create new file` -> `.github/workflows/code-check.yml` -> записать содержимое и закоммитить  
При загрузке файлов с локальной машины можно перейти в папку `.github/workflows/` и нажать `Add file` -> `Upload files`, или вообще апользоваться git

