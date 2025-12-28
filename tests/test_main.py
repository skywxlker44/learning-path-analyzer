import pandas as pd
from src.main import load_logs, summarize_student_activity, recommend_improvements

def test_load_logs():
    df = load_logs("data/sample.csv")
    assert not df.empty
    assert 'student_id' in df.columns

def test_summarize_student_activity():
    df = pd.DataFrame({
        'student_id': [1,1,2],
        'activity_type': ['quiz_attempt', 'assignment_submission', 'quiz_attempt']
    })
    summary = summarize_student_activity(df)
    assert summary.loc[1,'quiz_attempt'] == 1
    assert summary.loc[1,'assignment_submission'] == 1
    assert summary.loc[2,'quiz_attempt'] == 1

def test_recommend_improvements():
    summary = pd.DataFrame({
        'student_id': [1,2],
        'quiz_attempt': [1,5],
        'assignment_submission': [2,3],
        'forum_post': [0,3]
    }).set_index('student_id')
    recommendations = recommend_improvements(summary)
    assert 1 in recommendations
    assert 'Попробовать больше квизов' in recommendations[1]
    assert 'Активнее участвовать в форуме' in recommendations[1]
    assert 'Сдавать все задания' in recommendations[1]
    assert 2 in recommendations  # теперь 2 будет в defaultdict с пустым списком
