import streamlit as st
st.logo("fairfield_logo.png", size="large")

st.set_page_config(page_title="Course Breakdown", layout="centered")

st.title("Course Breakdown & Stats")
st.write(
    "Tag each course by type — Finance, Core, Elective, etc. — "
    "then see a stats breakdown of how you're performing across categories."
)

st.divider()

# ── Setup ─────────────────────────────────────────────────────────────────────
grade_points = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0
}

course_types = ["FNCE", "Core", "Elective", "Major", "Gen Ed", "Other"]

# ── Course Input ──────────────────────────────────────────────────────────────
st.header("Your Courses")

num_courses = st.number_input("How many courses?", min_value=1, max_value=10, value=3, step=1)

courses = []
for i in range(int(num_courses)):
    st.subheader(f"Course {i + 1}")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        name = st.text_input("Course Name", key=f"name_{i}", placeholder="e.g. Finance 101")
    with col2:
        grade = st.selectbox("Grade", options=list(grade_points.keys()), key=f"grade_{i}")
    with col3:
        credits = st.number_input("Credits", min_value=1, max_value=6, value=3, key=f"credits_{i}")
    with col4:
        ctype = st.selectbox("Type", options=course_types, key=f"type_{i}")
    courses.append({
        "name": name or f"Course {i+1}",
        "grade": grade,
        "credits": credits,
        "type": ctype
    })

st.divider()

# ── Overall Stats ─────────────────────────────────────────────────────────────
st.header("Overall Stats")

total_points = sum(grade_points[c["grade"]] * c["credits"] for c in courses)
total_credits = sum(c["credits"] for c in courses)
overall_gpa = total_points / total_credits if total_credits > 0 else 0.0

col1, col2, col3 = st.columns(3)
col1.metric("Overall GPA", f"{overall_gpa:.2f}")
col2.metric("Total Credits", total_credits)
col3.metric("Total Courses", len(courses))

st.divider()

# ── Breakdown by Course Type ──────────────────────────────────────────────────
st.header("GPA by Course Type")
st.write("Your GPA broken down by each course category.")

types_present = list(set(c["type"] for c in courses))

for ctype in sorted(types_present):
    type_courses = [c for c in courses if c["type"] == ctype]
    type_points = sum(grade_points[c["grade"]] * c["credits"] for c in type_courses)
    type_credits = sum(c["credits"] for c in type_courses)
    type_gpa = type_points / type_credits if type_credits > 0 else 0.0

    with st.expander(f"{ctype} — GPA: {type_gpa:.2f} ({len(type_courses)} course{'s' if len(type_courses) > 1 else ''}, {type_credits} credits)"):
        st.markdown("| Course | Grade | Credits | Quality Points |")
        st.markdown("|--------|-------|---------|----------------|")
        for c in type_courses:
            qp = grade_points[c["grade"]] * c["credits"]
            st.markdown(f"| {c['name']} | {c['grade']} | {c['credits']} | {qp:.1f} |")

st.divider()

# ── Best & Worst ──────────────────────────────────────────────────────────────
st.header("Performance Highlights")

sorted_courses = sorted(courses, key=lambda c: grade_points[c["grade"]], reverse=True)
best = sorted_courses[0]
worst = sorted_courses[-1]

col_b, col_w = st.columns(2)
with col_b:
    st.success(f"**Best:** {best['name']} — {best['grade']} ({grade_points[best['grade']]:.1f} pts)")
with col_w:
    if grade_points[worst["grade"]] < grade_points[best["grade"]]:
        st.warning(f"**Needs Work:** {worst['name']} — {worst['grade']} ({grade_points[worst['grade']]:.1f} pts)")
    else:
        st.success("All courses at the same grade level — consistent!")

st.divider()
st.caption("GPA Planner & Performance Analyzer · Fairfield University")
