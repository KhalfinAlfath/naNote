import streamlit as st
from datetime import date

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(
    page_title="NanoLab Data Recorder",
    page_icon="🧬",
    layout="wide"
)

# =====================
# STYLE TAMBAHAN
# =====================
st.markdown("""
<style>
.hero {
    padding: 2.5rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #99f6e4, #ecfeff);
}
.box {
    padding: 1rem;
    border-radius: 14px;
    background-color: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================
st.markdown("""
<div class="hero">
<h1>🧪 NanoLab Data Recorder</h1>
<p><b>Buku Catatan Digital Praktikum Nanoteknologi Pangan</b></p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================
# SESSION STATE
# =====================
if "data" not in st.session_state:
    st.session_state.data = []

# =====================
# FORM INPUT
# =====================
st.subheader("📋 Input Data Praktikum")

with st.form("form_nano"):
    c1, c2, c3 = st.columns(3)

    with c1:
        nama_sampel = st.text_input("Nama Sampel", "Nanoemulsi Minyak Ikan")
        metode = st.selectbox(
            "Metode Preparasi",
            ["Nanoemulsi", "Enkapsulasi", "Spray Drying", "Liposom", "Lainnya"]
        )

    with c2:
        ukuran = st.number_input("Ukuran Partikel (nm)", 0.0, 1000.0, 150.0)
        pdi = st.number_input("Polydispersity Index (PDI)", 0.0, 1.0, 0.25)

    with c3:
        ph = st.number_input("pH Sampel", 0.0, 14.0, 6.8)
        tanggal = st.date_input("Tanggal Pengujian", value=date.today())

    catatan = st.text_area(
        "Catatan Visual dan Stabilitas",
        "Warna putih susu homogen, tidak terjadi creaming setelah 24 jam."
    )

    simpan = st.form_submit_button("💾 Simpan Data")

# =====================
# PROSES SIMPAN
# =====================
if simpan:
    st.session_state.data.append({
        "Nama Sampel": nama_sampel,
        "Metode": metode,
        "Ukuran (nm)": ukuran,
        "PDI": pdi,
        "pH": ph,
        "Tanggal": tanggal,
        "Catatan Visual": catatan
    })

    st.success("✅ Data praktikum berhasil disimpan.")

# =====================
# TAMPILKAN DATA
# =====================
if st.session_state.data:
    st.subheader("📊 Riwayat Data Praktikum")
    st.dataframe(st.session_state.data, use_container_width=True)

# =====================
# INTERPRETASI SINGKAT
# =====================
st.subheader("🔍 Panduan Interpretasi Singkat")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<div class='box'><b>Ukuran Partikel</b><br>&lt; 200 nm menunjukkan sistem nano yang relatif stabil</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='box'><b>PDI</b><br>&lt; 0,3 menandakan distribusi ukuran partikel homogen</div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='box'><b>pH</b><br>pH ekstrem dapat memicu ketidakstabilan sistem</div>", unsafe_allow_html=True)

st.divider()
st.caption("NanoLab Data Recorder • Praktikum Nanoteknologi Pangan")
