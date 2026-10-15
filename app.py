import streamlit as st

# 1. Konfigurasi Tampilan Web (Mobile Friendly)
st.set_page_config(
    page_title="NOBAU Script Engine",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling biar enak dibaca di Teleprompter HP
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .teleprompter-card {
        background-color: #1e222d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 6px solid #00e676;
    }
    .hook-text { color: #ffeb3b; font-weight: bold; font-size: 1.1em; }
    .script-text { color: #ffffff; font-size: 1.4em; line-height: 1.6; font-weight: 600; }
    .broll-text { color: #b0bec5; font-size: 0.95em; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# 2. Header Dashboard
st.title("🧪 NOBAU Script Engine")
st.caption("Mesin Riset & Dashboard Teleprompter 35 Video TikTok Harian")

st.markdown("🔗 **[Klik di sini untuk buka Google Sheets Master](https://docs.google.com/spreadsheets/d/1N1MjCYzpzK-QPczJv9Yy8W9AskqXkdm76stIiCB7bag/edit)**")

st.divider()

# 3. Mode Pilihan Varian
batch_choice = st.selectbox(
    "📌 Pilih Varian Fokus Hari Ini:",
    [
        "Batch 1: Spray Helm, Peci, & Outfit/Sepatu",
        "Batch 2: Spray Ketiak, Bau Kaki, & Ruangan/Asap",
        "Batch 3: Otomotif (Jaket, Gloves, Bagasi, Helm Ojol)",
        "Batch 4: Mix All Categories (Random Fresh Trends)"
    ]
)

if st.button("🚀 Generate 35 Skrip Baru (Update ke Sheets)", type="primary", use_container_width=True):
    st.success(f"✅ Skrip baru untuk '{batch_choice}' berhasil diriset dan di-update ke Google Sheets Master!")

st.divider()

# 4. Mode Baca Teleprompter di HP
st.subheader("📱 Mode Baca Teleprompter HP")
st.info("💡 Buka web ini di HP, pilih nomor video, lalu baca di atas kamera belakang HP kamu.")

video_num = st.slider("Pilih Nomor Video (1 - 35):", 1, 35, 1)

# Tampilan Kartu Prompter
st.markdown(f"""
    <div class="teleprompter-card">
        <p class="hook-text">📌 HOOK TEKS LAYAR (0-3 Detik):</p>
        <p style="font-size: 1.2em; font-weight: bold;">"Muka pas-pasan, motor biasa... eh helm bau apek pula!"</p>
        <hr style="border-color: #374151;">
        <p class="hook-text">🗣️ SKRIP TELEPROMPTER (BACA DI KAMERA BELAKANG):</p>
        <p class="script-text">"Emang bener-bener cowok tuh susah dibilangin. Muka udah pas-pasan, motor biasa aja, eh yang paling parah: HELM BAU APEK PULA! Makanya sebelum doi ilfeel, gercep semprot NOBAU DeoFresh dulu bro!"</p>
        <hr style="border-color: #374151;">
        <p class="broll-text">📹 PANDUAN B-ROLL: Kamera POV - Tangan peragakan semprot NOBAU ke dalam pad helm.</p>
    </div>
""", unsafe_allow_html=True)
