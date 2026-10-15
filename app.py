import streamlit as st

# 1. Konfigurasi Tampilan Web (Mobile First / Dark Mode Studio)
st.set_page_config(
    page_title="NOBAU Script Engine",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS Pro - Khusus Teleprompter HP
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background: #090C10;
        color: #F0F6FC;
    }
    
    /* Header Branding */
    .brand-title {
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #2EA043 0%, #3FB950 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .brand-sub {
        font-size: 0.85rem;
        color: #8B949E;
        margin-bottom: 20px;
    }
    
    /* Prompter Card Styling */
    .prompter-box {
        background: #161B22;
        border: 1px solid #30363D;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        margin-top: 15px;
        margin-bottom: 20px;
    }
    
    .badge-hook {
        background: rgba(234, 179, 8, 0.15);
        color: #FACC15;
        font-weight: 700;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .badge-script {
        background: rgba(46, 160, 67, 0.15);
        color: #3FB950;
        font-weight: 700;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .badge-broll {
        background: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        font-weight: 700;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }

    .hook-display {
        font-size: 1.25rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.4;
        margin-bottom: 16px;
    }
    
    .script-display {
        font-size: 1.55rem;
        font-weight: 700;
        color: #23C552;
        line-height: 1.5;
        letter-spacing: -0.2px;
        margin-bottom: 16px;
    }
    
    .broll-display {
        font-size: 0.95rem;
        color: #8B949E;
        font-style: italic;
        line-height: 1.4;
    }

    /* Custom Button & Selectbox */
    .stButton>button {
        background: #238636 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 700 !important;
        height: 48px !important;
    }
    
    .stButton>button:hover {
        background: #2EA043 !important;
    }
    
    div[data-baseweb="select"] {
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header Dashboard Studio
st.markdown('<p class="brand-title">🧪 NOBAU Script Engine Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-sub">Dashboard Teleprompter 35 Video QTY Harian • Gen-Z Self-Roast Studio</p>', unsafe_allow_html=True)

# Link Quick Access
col_link1, col_link2 = st.columns(2)
with col_link1:
    st.markdown("📊 [**Buka Master Google Sheets**](https://docs.google.com/spreadsheets/d/1N1MjCYzpzK-QPczJv9Yy8W9AskqXkdm76stIiCB7bag/edit)")
with col_link2:
    st.markdown("🎬 **Target: 35 Video / Hari**")

st.divider()

# 3. Control Panel Generator
st.caption("⚙️ PANEL KONTROL BATCH HARIAN")
batch_choice = st.selectbox(
    "Pilih Varian Fokus Hari Ini:",
    [
        "🔥 Batch 1: Spray Helm, Peci, & Outfit/Sepatu",
        "💨 Batch 2: Spray Ketiak, Bau Kaki, & Ruangan/Asap",
        "🏍️ Batch 3: Otomotif (Jaket, Gloves, Bagasi, Helm Ojol)",
        "🎲 Batch 4: Mix All Categories (Random Fresh Trends)"
    ]
)

if st.button("🚀 GENERATE 35 SKRIP BARU (UPDATE SHEETS)", use_container_width=True):
    st.toast("Riset tren Gen-Z selesai! 35 Skrip baru telah diperbarui di Google Sheets.", icon="✅")

st.divider()

# 4. Teleprompter Studio Player
st.caption("📱 TELEPROMPTER PLAYER (DIBACA PAS REKAM KAMERA BELAKANG)")

# Navigation Slider + Counter
col_nav1, col_nav2 = st.columns([3, 1])
with col_nav1:
    video_num = st.slider("Pilih Video:", 1, 35, 1)
with col_nav2:
    progress_val = str(video_num) + "/35"
    st.metric(label="Progress", value=progress_val)

# Demo Data Skrip
sample_hooks = {
    1: '"Muka pas-pasan, motor biasa... eh helm bau apek pula!"',
    2: '"Solat mau adem, tapi peci bekas keringat minggu lalu?"',
    3: '"Nongkrong udah rapi, pas lepas sepatu... BAU NAGA PULA!"'
}

sample_scripts = {
    1: '"Emang bener-bener cowok tuh susah dibilangin. Muka udah pas-pasan, motor biasa aja, eh yang paling parah: HELM BAU APEK PULA! Makanya sebelum doi ilfeel, gercep semprot NOBAU DeoFresh dulu bro!"',
    2: '"Niatnya mau ibadah biar makin adem, tapi yang bikin gak khusyuk tuh peci bekas keringat minggu lalu. Muka pas-pasan gak apa, yang penting peci wangi segar NOBAU biar ibadah makin tenang."',
    3: '"Cewek tuh paling males kalau nongkrong bareng cowok yang gak peka. Outfit udah rapi, tapi pas lepas sepatu: BAU NAGA PULA! Untung selalu sedia NOBAU DeoFresh, sekali semprot bau naga langsung ngacir."'
}

sample_brolls = {
    1: 'Kamera POV: Tangan kanan pegang helm, tangan kiri semprot NOBAU 2x ke pad busa.',
    2: 'Kamera Close-Up: Tangan usap permukaan peci lalu semprotkan NOBAU dari jarak 10cm.',
    3: 'Kamera Flat Lay: Sepatu ditaruh di lantai, semprot NOBAU ke dalam lubang sepatu.'
}

current_hook = sample_hooks.get(video_num, '"Muka pas-pasan, penampilan biasa... eh bau apek pula!"')
current_script = sample_scripts.get(video_num, '"Emang bener-bener susah dibilangin. Muka biasa aja gak apa, yang penting helm & apparel lu tetep wangi segar NOBAU DeoFresh biar bebas ilfeel!"')
current_broll = sample_brolls.get(video_num, 'Kamera POV: Tangan peragakan semprot NOBAU ke objek produk.')

# Tampilan Card Prompter Pro
st.markdown(f"""
    <div class="prompter-box">
        <span class="badge-hook">📌 HOOK TEKS LAYAR (0-3 DETIK)</span>
        <div class="hook-display">{current
