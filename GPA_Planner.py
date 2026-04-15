import streamlit as st
st.logo("fairfield_logo.png", size="large")
st.set_page_config(page_title="GPA Planner")
st.title("GPA Planner Performance Analyzer")

st.write("Enter your courses below to calculate your current GPA and plan for your target.")

# Input Section 
st.header("Your Courses")

num_courses = st.number_input("How many courses are you taking?", min_value=1, max_value=10, value=3, step=1)

grade_points = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
                "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0}

courses = []
for i in range(int(num_courses)):
    st.subheader(f"Course {i + 1}")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input(f"Course Name", key=f"name_{i}", placeholder="e.g. Finance 101")
    with col2:
        grade = st.selectbox(f"Grade", options=list(grade_points.keys()), key=f"grade_{i}")
    with col3:
        credits = st.number_input(f"Credit Hours", min_value=1, max_value=6, value=3, key=f"credits_{i}")
    courses.append({"name": name, "grade": grade, "credits": credits})

# GPA Calculation 
total_points = sum(grade_points[c["grade"]] * c["credits"] for c in courses)
total_credits = sum(c["credits"] for c in courses)
current_gpa = total_points / total_credits if total_credits > 0 else 0.0

st.header("Your Results")
st.metric(label="Current GPA", value=f"{current_gpa:.2f}")

# Slider tool
st.header("Target GPA Planner")
target_gpa = st.slider("Set your target GPA", min_value=0.0, max_value=4.0, value=3.5, step=0.1)

additional_credits = st.number_input("How many additional credit hours are you planning to take?", min_value=1, max_value=200, value=15)

needed_points = (target_gpa * (total_credits + additional_credits)) - total_points
needed_gpa = needed_points / additional_credits if additional_credits > 0 else 0.0

if needed_gpa > 4.0:
    st.warning(f"A {target_gpa} GPA is not achievable in {additional_credits} credit hours from your current standing. Try adding more credits or adjusting your target.")
elif needed_gpa < 0:
    st.success(f"You've already exceeded a {target_gpa} GPA!")
else:
    st.success(f"To reach a {target_gpa} GPA, you need an average GPA of **{needed_gpa:.2f}** over your next {additional_credits} credit hours.")