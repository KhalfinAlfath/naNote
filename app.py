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
# STYLE KUSTOM
# =====================
st.markdown("""
<style>
.hero {
    padding: 2.5rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #99f6e4, #ecfeff);
}
.card {
    padding: 1.2rem;
    border-radius: 16px;
    background-color: #ffffff;
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# =====================
# HERO SECTION
# =====================
st.markdown("""
<div class="hero">
<h1>🧬 NanoLab Data Recorder</h1>
<p><b>Buku Catatan Digital Praktikum Nanoteknologi Pangan</b></p>
<p>Mengubah pencatatan manual praktikum nano menjadi sistem digital yang rapi, konsisten, dan terdokumentasi.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================
# FORM INPUT DATA
# =====================
st.subheader("🧪 Pencatatan Data Praktikum")

with st.form("form_praktikum"):
    col1, col2, col3 = st.columns(3)

    with col1:
        nama_sampel = st.text_input(
            "Nama Sampel",
            placeholder="Contoh: Nanoemulsi Minyak Ikan"
        )
        metode = st.selectbox(
            "Metode Preparasi",
            ["Nanoemulsi", "Enkapsulasi", "Spray Drying", "Liposom", "Lainnya"]
        )

    with col2:
        ukuran = st.number_input(
            "Ukuran Partikel (nm)",
            min_value=0.0,
            placeholder="Contoh: 150"
        )
        pdi = st.number_input(
            "Polydispersity Index (PDI)",
            min_value=0.0,
            max_value=1.0,
            step=0.01
        )

    with col3:
        ph = st.number_input(
            "pH Sampel",
            min_value=0.0,
            max_value=14.0,
            step=0.1
        )
        tanggal = st.date_input(
            "Tanggal Pengujian",
            value=date.today()
        )

    catatan_visual = st.text_area(
        "Catatan Visual & Stabilitas",
        placeholder=(
            "Contoh:\n"
            "- Warna putih susu homogen\n"
            "- Tidak terjadi creaming setelah 24 jam\n"
            "- Tidak ada pemisahan fase"
        )
    )

    st.form_submit_button("💾 Simpan Data")

# =====================
# INSIGHT ILMIAH
# =====================
st.subheader("🔍 Insight Singkat Nanoteknologi")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <b>Ukuran Partikel</b><br>
    Ukuran < 200 nm menunjukkan sistem berada pada skala nano dan berpotensi lebih stabil.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <b>PDI</b><br>
    Nilai PDI < 0,3 menandakan distribusi ukuran partikel yang relatif homogen.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <b>pH Sistem</b><br>
    Perubahan pH dapat memengaruhi muatan permukaan dan kestabilan sistem nano.
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("NanoLab Data Recorder • Praktikum Nanoteknologi Pangan")
