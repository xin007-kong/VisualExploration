import streamlit as st
from collections import defaultdict

# 模拟数据
courses = ["Math", "History", "Biology",
           "Computer Science", "Art", "Physical Education"]

ratings = {
    "Alice": {"Math": 5, "History": 4, "Biology": 4},
    "Bob": {"Math": 4, "Computer Science": 5, "Physical Education": 3},
    "Charlie": {"History": 3, "Art": 5, "Physical Education": 4},
}


def similarity(student1, student2):
    common_courses = set(ratings[student1].keys()) & set(
        ratings[student2].keys())
    if not common_courses:
        return 0
    diff = sum([(ratings[student1][course] - ratings[student2]
               [course])**2 for course in common_courses])
    return 1 / (1 + diff)


def recommend_for_student(student_name):
    scores = defaultdict(float)
    for other_student in ratings:
        if other_student == student_name:
            continue
        sim = similarity(student_name, other_student)
        for course, rating in ratings[other_student].items():
            if course not in ratings[student_name]:
                scores[course] += sim * rating

    recommended_courses = sorted(scores, key=scores.get, reverse=True)[:3]
    return recommended_courses


# Streamlit UI
st.title("Campus Course Recommender")

student_name = st.selectbox("Select a student:", list(ratings.keys()))
recommended_courses = recommend_for_student(student_name)

st.write(f"Recommended courses for {student_name}:")
for course in recommended_courses:
    st.write(course)
