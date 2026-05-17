import streamlit as st

# Setup Halaman
st.set_page_config(
    page_title="Sistem Master Trading News",
    page_icon="📈",
    layout="centered"
)

# Injeksi Custom CSS 
st.markdown("""
    <style>
    .main-header { font-size: 34px !important; font-weight: 800; color: #1a237e; line-height: 1.2; margin-bottom: 15px;}
    .sub-header { font-size: 18px !important; margin-bottom: 20px; color: #424242; line-height: 1.5;}
    .text-red { color: #d32f2f; font-weight: bold; }
    .problem-box { background-color: #ffebee; padding: 25px; border-radius: 10px; margin-top: 20px; margin-bottom: 30px; border-left: 6px solid #c62828;}
    .benefit-box { background-color: #f8fbff; border: 1px solid #bbdefb; padding: 25px; border-radius: 10px; margin-bottom: 30px; }
    .offer-box { background-color: #ffffff; border: 2px dashed #9e9e9e; padding: 25px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);}
    .price-strike { text-decoration: line-through; color: #757575; font-size: 20px; }
    .price-special { color: #d32f2f; font-size: 42px; font-weight: 900; }
    .guarantee-box { background-color: #fff8e1; border: 2px solid #ffb300; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 30px;}
    
    /* Tombol WA Custom HTML */
    .btn-wa {
        display: block;
        background-color: #25D366;
        color: white !important;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 20px;
        border-radius: 50px;
        text-decoration: none;
        box-shadow: 0 4px 10px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
        margin: 10px 0 20px 0;
        animation: pulse 1.5s infinite;
    }
    .btn-wa:hover {
        background-color: #128C7E;
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(18, 140, 126, 0.5);
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION DENGAN GAMBAR ---
# Membagi layar jadi 2 kolom: Kiri (teks) rasio 1.2, Kanan (gambar) rasio 1.0
col1, col2 = st.columns([1.2, 1]) 

with col1:
    st.markdown('<div class="main-header">Kuasai "Ledakan" Pasar & Ubah Berita Menjadi Mesin Profit!</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Cara cerdas profit konsisten meskipun pemula, tanpa harus seharian pantau layar monitor.</div>', unsafe_allow_html=True)
    
    # GANTI NOMOR WA DI BAWAH INI (Pastikan pakai format 628... tanpa spasi/tanda plus)
    wa_link = "https://wa.me/6282293274916?text=Halo%20Admin,%20saya%20mau%20pesan%20Paket%20Master%20Trading%20News%20promo%20Rp149.000"
    st.markdown(f'<a href="{wa_link}" class="btn-wa" target="_blank">YA, SAYA MAU CUAN DARI BERITA SEKARANG!</a>', unsafe_allow_html=True)

with col2:
    # Menggunakan gambar ilustrasi profesional dari Unsplash
    st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80", use_column_width=True)

st.divider()

# --- PROBLEM SECTION ---
st.markdown('<div class="problem-box">', unsafe_allow_html=True)
st.subheader("Apakah Anda Mengalami Ini?")
st.markdown("""
- ❌ **Bingung** kenapa harga tiba-tiba bergerak liar tanpa sebab?
- ❌ **Sudah pasang indikator banyak** tapi tetap saja kena pergerakan palsu?
- ❌ **Ingin trading** tapi tidak punya waktu karena sibuk kerja?
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- SOLUTION & BENEFITS SECTION ---
st.markdown('<h3>Memperkenalkan: <span class="text-red">Sistem Master Trading News</span></h3>', unsafe_allow_html=True)
st.write("Bukan sekadar menebak, tapi memahami **psikologi pasar** saat berita besar rilis. Kami tidak menggunakan indikator yang membingungkan, kami menggunakan data nyata yang menggerakkan ekonomi dunia.")

st.markdown('<div class="benefit-box">', unsafe_allow_html=True)
st.markdown("""
- ✅ **Step-by-Step:** Panduan dari nol cara baca kalender ekonomi.
- ✅ **Anti-Gaptek:** Tanpa software rumit, cukup pakai browser dan aplikasi trading biasa.
- ✅ **Efisiensi Waktu:** Hanya trading saat berita penting (kurang dari 30 menit sehari).
- ✅ **Psikologi Tenang:** Tahu kapan harus masuk dan kapan harus menjauh dari pasar.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- OFFER STACK SECTION ---
st.markdown('<div class="offer-box">', unsafe_allow_html=True)
st.subheader("Dapatkan Paket Lengkap Master Trading News:")
st.markdown("""
- 📘 **E-book Utama** (Value Rp499.000)
- 🎁 **Bonus 1: Cheat Sheet Berita High Impact** (Value Rp150.000)
- 🎁 **Bonus 2: Template Kalkulator Lot Aman** (Value Rp100.000)
- 🎁 **Bonus 3: Akses Komunitas Telegram VIP** (Value Rp250.000)
""")
st.markdown('<p style="text-align:center;">Total Nilai: <span class="price-strike">Rp999.000</span></p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">Harga Spesial Hari Ini:<br><span class="price-special">Rp149.000</span></p>', unsafe_allow_html=True)

# TOMBOL WA KEDUA DI BAGIAN HARGA
st.markdown(f'<a href="{wa_link}" class="btn-wa" target="_blank">AMBIL HARGA PROMO SEKARANG!</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- GUARANTEE SECTION ---
st.markdown('<div class="guarantee-box">', unsafe_allow_html=True)
st.markdown("### 🛡️ Garansi 7 Hari Tanpa Risiko!")
st.write("Kami sangat yakin materi ini bermanfaat. Jika dalam 7 hari Anda merasa e-book ini tidak berguna, kami kembalikan uang Anda 100%. **Tanpa tanya.**")
st.markdown('</div>', unsafe_allow_html=True)
