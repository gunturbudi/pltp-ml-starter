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

# Data gambar: formulir scan dan citra termal
try:
    from PIL import Image
    cek("Pillow (baca gambar)", True, Image.__version__ if hasattr(Image, "__version__") else "")
except Exception as e:
    cek("Pillow (baca gambar)", False, f"belum terpasang -> pip install pillow  ({type(e).__name__})")

dok = AKAR / "data" / "dokumen"
n_dok = len([f for f in dok.glob("LG-*") if f.suffix.lower() in (".png", ".jpg")]) if dok.exists() else 0
cek("data/dokumen/", n_dok == 30 and (dok / "kunci_dokumen.csv").exists(),
    f"{n_dok} formulir (harus 30) + kunci_dokumen.csv")

citra = AKAR / "data" / "citra_termal"
try:
    import pandas as pd
    import numpy as np
    from PIL import Image
    label = pd.read_csv(citra / "label.csv")
    n_png = len(list(citra.glob("T*.png")))
    ukuran = np.asarray(Image.open(citra / label["file"].iloc[0])).shape
    cek("data/citra_termal/", n_png == 160 and len(label) == 160 and ukuran == (120, 160, 3),
        f"{n_png} gambar, label {len(label)} baris, ukuran {ukuran} (harus 160 · 160 · (120, 160, 3))")
except Exception as e:
    cek("data/citra_termal/", False, f"tidak terbaca ({type(e).__name__}) -> git pull, atau salin ulang folder data")

wajib = all(hasil)

try:
    import tensorflow as tf
    print(f"✅  {'tensorflow (Hari 4)':<28} {tf.__version__}")
except Exception:
    print(f"⚠️  {'tensorflow (Hari 4)':<28} belum ada — boleh, pasang sebelum Hari 4")

print("\nLULUS — siap dipakai." if wajib else "\nBELUM LULUS — tunjukkan layar ini ke asisten.")
