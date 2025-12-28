import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def load_logs(csv_path):
    """
    Загружает логи студентов из CSV.
    Ожидаемые колонки: student_id, timestamp, activity_type
    """
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    return df


def summarize_student_activity(df):
    """
    Создает сводную таблицу по активности студентов.
    Если нет колонки 'timestamp', просто считаем количество записей по типу активности.
    """
    if 'timestamp' in df.columns:
        values_col = 'timestamp'
    else:
        # Создаем временную колонку с единицами для подсчета
        df['count'] = 1
        values_col = 'count'

    summary = df.pivot_table(
        index='student_id',
        columns='activity_type',
        values=values_col,
        aggfunc='count' if values_col == 'timestamp' else 'sum',
        fill_value=0
    )

    return summary


def recommend_improvements(summary):
    """
    Генерирует рекомендации для студентов на основе их активности
    """
    recommendations = defaultdict(list)

    for student_id in summary.index:
        row = summary.loc[student_id]
        if row.get('quiz_attempt', 0) < 3:
            recommendations[student_id].append('Попробовать больше квизов')
        if row.get('assignment_submission', 0) < 3:
            recommendations[student_id].append('Сдавать все задания')
        if row.get('forum_post', 0) < 2:
            recommendations[student_id].append('Активнее участвовать в форуме')

        # Убедимся, что у каждого студента есть ключ, даже если нет рекомендаций
        if student_id not in recommendations:
            recommendations[student_id] = []

    return recommendations


def plot_activity_summary(summary, output_path="reports/activity_summary.png"):
    """
    Строит график активности студентов и сохраняет его
    """
    summary.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Активность студентов")
    plt.xlabel("student_id")
    plt.ylabel("Количество действий")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    df = load_logs("data/sample.csv")
    summary = summarize_student_activity(df)
    recommendations = recommend_improvements(summary)
    print("Рекомендации для студентов:")
    for student, recs in recommendations.items():
        print(f"Студент {student}: {', '.join(recs) if recs else 'Нет рекомендаций'}")
    plot_activity_summary(summary)
