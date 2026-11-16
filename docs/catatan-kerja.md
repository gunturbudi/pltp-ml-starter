# Catatan kerja

File ini adalah "ingatan" proyek. Agent membacanya saat mulai dan memperbaruinya setelah
menyelesaikan satu tugas. Riwayat chat hilang saat Anda pindah editor; isi file ini tidak.

## Tujuan saat ini
Menyediakan kode untuk membuka dan mengeksplorasi `data/produksi_bulanan.csv` tanpa mengubah data mentah.

## Sudah selesai
- [2026-11-16] Eksplorasi struktur, kualitas, dan pola produksi bulanan; ringkasan dihitung tanpa menyimpan perubahan pada CSV.
- [2026-11-16] Membuat dan menjalankan skrip Python untuk mengulang ringkasan, pemeriksaan kualitas, dan grafik.
- [2026-11-16] Menambahkan sel pembuka CSV di `notebook/latihan_notebook.ipynb`; path relatif berhasil diuji dari folder notebook.
- [2026-11-16] Menambahkan sel grafik scatter `uap_rencana_ton` vs `uap_aktual_ton` per unit di `notebook/latihan_notebook.ipynb` menggunakan `gaya_grafik.py`.

## File yang dibuat / diubah
- `skrip/eksplorasi_produksi.py` — laporan kualitas data, ringkasan, dan grafik eksplorasi.
- `notebook/latihan_notebook.ipynb` — sel pandas untuk membaca data dan grafik scatter `uap_rencana_ton` vs `uap_aktual_ton`.
- `gambar/eksplorasi_cf_per_unit.png` dan `gambar/eksplorasi_energi_tahunan.png` — keluaran grafik skrip.
- `docs/catatan-kerja.md` — catatan hasil eksplorasi dan tindak lanjut.

## Keputusan pengguna
Belum ada. Tidak ada pembersihan atau perubahan data yang dilakukan.

## Langkah berikutnya
1. Tinjau nilai `energi_aktual_mwh` di luar rentang dan tentukan perlakuan saat cleaning.
2. Jika cleaning diminta, minta keputusan untuk variasi huruf `kode_unit`, baris duplikat, dan nilai kosong sebelum mengubah data.

## Masalah terbuka
- Kernel notebook Python 3.12.13 belum memiliki `ipykernel`; sel belum bisa dijalankan dari notebook, meski baris pembacaan CSV berhasil diuji dari folder `notebook/`.
- Beberapa nilai berada di luar rentang kamus: sembilan `uap_rencana_ton` dan delapan `energi_rencana_mwh` di bawah batas minimum; delapan `energi_aktual_mwh` di atas 75.000. Perlu verifikasi.
- Kode `arl`/`ARL` dan `Btl`/`btl`/`BTL` bervariasi huruf besar-kecil; terdapat satu duplikat identik dan 12 energi aktual kosong.

## Alat yang dipakai
<!-- - 17 Nov: Antigravity → kuota habis → lanjut di Cursor -->
