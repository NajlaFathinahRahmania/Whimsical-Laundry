# Tugas Besar Praktikum Algoritma Dan Pemrograman - Aplikasi Biaya Laundry Kiloan
# Tugasbesar_Najla_D1021261033.py

import time

import streamlit as st

st.set_page_config(page_title="Najelll love ", page_icon="🪷", layout="centered")

# ---------- tampilan (CSS) ----------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat&display=swap');
.hero {
    background: linear-gradient(135deg, #ff8fab, #ffb3c6, #fb6f92);
    padding: 26px 20px;
    border-radius: 20px;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(210, 130, 170, .30);
}

.hero h1 { margin: 0; font-size: 2.3rem; color: white; }
.hero p  { margin: 6px 0 0; opacity: .92; }
.card {
    border-radius: 14px; padding: 14px 16px; margin-bottom: 12px;
    color: #1d1d1d; box-shadow: 0 2px 8px rgba(0,0,0,.08);
}
.card .label { font-size: .82rem; opacity: .75; }
.card .value { font-size: 1.45rem; font-weight: 700; }
.c-pink   { background: #FBF4EB; border-left: 6px solid #C43670; }
.c-blue { background: #CFE3E3; border-left: 6px solid #0B2545; }
.c-purple { background: #E8D9E8; border-left: 6px solid #8a5F8A; }
.c-green { background: #C8E6C9; border-left: 6px solid #245223; }
.c-brown   { background: #FAF7F0; border-left: 6px solid #3B2A20; }
.total {
    background: linear-gradient(135deg, #ffc2d1, #ff8fab);
    border-radius: 18px; padding: 20px; text-align: center;
    color: #FFFFFF; margin-top: 6px;
    box-shadow: 0 6px 18px rgba(67,160,71,.35);
}
.total .label { font-size: 1rem; font-weight: 600; }
.total .value { font-size: 2.2rem; font-weight: 800; }
.footer { text-align: center; opacity: .6; font-size: .8rem; margin-top: 30px; }

/* ---------- halaman pembuka & loading ---------- */
.opening {
    background: linear-gradient(-45deg, #ffffff, #ff8fab, #ffb3c6, #fb6f92);
    background-size: 400% 400%;
    animation: gradasi 8s ease infinite;
    padding: 60px 20px; border-radius: 26px; color: white;
    text-align: center; margin-top: 30px; margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(33,150,243,.45);
}
.opening h1 { font-size: 2.8rem; margin: 10px 0 4px; color: white; }
.opening p  { font-size: 1.05rem; opacity: .95; margin: 4px 0; }
.opening .logo { font-size: 4.5rem; display: inline-block; animation: melayang 2.6s ease-in-out infinite; }
.opening .badge {
    display: inline-block; margin-top: 18px; padding: 6px 16px;
    background: rgba(255,255,255,.2); border-radius: 999px; font-size: .85rem;
}
.loading-box {
    text-align: center; padding: 50px 20px; border-radius: 24px;
    background: linear-gradient(135deg, #fb6f92, #ffb3c6);
    box-shadow: 0 6px 20px rgba(33,150,243,.25); margin-top: 40px;
}
.loading-box .mesin { font-size: 4.5rem; display: inline-block; animation: putar 1.2s linear infinite; }
.loading-box h3 { color: #ffffff; margin: 10px 0 0; }
@keyframes gradasi { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
@keyframes melayang { 0%,100% {transform: translateY(0);} 50% {transform: translateY(-14px);} }
@keyframes putar { from {transform: rotate(0deg);} to {transform: rotate(360deg);} }

/* ---------- font judul Whimsical Laundry ---------- */
.opening h1, .hero h1 {
    font-family: 'Caveat', cursive;
    font-weight: 400;
    letter-spacing: 1px;
}

/* ---------- warna tombol AYO & Hitung (pink) ---------- */
.stButton > button[kind="primary"],
.stButton > button[kind="primaryFormSubmit"],
.stButton > button[data-testid="stBaseButton-primary"],
.stButton > button[data-testid="stBaseButton-primaryFormSubmit"] {
    background: #F48FB1;
    border: none;
    color: white;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #EC6A97;
    color: white;
}

/* ---------- warna kotak info & success (pink) ---------- */
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]),
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]),
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) div[data-baseweb="notification"],
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) div[data-baseweb="notification"],
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) [data-testid="stAlertContainer"],
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) [data-testid="stAlertContainer"],
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) [role="alert"],
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) [role="alert"] {
    background: #FFD6E4 !important;
    background-color: #FFD6E4 !important;
    color: #880E4F;
    border-radius: 12px;
}
div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) *,
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) * {
    color: #880E4F;
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- fungsi ----------
def hitung_laundry(nim, berat):
    digit_terakhir = int(nim[-1])
    digit_genap = sum(1 for d in nim if int(d) % 2 == 0)

    tarif_per_kg = 5000 + (digit_terakhir * 500)
    persen_diskon = digit_genap * 1
    biaya_normal = berat * tarif_per_kg
    potongan = persen_diskon / 100 * biaya_normal
    total_bayar = biaya_normal - potongan

    return {
        "nim": nim,
        "berat": berat,
        "tarif": tarif_per_kg,
        "digit_genap": digit_genap,
        "persen": persen_diskon,
        "normal": biaya_normal,
        "potongan": potongan,
        "total": total_bayar,
    }


def rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")


def kartu(warna, ikon, label, nilai):
    return (
        f'<div class="card {warna}"><div class="label">{ikon} {label}</div>'
        f'<div class="value">{nilai}</div></div>'
    )


# ---------- state ----------
for kunci, awal in {
    "nim": "",
    "berat": 0,
    "hasil": None,
    "error": None,
    "baru": False,
    "riwayat": [],
    "halaman": "opening",
}.items():
    if kunci not in st.session_state:
        st.session_state[kunci] = awal


def proses_hitung():
    nim = st.session_state.nim.strip()
    berat = st.session_state.berat
    st.session_state.hasil = None
    st.session_state.error = None
    st.session_state.baru = False

    # validasi NIM: tepat 10 digit angka
    if len(nim) != 10 or not nim.isdigit():
        st.session_state.error = (
            "Nice try bestie, harus 10 angka dan gak boleh huruf yaa..."
        )
        return

    # validasi berat: bilangan bulat > 0
    if berat <= 0:
        st.session_state.error = "dikit lagi... Berat cucian harus lebih dari 0 :) "
        return

    hasil = hitung_laundry(nim, int(berat))
    st.session_state.hasil = hasil
    st.session_state.baru = True
    st.session_state.riwayat.append(
        {
            "NIM": hasil["nim"],
            "Berat (kg)": hasil["berat"],
            "Diskon": f"{hasil['persen']} %",
            "Total Bayar": rupiah(hasil["total"]),
        }
    )


def proses_reset():
    st.session_state.nim = ""
    st.session_state.berat = 0
    st.session_state.hasil = None
    st.session_state.error = None
    st.session_state.baru = False


# ---------- halaman pembuka ----------
if st.session_state.halaman == "opening":
    st.markdown(
        """
<div class="opening">
    <div class="logo">🪷</div>
    <h1>Whimsical Laundry </h1>
    <p> > Welcome to Whimsical Laundry < </p>
    <p> cuci semua pakaianmu disini  🩰</p>
    <div class="badge">Tugas Besar Praktikum Algoritma</div>
</div>
""",
        unsafe_allow_html=True,
    )
    if st.button("🪄 AYO!!!", type="primary", use_container_width=True):
        st.session_state.halaman = "loading"
        st.rerun()
    st.markdown(
        '<div class="footer">Najla Fathinah Rahmania(1021261033) </div>',
        unsafe_allow_html=True,
    )
    st.stop()

# ---------- halaman loading ----------
if st.session_state.halaman == "loading":
    tempat = st.empty()
    langkah = [
        (15, "Hey Youu..."),
        (40, "I Love You!..."),
        (65, "Do You Love Me?..."),
        (90, "Why No:(..."),
        (100, "Aww I Love You So Much 🥰"),
    ]
    bar = st.progress(0)
    for persen, teks in langkah:
        tempat.markdown(
            f'<div class="loading-box"><div class="mesin">🌀</div><h3>{teks}</h3></div>',
            unsafe_allow_html=True,
        )
        bar.progress(persen, text=f"{persen}%")
        time.sleep(0.7)
    st.session_state.halaman = "app"
    st.rerun()

# ---------- sidebar ----------
with st.sidebar:
    st.header("📘 How to Calculate ")
    st.markdown(
        """
- **Tarif/kg** = Rp 5.000 + (digit terakhir NIM × Rp 500)
- **Diskon** = jumlah digit genap NIM × 1 %
- **Biaya normal** = berat × tarif/kg
- **Potongan** = diskon × biaya normal
- **Total bayar** = biaya normal − potongan
"""
    )
    st.info("Angka 0 jadi digit genap ya...")
    if st.button("🏠 Maw Pulang?", use_container_width=True):
        st.session_state.halaman = "opening"
        st.rerun()

# ---------- tampilan utama ----------
st.markdown(
    """
<div class="hero">
    <h1>🪷 Whimsical Laundry </h1>
    <p>Hitung Laundry Kamu di Sini yaa... Selamat mencuci </p>
</div>
""",
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.text_input("💌 isi NIM kamu (10 digit)", key="nim", placeholder="contoh: 2411001347")
    st.number_input("🧶 Berat Cucian (kg)", step=1, key="berat")

    col1, col2 = st.columns(2)
    col1.button(
        "🧮 Hitung", on_click=proses_hitung, use_container_width=True, type="primary"
    )
    col2.button("🔄 Reset", on_click=proses_reset, use_container_width=True)

if st.session_state.error:
    st.error("⚠️ " + st.session_state.error)

h = st.session_state.hasil
if h:
    if st.session_state.baru:
        st.toast("Perhitungan berhasil!", icon="✅")
        if h["persen"] >= 8:
            st.snow()
        st.session_state.baru = False

    st.subheader("📋 Rincian Perhitungan")

    a, b = st.columns(2)
    a.markdown(
        kartu("c-pink", "🏷️", "Tarif per kg", rupiah(h["tarif"])), unsafe_allow_html=True
    )
    b.markdown(
        kartu("c-purple", "💜", "Persen diskon", f"{h['persen']} %"),
        unsafe_allow_html=True,
    )

    c, d = st.columns(2)
    c.markdown(
        kartu("c-blue", "💵", "Biaya normal", rupiah(h["normal"])),
        unsafe_allow_html=True,
    )
    d.markdown(
        kartu("c-green", "✂️", "Potongan", rupiah(h["potongan"])),
        unsafe_allow_html=True,
    )

    st.markdown(
        kartu(
            "c-brown",
            "🔢",
            "Jumlah digit genap pada NIM",
            f"{h['digit_genap']} dari 10 digit",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="total">
    <div class="label">💰 TOTAL BAYAR</div>
    <div class="value">{rupiah(h['total'])}</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if h["potongan"] > 0:
        st.success(f"🎉 Wah! Kamu hemat {rupiah(h['potongan'])} berkat diskon {h['persen']} %!")
    else:
        st.info("maaf! gak ada diskon cuz NIM kamu ganjil semua.")

# ---------- riwayat ----------
if st.session_state.riwayat:
    with st.expander("🕘 Riwayat perhitungan"):
        st.dataframe(st.session_state.riwayat, use_container_width=True)

st.markdown(
    '<div class="footer">Tugas Besar Praktikum Algoritma • Najla Fathinah Rahmania(D1021261033)</div>',
    unsafe_allow_html=True,
)