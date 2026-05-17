import streamlit as st

# Setup Halaman
st.set_page_config(
    page_title="Sistem Master Trading News",
    page_icon="📈",
    layout="centered"
)

# Injeksi Custom CSS untuk mengubah tampilan standar Streamlit
st.markdown("""
    <style>
    .main-header { font-size: 32px !important; font-weight: bold; color: #1a237e; text-align: center; line-height: 1.3; }
    .sub-header { font-size: 18px !important; text-align: center; margin-bottom: 30px; color: #555; }
    .text-red { color: #d32f2f; font-weight: bold; }
    .problem-box { background-color: #ffebee; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .benefit-box { background-color: #f8fbff; border: 2px solid #e3f2fd; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .offer-box { background-color: #fafafa; border: 3px dashed #ccc; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .price-strike { text-decoration: line-through; color: #757575; font-size: 20px; }
    .price-special { color: #d32f2f; font-size: 36px; font-weight: bold; }
    .guarantee-box { background-color: #fff8e1; border: 2px solid #ffc107; padding: 20px; border-radius: 8px; text-align: center; }
    
    /* Modifikasi Tombol Bawaan Streamlit */
    div.stButton > button:first-child {
        background-color: #2e7d32;
        color: white;
        font-size: 22px;
        font-weight: bold;
        padding: 15px 24px;
        border-radius: 50px;
        width: 100%;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #1b5e20;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p class="main-header">Kuasai "Ledakan" Pasar dan Ubah Berita Ekonomi Menjadi Mesin Profit Anda!</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Cara Cerdas Profit Konsisten Meskipun Anda Pemula, Tanpa Harus Seharian di Depan Monitor.</p>', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# --- GUARANTEE SECTION ---
st.markdown('<div class="guarantee-box">', unsafe_allow_html=True)
st.markdown("### 🛡️ Garansi 7 Hari Tanpa Risiko!")
st.write("Kami sangat yakin materi ini bermanfaat. Jika dalam 7 hari Anda merasa e-book ini tidak berguna, kami kembalikan uang Anda 100%. **Tanpa tanya.**")
st.markdown('</div>', unsafe_allow_html=True)

# --- CALL TO ACTION ---
st.write("") # Spacer
if st.button("YA, SAYA MAU CUAN DARI BERITA SEKARANG!"):
    # Anda bisa arahkan ini ke link checkout Sejoli / order online lainnya menggunakan st.link_button jika di Streamlit versi terbaru
    # st.link_button("YA, SAYA MAU CUAN DARI BERITA SEKARANG!", "https://link-checkout-anda.com")
    st.success("Mengarahkan ke halaman pembayaran...")
