import streamlit as st
st.logo("fairfield_logo.png", size="large")

st.set_page_config(page_title="Finals Calculator", layout="centered")

st.title("Finals Grade Calculator")
st.write(
    "Enter your current grade in a course and how much the final exam is worth. "
    "We'll tell you exactly what score you need on the final to hit your target grade."
)

st.divider()

# ── Input ─────────────────────────────────────────────────────────────────────
st.header("Course Details")

col1, col2 = st.columns(2)
with col1:
    course_name = st.text_input("Course Name", placeholder="e.g. Finance 101")
with col2:
    final_weight = st.slider("Final Exam Weight (%)", min_value=5, max_value=70, value=30, step=5)

current_grade = st.number_input(
    "Your current grade before the final (%)",
    min_value=0.0, max_value=100.0, value=85.0, step=0.5
)

target_grade = st.number_input(
    "Target final course grade (%)",
    min_value=0.0, max_value=100.0, value=90.0, step=0.5
)

st.divider()

# ── Calculation ───────────────────────────────────────────────────────────────
# current_grade is worth (100 - final_weight)% of the total
# target = current_grade * (1 - final_weight/100) + final_score * (final_weight/100)
# solve for final_score

current_weight = 1 - (final_weight / 100)
needed_final = (target_grade - (current_grade * current_weight)) / (final_weight / 100)

st.header("Your Results")

label = course_name if course_name else "this course"

col_r1, col_r2, col_r3 = st.columns(3)
col_r1.metric("Current Grade", f"{current_grade:.1f}%")
col_r2.metric("Final Weight", f"{final_weight}%")
col_r3.metric("Target Grade", f"{target_grade:.1f}%")

st.write("")

if needed_final > 100:
    st.error(
        f"❌ You need a **{needed_final:.1f}%** on the final to reach **{target_grade:.0f}%** in {label} — "
        f"which isn't possible. Consider adjusting your target."
    )
elif needed_final < 0:
    st.success(
        f"✅ You've already locked in a **{target_grade:.0f}%** in {label} — "
        f"even a 0 on the final won't drop you below your target!"
    )
else:
    if needed_final >= 90:
        st.warning(f"⚠️ You need a **{needed_final:.1f}%** on the final to reach **{target_grade:.0f}%** in {label}. That's a high bar — start studying.")
    elif needed_final >= 70:
        st.info(f"📘 You need a **{needed_final:.1f}%** on the final to reach **{target_grade:.0f}%** in {label}. Doable with solid prep.")
    else:
        st.success(f"✅ You only need a **{needed_final:.1f}%** on the final to reach **{target_grade:.0f}%** in {label}. You're in good shape.")

st.divider()

# ── What-if Table ─────────────────────────────────────────────────────────────
st.header("What-If Final Scores")
st.write("See what course grade you'd end up with for different final exam scores.")

st.markdown("| Final Score | Resulting Course Grade |")
st.markdown("|-------------|------------------------|")

for score in [50, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
    result = (current_grade * current_weight) + (score * (final_weight / 100))
    st.markdown(f"| {score}% | {result:.1f}% |")

st.divider()
st.caption("GPA Planner & Performance Analyzer · Fairfield University")
