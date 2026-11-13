# -*- coding: utf-8 -*-
"""
Dashboard pertama — titik awal capstone.

    streamlit run app/app_mulai.py

Kembangkan file ini bersama AI agent: tambah grafik, model, dan metrik evaluasi.
"""
from pathlib import Path

import pandas as pd
import streamlit as st

DATA = Path(__file__).resolve().parent.parent / "data"

st.set_page_config(page_title="Dashboard PLTP Nusantara", layout="wide")
st.title("Dashboard PLTP Nusantara")
st.caption("Data simulasi untuk pelatihan — bukan data operasional nyata.")


@st.cache_data
def muat(file):
    df = pd.read_csv(file)
    df["kode_unit"] = df["kode_unit"].str.upper()   # seragamkan salah ketik huruf kecil
    df = df.drop_duplicates()                       # buang 1 baris ganda
    df["tanggal"] = pd.to_datetime(df["tanggal"])
    return df


# ① Data: upload sendiri, atau pakai data contoh
with st.sidebar:
    st.header("① Data")
    upload = st.file_uploader("Upload CSV produksi", type="csv")
    df = muat(upload if upload is not None else DATA / "produksi_bulanan.csv")
    units = st.multiselect("Unit", sorted(df["kode_unit"].unique()), default=sorted(df["kode_unit"].unique()))
    th0, th1 = int(df["tahun"].min()), int(df["tahun"].max())
    tahun = st.slider("Tahun", th0, th1, (th0, th1))

pilih = df[df["kode_unit"].isin(units) & df["tahun"].between(*tahun)]

# Ringkasan
k1, k2, k3 = st.columns(3)
k1.metric("CF rata-rata", f"{pilih['cf_persen'].mean():.1f} %")
k2.metric("Energi aktual", f"{pilih['energi_aktual_mwh'].sum() / 1000:,.0f} GWh")
k3.metric("Jumlah baris", f"{len(pilih):,}")

# ② Eksplorasi
st.subheader("② Eksplorasi")
tren = pilih.pivot_table(index="tanggal", columns="kode_unit", values="cf_persen")
st.line_chart(tren, y_label="CF (%)")

# ③ Prediksi / cluster — diisi mulai Hari 2–4
st.subheader("③ Prediksi / cluster")
st.info("Belum ada model. Minta AI agent menambahkan hasil clustering (P1) atau prediksi gangguan (P2) di sini.")

# ④ Evaluasi model — wajib untuk capstone
st.subheader("④ Evaluasi model")
st.info("Tampilkan metrik model dan baseline di sini.")

with st.expander("Lihat data"):
    st.dataframe(pilih, width="stretch")
