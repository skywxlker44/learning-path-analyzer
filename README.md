````markdown
# Learning Path Analyzer

## Описание
Learning Path Analyzer — это инструмент для анализа учебной активности студентов на основе логов LMS (например, Moodle или Canvas).  
Он подсчитывает типы активностей студентов, генерирует рекомендации и визуализирует прогресс в виде графиков.

---

## Возможности
- Загрузка логов в формате CSV
- Подсчет активности студентов по типам:
  - Квизы (`quiz_attempt`)
  - Задания (`assignment_submission`)
  - Форумы (`forum_post`)
- Генерация рекомендаций для улучшения учебного процесса
- Визуализация активности с помощью графиков

---

## Установка

### Требования
- Python 3.8+
- pip

### Шаги установки
```bash
git clone https://github.com/skywxlker44/learning-path-analyzer.git
cd learning-path-analyzer
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
# source venv/bin/activate
pip install -r requirements.txt
````

---

## Использование

### Пример загрузки данных и анализа

```python
from src.main import load_logs, summarize_student_activity, recommend_improvements, plot_activity_summary

# Загрузить логи
df = load_logs("data/sample.csv")

# Суммировать активность студентов
summary = summarize_student_activity(df)

# Получить рекомендации
recommendations = recommend_improvements(summary)
print(recommendations)

# Построить график активности
plot_activity_summary(summary)
```

---

## Структура проекта

```
.
├── src/                 # Исходный код
│   ├── __init__.py
│   └── main.py
├── tests/               # Unit тесты
│   ├── __init__.py
│   └── test_main.py
├── data/                # Примеры CSV файлов
│   └── sample.csv
├── docs/                # Документация (опционально)
├── scripts/             # Вспомогательные скрипты (опционально)
├── .github/workflows/   # CI/CD
├── README.md
└── requirements.txt
```

---

## Тестирование

Запуск тестов с покрытием:

```bash
pytest tests/ -v --cov=src
```

---

## CI/CD

* Проверка кода с помощью `flake8` и `black`
* Автоматический запуск тестов через GitHub Actions
* Workflow для генерации отчета активности студентов (сохранение в artifact)

---

## Автор

Быков Дмитрий РИ-150931
