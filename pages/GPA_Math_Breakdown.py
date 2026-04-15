import streamlit as st
st.logo("fairfield_logo.png", size="large")

st.set_page_config(page_title="How GPA Works", layout="centered")

st.title("How GPA is Calculated")
st.write("A quick breakdown of how your GPA is computed and what each grade is worth.")

st.divider()

# ── Grade Scale Table ─────────────────────────────────────────────────────────
st.header("Grade Point Scale")
st.write("Each letter grade maps to a numeric value called a **grade point**.")

grade_points = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0
}

col1, col2 = st.columns(2)
with col1:
    st.markdown("| Grade | Points |")
    st.markdown("|-------|--------|")
    for grade, pts in list(grade_points.items())[:5]:
        st.markdown(f"| {grade} | {pts} |")

with col2:
    st.markdown("| Grade | Points |")
    st.markdown("|-------|--------|")
    for grade, pts in list(grade_points.items())[5:]:
        st.markdown(f"| {grade} | {pts} |")

st.divider()

# ── Formula Explanation ───────────────────────────────────────────────────────
st.header("The Formula")
st.write("GPA is a **weighted average** based on credit hours, not a simple average of grades.")

st.markdown("""
**Step 1 — Quality Points per course:**
> Quality Points = Grade Points × Credit Hours

**Step 2 — Total Quality Points:**
> Add up quality points across all courses

**Step 3 — GPA:**
> GPA = Total Quality Points ÷ Total Credit Hours
""")

st.divider()

# ── Worked Example ────────────────────────────────────────────────────────────
st.header("Worked Example")
st.write("Say you're taking these three courses this semester:")

example = [
    {"Course": "Finance 101", "Grade": "A",  "Credits": 3, "Points": 4.0},
    {"Course": "Statistics",  "Grade": "B+", "Credits": 4, "Points": 3.3},
    {"Course": "English",     "Grade": "B-", "Credits": 3, "Points": 2.7},
]

st.markdown("| Course | Grade | Credits | Grade Points | Quality Points |")
st.markdown("|--------|-------|---------|--------------|----------------|")
total_qp = 0
total_cr = 0
for row in example:
    qp = row["Points"] * row["Credits"]
    total_qp += qp
    total_cr += row["Credits"]
    st.markdown(f"| {row['Course']} | {row['Grade']} | {row['Credits']} | {row['Points']} | {qp:.1f} |")

st.markdown(f"| **Total** | | **{total_cr}** | | **{total_qp:.1f}** |")

gpa = total_qp / total_cr
st.success(f"**GPA = {total_qp:.1f} ÷ {total_cr} = {gpa:.2f}**")

st.divider()

# ── Why Credits Matter ────────────────────────────────────────────────────────
st.header("Why Credit Hours Matter")
st.write(
    "A 4-credit course has more weight than a 3-credit course. "
    "That means an A in a 4-credit class boosts your GPA more than an A in a 3-credit class — "
    "and an F in a 4-credit class hurts more too."
)

st.info("Tip: Prioritize grade performance in your highest-credit courses. They move the needle most.")

st.divider()
st.caption("GPA Planner & Performance Analyzer · Fairfield University")
