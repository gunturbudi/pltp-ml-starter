# -*- coding: utf-8 -*-
"""
gaya_grafik.py — satu gaya untuk semua grafik matplotlib di proyek ini.

Pakai di notebook (folder notebook/):

    import sys; sys.path.insert(0, "..")
    import gaya_grafik as gg
    gg.terapkan()

    fig, ax = plt.subplots()
    ax.bar(tabel.index, tabel["cf_persen"], color=gg.warna_unit(tabel.index))
    gg.rapikan(ax, judul="CF rata-rata per unit", x="Unit", y="CF (%)")
    gg.simpan(fig, "cf_per_unit")        # → gambar/cf_per_unit.png

Di skrip (skrip/) dan aplikasi (app/) caranya sama; `sys.path.insert` cukup
menunjuk ke folder induk proyek.

Aturan yang dibawa templat ini:
- setiap unit punya warna tetap (ARL selalu biru, BTL selalu oranye, ...), jadi
  warna tidak berubah ketika unit difilter;
- grid tipis, tanpa bingkai atas/kanan, sumbu y batang mulai dari 0;
- judul, label sumbu, dan satuan wajib diisi lewat `rapikan()`;
- gambar disimpan ke `gambar/` dengan resolusi yang sama untuk semua orang.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

AKAR = Path(__file__).resolve().parent
FOLDER_GAMBAR = AKAR / "gambar"

# Enam warna kategori (sudah diuji aman untuk buta warna). Urutannya tetap.
WARNA = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]
WARNA_UNIT = dict(zip(["ARL", "BTL", "CKR", "DRG", "EKL", "FRS"], WARNA))
ABU = "#8a8f98"      # untuk "lainnya", baseline, atau data pembanding
TINTA = "#1f2933"    # teks dan angka
TINTA_REDUP = "#5b6470"


def terapkan():
    """Pasang gaya proyek untuk semua grafik berikutnya. Panggil sekali di awal."""
    mpl.rcParams.update({
        "figure.figsize": (9, 4.8),
        "figure.dpi": 110,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.prop_cycle": mpl.cycler(color=WARNA),
        "axes.edgecolor": "#c8ccd2",
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.axisbelow": True,
        "grid.color": "#e6e8eb",
        "grid.linewidth": 0.8,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlecolor": TINTA,
        "axes.labelsize": 11,
        "axes.labelcolor": TINTA_REDUP,
        "xtick.color": TINTA_REDUP,
        "ytick.color": TINTA_REDUP,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "lines.linewidth": 2,
        "lines.markersize": 6,
        "legend.frameon": False,
        "legend.fontsize": 10,
        "font.size": 11,
        "savefig.dpi": 150,
        "savefig.bbox": "tight",
    })


def warna_unit(kode):
    """Warna tetap untuk satu kode unit, atau daftar warna untuk banyak kode."""
    if isinstance(kode, str):
        return WARNA_UNIT.get(kode.upper(), ABU)
    return [WARNA_UNIT.get(str(k).upper(), ABU) for k in kode]


def rapikan(ax, judul, x, y, sumber="Data simulasi PLTP Nusantara", nol=True):
    """Judul, label sumbu (sertakan satuan, mis. "CF (%)"), dan catatan sumber.

    nol=True memaksa sumbu y mulai dari 0 — wajib untuk grafik batang.
    """
    ax.set_title(judul)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if nol:
        bawah, atas = ax.get_ylim()
        ax.set_ylim(min(0, bawah), atas)
    ax.figure.text(0.01, -0.02, sumber, fontsize=9, color=TINTA_REDUP, ha="left", va="top")
    return ax


def label_batang(ax, fmt="{:.1f}"):
    """Tulis nilai di atas setiap batang (pengganti warna sebagai satu-satunya petunjuk)."""
    for wadah in ax.containers:
        ax.bar_label(wadah, fmt=fmt, padding=3, fontsize=9, color=TINTA)
    return ax


def simpan(fig, nama):
    """Simpan ke gambar/<nama>.png dan kembalikan path-nya."""
    FOLDER_GAMBAR.mkdir(exist_ok=True)
    path = FOLDER_GAMBAR / f"{nama}.png"
    fig.savefig(path)
    print("Tersimpan:", path.relative_to(AKAR))
    return path


if __name__ == "__main__":
    # Uji cepat: python gaya_grafik.py  → gambar/uji_gaya.png
    import pandas as pd

    df = pd.read_csv(AKAR / "data" / "produksi_bulanan.csv")
    df["kode_unit"] = df["kode_unit"].str.upper()
    df = df.drop_duplicates()
    cf = df.groupby("kode_unit")["cf_persen"].mean().sort_values()
    assert len(cf) == 6, f"harus 6 unit, dapat {len(cf)}"

    terapkan()
    fig, ax = plt.subplots()
    ax.bar(cf.index, cf.values, color=warna_unit(cf.index))
    rapikan(ax, judul="CF rata-rata per unit, 2011–2025", x="Unit", y="CF (%)")
    label_batang(ax)
    simpan(fig, "uji_gaya")
