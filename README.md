# PLTP ML Starter — Machine Learning dengan AI Coding Agent

Starter kit peserta **Pelatihan Machine Learning untuk Operasi PLTP** (16–20 November 2026).
Berisi data simulasi, aturan untuk AI coding agent, pemeriksa lingkungan, notebook cadangan,
dan dashboard Streamlit pertama Anda.

> ### ⚠️ Data simulasi
> Seluruh data di repositori ini **fiktif**, dibangkitkan untuk pelatihan. Bukan data
> operasional PT Pertamina Geothermal Energy dan tidak boleh dipakai untuk keputusan nyata.
> Karena fiktif, data ini **aman dikirim ke AI cloud**. Data operasional nyata **tidak**.

---

## 1. Unduh

**Tanpa Git:** tombol hijau **Code → Download ZIP**, lalu ekstrak ke `Documents/`.

**Dengan Git:**

```bash
git clone https://github.com/gunturbudi/pltp-ml-starter.git
```

## 2. Pasang

1. **Python** lewat [Anaconda](https://www.anaconda.com/download) (atau Miniconda).
2. Satu library tambahan — buka *Anaconda Prompt* di folder ini:
   ```bash
   pip install -r requirements.txt
   ```
3. **Satu AI coding tool** (pilih satu, boleh keduanya):

   | Alat | Akun | Catatan |
   |---|---|---|
   | **Antigravity** (Google) — alat utama | akun Google | gratis, kuota mingguan |
   | **VS Code + GitHub Copilot Free** — alternatif | akun GitHub | gratis, kuota bulanan terbatas |

4. Periksa semuanya:
   ```bash
   python cek_lingkungan.py
   ```
   Semua baris harus ✅ (TensorFlow boleh ❌ sampai Hari 4).

## 3. Dashboard pertama Anda (quick win)

```bash
streamlit run app/app_mulai.py
```

Browser terbuka di `http://localhost:8501`. Lalu minta AI agent mengubahnya, misalnya:

> *Tambahkan grafik jumlah forced outage per unit dari `data/gangguan.csv` ke `app/app_mulai.py`.*

## 4. Isi folder

| Folder / file | Isi |
|---|---|
| `data/` | 6 CSV simulasi PLTP Nusantara + `kamus_data.md` (**baca ini dulu**) |
| `data/olahan/` | tempat menyimpan hasil olahan Anda — file mentah di `data/` **jangan diubah** |
| `notebook/` | notebook *rekaman prompt* Hari 1–2 (Rencana C, lihat bawah) |
| `app/app_mulai.py` | dashboard Streamlit pertama, titik awal capstone |
| `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `.github/copilot-instructions.md` | aturan proyek yang otomatis dibaca AI agent |
| `prompt-log.md` | templat catatan prompt — diisi sepanjang pelatihan |
| `docs/rencana-koneksi.md` | apa yang dilakukan bila AI cloud terblokir |
| `cek_lingkungan.py` | pemeriksa instalasi |

## 5. Bila AI cloud tidak bisa diakses

Jaringan tempat pelatihan bisa memblokir layanan AI. Urutan cadangan:

- **Rencana A** — VPN atau hotspot HP, lalu pakai Antigravity / Copilot seperti biasa.
- **Rencana B** — AI lokal perusahaan (Qwen) lewat VS Code + ekstensi *Continue*.
- **Rencana C** — buka `notebook/ai-rekaman-hari*.ipynb`: prompt + kode hasil AI sudah tersedia.
  Baca, tebak hasilnya, jalankan, periksa.

Detail langkahnya ada di [`docs/rencana-koneksi.md`](docs/rencana-koneksi.md).

## 6. Studi kasus

PT Energi Panas Nusantara (fiktif) — 6 unit PLTP, Januari 2011 – Desember 2025.

| # | Pertanyaan | Jenis tugas ML |
|---|---|---|
| P1 | Bulan mana yang cocok untuk jendela pemeliharaan? | Clustering |
| P2 | Unit mana yang berisiko forced outage bulan depan? | Klasifikasi |
| P3 | Berapa harga wajar diusulkan, dan produksi yang bisa dijanjikan? | Regresi + time-series |

Hasil akhir Hari 5: **model ML yang dikemas sebagai dashboard Streamlit** — upload/pilih data,
eksplorasi, prediksi atau cluster, dan metrik evaluasi dengan baseline.
