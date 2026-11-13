# -*- coding: utf-8 -*-
"""
cek_lingkungan.py — memeriksa apakah laptop siap untuk pelatihan.

    python cek_lingkungan.py

Semua baris harus ✅. TensorFlow boleh ❌ sampai Hari 4.
"""
import importlib
import sys
from pathlib import Path

AKAR = Path(__file__).resolve().parent
hasil = []


def cek(nama, lulus, ket=""):
    hasil.append(lulus)
    tanda = "✅" if lulus else "❌"
    print(f"{tanda}  {nama:<28} {ket}")


try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

print("Pemeriksaan lingkungan — Pelatihan ML Operasi PLTP\n")

v = sys.version_info
cek("Python >= 3.10", v >= (3, 10), f"versi {v.major}.{v.minor}.{v.micro}")

for lib in ["pandas", "numpy", "matplotlib", "sklearn", "statsmodels", "streamlit"]:
    try:
        m = importlib.import_module(lib)
        cek(lib, True, getattr(m, "__version__", ""))
    except Exception as e:
        cek(lib, False, f"belum terpasang -> pip install -r requirements.txt  ({type(e).__name__})")

try:
    import pandas as pd
    df = pd.read_csv(AKAR / "data" / "produksi_bulanan.csv")
    cek("data/produksi_bulanan.csv", len(df) == 1081, f"{len(df)} baris (harus 1081)")
except Exception as e:
    cek("data/produksi_bulanan.csv", False, f"tidak terbaca ({type(e).__name__})")

wajib = all(hasil)

try:
    import tensorflow as tf
    print(f"✅  {'tensorflow (Hari 4)':<28} {tf.__version__}")
except Exception:
    print(f"⚠️  {'tensorflow (Hari 4)':<28} belum ada — boleh, pasang sebelum Hari 4")

print("\nLULUS — siap dipakai." if wajib else "\nBELUM LULUS — tunjukkan layar ini ke asisten.")
