# Aturan proyek untuk AI coding agent

Proyek pelatihan Machine Learning untuk operasi PLTP. Penggunanya sebagian besar **belum pernah
memprogram**, jadi kejelasan lebih penting daripada kecanggihan.

## Data
- Data mentah ada di `data/` dan **TIDAK BOLEH diubah, ditimpa, atau dihapus**.
- Simpan semua hasil olahan ke `data/olahan/`.
- Arti setiap kolom dan rentang wajarnya ada di `data/kamus_data.md` — baca sebelum menganalisis.
- Data gambar: `data/dokumen/` (30 formulir scan + `kunci_dokumen.csv`) dan `data/citra_termal/`
  (160 PNG + `label.csv`). Baca gambar dengan Pillow/matplotlib; jangan mengubah atau
  memindahkan file aslinya.
- `kode_unit` di `produksi_bulanan.csv` punya salah ketik huruf besar-kecil; ada 1 baris
  duplikat dan 12 nilai kosong di `energi_aktual_mwh`. **Jangan memperbaikinya diam-diam** —
  tunjukkan dulu ke pengguna dan minta keputusan.

## Kode
- Python dengan pandas, matplotlib, scikit-learn, dan Streamlit. Jangan menambah library lain
  tanpa bertanya.
- Notebook ada di `notebook/` dan membaca data lewat path relatif `../data/...`.
  Aplikasi Streamlit ada di `app/` dan membaca data relatif terhadap lokasi file aplikasi.
- Skrip `.py` (pekerjaan yang dijalankan berulang) ada di `skrip/`, membaca data lewat
  `Path(__file__).resolve().parent.parent / "data"`, menaruh bagian utama di
  `if __name__ == "__main__":`, mencetak jumlah baris, dan memakai `assert` untuk hasil penting.
- Satu sel notebook = satu langkah. Beri komentar singkat **dalam bahasa Indonesia**.
- Setiap langkah yang mengubah jumlah baris (`merge`, `dropna`, `drop_duplicates`, filter)
  harus mencetak jumlah baris sebelum dan sesudah.
- Untuk model ML: selalu buat **baseline** sederhana, pisahkan train–test sebelum
  pra-pemrosesan, dan laporkan metrik pada data test.

## Grafik
- Setiap grafik matplotlib memakai `gaya_grafik.py` di akar proyek: panggil `gg.terapkan()` sekali,
  warnai unit dengan `gg.warna_unit(...)` (warna tetap per unit), lalu `gg.rapikan(ax, judul, x, y)`.
  Dari `notebook/` atau `skrip/`: `import sys; sys.path.insert(0, "..")` lalu `import gaya_grafik as gg`.
- Label sumbu menyertakan satuan, mis. `CF (%)`, `Energi (MWh)`. Grafik batang mulai dari 0.
- Grafik yang dipakai di laporan atau dashboard disimpan dengan `gg.simpan(fig, "nama")` ke `gambar/`.

## Model dan hasil
- Model terlatih disimpan ke `model/` dengan `joblib.dump` (nama file menyebut tugas dan model,
  mis. `model/p2_random_forest.joblib`), bersama daftar feature dan metrik test-nya.
- Setelah menyimpan, muat ulang model dan `assert` prediksinya sama dengan model di memori.
- Aplikasi Streamlit **memuat** model dari `model/` (`@st.cache_resource`), tidak melatih ulang.
- Data berwaktu dipisah train–test **berdasarkan tanggal**, bukan acak. Laporkan baseline
  dan model dalam satu tabel.

## Cara bekerja
- Sebelum menulis kode untuk tugas yang lebih dari satu langkah, jelaskan **rencana** dulu.
- Setelah menjalankan kode, jelaskan hasilnya dalam 2–3 kalimat bahasa Indonesia, termasuk
  hal yang mungkin keliru atau perlu diperiksa pengguna.
- Bila memperbaiki error, jelaskan penyebabnya. Jangan "memperbaiki" dengan membuang data.

## Catatan kerja (agar bisa pindah alat)
- Peserta bisa berganti editor atau agent kapan saja (kuota habis, jaringan terblokir). Riwayat
  chat **tidak ikut pindah** — yang ikut hanya file di folder ini.
- Saat mulai bekerja, baca `docs/catatan-kerja.md` bila ada isinya, lalu lanjutkan dari
  "Langkah berikutnya".
- Setelah menyelesaikan satu tugas, perbarui `docs/catatan-kerja.md`: tujuan, yang sudah selesai,
  file yang dibuat/diubah, keputusan pengguna, langkah berikutnya, dan masalah terbuka. Singkat.
- Simpan aturan proyek hanya di file ini (`AGENTS.md`), bukan di pengaturan khusus satu editor.
