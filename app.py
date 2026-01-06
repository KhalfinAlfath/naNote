import streamlit as st
from datetime import date

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="NanoLab",
    page_icon="🧬",
    layout="wide"
)

# =====================
# HEADER HERO
# =====================
st.markdown("""
<style>
.hero {
    padding: 2.5rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #99f6e4, #ecfeff);
}
.metric-box {
    padding: 1rem;
    border-radius: 14px;
    background-color: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🧬 NanoLab Data Recorder</h1>
<p><b>Digital Research Notebook</b> for Food Nanotechnology Practicum</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================
# FORM SECTION
# =====================
st.subheader("🧪 Experimental Data Input")

with st.form("nano_form"):
    c1, c2, c3 = st.columns(3)

    with c1:
        sample = st.text_input("Sample Name", "Nanoemulsion Fish Oil")
        method = st.selectbox("Preparation Method", [
            "Nanoemulsion",
            "Encapsulation",
            "Spray Drying",
            "Liposomal System",
            "Other"
        ])

    with c2:
        size = st.number_input("Particle Size (nm)", 0.0, 1000.0, 150.0)
        pdi = st.number_input("PDI", 0.0, 1.0, 0.25)

    with c3:
        ph = st.number_input("pH", 0.0, 14.0, 6.8)
        test_date = st.date_input("Test Date", value=date.today())

    visual = st.text_area(
        "Visual Observation & Stability Notes",
        "Homogeneous milky appearance, no phase separation after 24 hours."
    )

    submit = st.form_submit_button("Save Experimental Record")

if submit:
    st.success("Experimental data recorded successfully (demo mode).")

# =====================
# QUICK INTERPRETATION
# =====================
st.subheader("🔎 Quick Research Insight")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<div class='metric-box'><b>Particle Size</b><br><200 nm indicates nano-scale stability</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='metric-box'><b>PDI</b><br><0.3 suggests uniform distribution</div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-box'><b>pH</b><br>Extreme pH may reduce stability</div>", unsafe_allow_html=True)

st.divider()
st.caption("NanoLab Data Recorder • Academic Prototype")
