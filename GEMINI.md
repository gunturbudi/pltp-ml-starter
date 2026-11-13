# Aturan proyek untuk AI coding agent

Proyek pelatihan Machine Learning untuk operasi PLTP. Penggunanya sebagian besar **belum pernah
memprogram**, jadi kejelasan lebih penting daripada kecanggihan.

## Data
- Data mentah ada di `data/` dan **TIDAK BOLEH diubah, ditimpa, atau dihapus**.
- Simpan semua hasil olahan ke `data/olahan/`.
- Arti setiap kolom dan rentang wajarnya ada di `data/kamus_data.md` — baca sebelum menganalisis.
- `kode_unit` di `produksi_bulanan.csv` punya salah ketik huruf besar-kecil; ada 1 baris
  duplikat dan 12 nilai kosong di `energi_aktual_mwh`. **Jangan memperbaikinya diam-diam** —
  tunjukkan dulu ke pengguna dan minta keputusan.

## Kode
- Python dengan pandas, matplotlib, scikit-learn, dan Streamlit. Jangan menambah library lain
  tanpa bertanya.
- Notebook ada di `notebook/` dan membaca data lewat path relatif `../data/...`.
  Aplikasi Streamlit ada di `app/` dan membaca data relatif terhadap lokasi file aplikasi.
- Satu sel notebook = satu langkah. Beri komentar singkat **dalam bahasa Indonesia**.
- Setiap langkah yang mengubah jumlah baris (`merge`, `dropna`, `drop_duplicates`, filter)
  harus mencetak jumlah baris sebelum dan sesudah.
- Untuk model ML: selalu buat **baseline** sederhana, pisahkan train–test sebelum
  pra-pemrosesan, dan laporkan metrik pada data test.

## Cara bekerja
- Sebelum menulis kode untuk tugas yang lebih dari satu langkah, jelaskan **rencana** dulu.
- Setelah menjalankan kode, jelaskan hasilnya dalam 2–3 kalimat bahasa Indonesia, termasuk
  hal yang mungkin keliru atau perlu diperiksa pengguna.
- Bila memperbaiki error, jelaskan penyebabnya. Jangan "memperbaiki" dengan membuang data.
