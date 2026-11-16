# -*- coding: utf-8 -*-
"""Eksplorasi awal data produksi bulanan tanpa mengubah file sumber."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

AKAR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(AKAR))
import gaya_grafik as gg

DATA = AKAR / "data" / "produksi_bulanan.csv"
JUMLAH_BARIS_SESUAI_KAMUS = 1081
KODE_UNIT_SESUAI_KAMUS = {"ARL", "BTL", "CKR", "DRG", "EKL", "FRS"}
RENTANG_WAJAR = {
    "uap_rencana_ton": (50_000, 700_000),
    "uap_aktual_ton": (0, 700_000),
    "energi_rencana_mwh": (5_000, 75_000),
    "energi_aktual_mwh": (0, 75_000),
    "jam_operasi": (0, 744),
    "cf_persen": (0, 95),
}


def tampilkan_barisan(data, kondisi, judul, kolom):
    """Tampilkan baris yang cocok dan laporkan perubahan jumlah tampilan."""
    jumlah_awal = len(data)
    hasil = data.loc[kondisi, kolom]
    print(f"\n{judul}")
    print(f"Baris sebelum pemeriksaan: {jumlah_awal}; baris yang ditampilkan: {len(hasil)}")
    if hasil.empty:
        print("Tidak ada.")
    else:
        print(hasil.to_string(index=False))


def main():
    print("Eksplorasi produksi bulanan - data sumber tidak diubah")
    data = pd.read_csv(DATA)
    print(f"\nJumlah baris: {len(data)} (kamus data: {JUMLAH_BARIS_SESUAI_KAMUS})")
    print(f"Jumlah kolom: {len(data.columns)}")
    print(f"Rentang tanggal: {data['tanggal'].min()} sampai {data['tanggal'].max()}")
    assert len(data) == JUMLAH_BARIS_SESUAI_KAMUS, (
        f"Jumlah baris berubah: diharapkan {JUMLAH_BARIS_SESUAI_KAMUS}, "
        f"ditemukan {len(data)}"
    )

    print("\nNama kolom:")
    print(", ".join(data.columns))

    print("\nNilai kosong per kolom:")
    kosong = data.isna().sum()
    print(kosong[kosong.gt(0)].to_string() if kosong.gt(0).any() else "Tidak ada.")

    print("\nJumlah baris per kode_unit persis seperti di file (tanpa koreksi):")
    print(data["kode_unit"].value_counts(dropna=False).sort_index().to_string())

    kode_tidak_dikenal = ~data["kode_unit"].isin(KODE_UNIT_SESUAI_KAMUS)
    tampilkan_barisan(
        data,
        kode_tidak_dikenal,
        "Baris dengan kode_unit yang tidak sama persis dengan kamus:",
        ["tanggal", "kode_unit"],
    )

    duplikat_kunci = data.duplicated(
        subset=["tanggal", "kode_unit"], keep=False
    )
    tampilkan_barisan(
        data,
        duplikat_kunci,
        "Baris dengan pasangan tanggal + kode_unit yang berulang:",
        ["tanggal", "kode_unit"],
    )

    kunci_diagnostik = pd.DataFrame(
        {
            "tanggal": data["tanggal"],
            "kode_unit_diagnostik": data["kode_unit"].str.upper(),
        }
    )
    duplikat_kapitalisasi = kunci_diagnostik.duplicated(keep=False)
    tampilkan_barisan(
        data,
        duplikat_kapitalisasi,
        "Kandidat duplikat jika kapitalisasi kode diseragamkan (diagnostik saja):",
        ["tanggal", "kode_unit"],
    )

    for kolom, (batas_bawah, batas_atas) in RENTANG_WAJAR.items():
        di_luar_rentang = data[kolom].notna() & (
            data[kolom].lt(batas_bawah) | data[kolom].gt(batas_atas)
        )
        tampilkan_barisan(
            data,
            di_luar_rentang,
            f"Nilai {kolom} di luar rentang kamus "
            f"({batas_bawah:,}-{batas_atas:,}):",
            ["tanggal", "kode_unit", kolom],
        )

    print("\nRingkasan menurut kode_unit mentah:")
    per_unit = data.groupby("kode_unit", dropna=False).agg(
        jumlah_baris=("kode_unit", "size"),
        energi_aktual_rata_rata_mwh=("energi_aktual_mwh", "mean"),
        cf_rata_rata_persen=("cf_persen", "mean"),
        cf_minimum_persen=("cf_persen", "min"),
        cf_maksimum_persen=("cf_persen", "max"),
    )
    print(per_unit.round(2).to_string())

    print("\nRingkasan per tahun (energi kosong diabaikan pada penjumlahan):")
    per_tahun = data.groupby("tahun").agg(
        jumlah_baris=("tahun", "size"),
        energi_aktual_mwh=("energi_aktual_mwh", lambda nilai: nilai.sum(min_count=1)),
        cf_rata_rata_persen=("cf_persen", "mean"),
    )
    print(per_tahun.round(2).to_string())

    print("\nRata-rata CF menurut bulan kalender:")
    per_bulan = data.groupby("bulan")["cf_persen"].mean()
    print(per_bulan.round(2).to_string())

    gg.terapkan()

    fig, ax = plt.subplots()
    urutan_unit = per_unit["cf_rata_rata_persen"].sort_values().index
    ax.bar(
        urutan_unit,
        per_unit.loc[urutan_unit, "cf_rata_rata_persen"],
        color=gg.warna_unit(urutan_unit),
    )
    gg.rapikan(
        ax,
        judul="CF rata-rata per kode unit",
        x="Kode unit (seperti di file)",
        y="CF (%)",
    )
    gg.label_batang(ax)
    gg.simpan(fig, "eksplorasi_cf_per_unit")
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.bar(per_tahun.index.astype(str), per_tahun["energi_aktual_mwh"] / 1000)
    gg.rapikan(
        ax,
        judul="Energi aktual tahunan",
        x="Tahun",
        y="Energi aktual (ribu MWh)",
    )
    ax.tick_params(axis="x", rotation=45)
    gg.simpan(fig, "eksplorasi_energi_tahunan")
    plt.close(fig)

    print("\nGrafik disimpan di gambar/. Periksa anomali sebelum melakukan pembersihan.")


if __name__ == "__main__":
    main()
