# Kamus Data — Paket Latihan "PLTP Nusantara"

> **Status data.** Seluruh isi paket ini adalah **data simulasi** yang dibuat khusus untuk
> pelatihan. Bukan data operasional PGE, bukan turunan dari data PGE. Nama unit, lokasi,
> angka produksi, harga, dan catatan gangguan seluruhnya **fiktif dan berbasis asumsi**.
> Jangan dipakai untuk analisis atau pengambilan keputusan nyata.

Bacalah dokumen ini sebelum Hari 2. Dua halaman, tidak perlu dihafal — cukup tahu di mana
mencarinya kalau nanti lupa.

---

## Skenario

PT Energi Panas Nusantara (fiktif) mengoperasikan **6 unit PLTP** di enam lokasi fiktif.
Data mencakup **Januari 2011 – Desember 2025** (15 tahun, 180 bulan).

Setiap bulan perusahaan harus menjawab tiga pertanyaan. Ketiganya menjadi benang merah
seluruh latihan:

| # | Pertanyaan operasional | Jenis tugas ML |
|---|---|---|
| **P1** | Bulan-bulan mana yang berkarakter serupa, sehingga cocok dijadikan jendela pemeliharaan? | Clustering |
| **P2** | Unit mana yang berisiko mengalami gangguan bulan depan? | Klasifikasi |
| **P3** | Berapa harga energi yang wajar diusulkan, dan berapa produksi yang bisa dijanjikan? | Regresi + time-series |

---

## Istilah yang perlu diketahui lebih dulu

| Istilah | Arti dalam bahasa sehari-hari |
|---|---|
| **MW** (megawatt) | Ukuran *kemampuan* pembangkit pada satu saat. Seperti tenaga maksimum mesin mobil. |
| **MWh** (megawatt-hour) | Ukuran *jumlah energi* yang dihasilkan selama satu periode. Seperti jarak yang benar-benar ditempuh. |
| **CF** (*capacity factor*) | Berapa persen dari kemampuan maksimum yang benar-benar terpakai selama sebulan. CF 85 % artinya unit berproduksi setara 85 % dari kemungkinan terbaiknya. Rumus: `energi_aktual_mwh ÷ (kapasitas_mw × jam_dalam_bulan) × 100`. |
| **Derating** | Unit tetap jalan, tetapi tidak bisa pada tenaga penuh. |
| **Outage** | Unit berhenti sama sekali. |
| **MO** (*maintenance outage*) | Berhenti **terencana** untuk pemeliharaan. Sudah dijadwalkan jauh hari. |
| **FO** (*forced outage*) | Berhenti **paksa** karena gangguan. Tidak direncanakan — inilah yang ingin diprediksi di P2. |
| **PD / FD** | Derating terencana (*planned derating*) dan derating paksa (*forced derating*). |
| **Reserve margin** | Kelebihan kapasitas sistem di atas permintaan puncak, dalam persen. Makin kecil, makin genting kondisi sistem, dan makin mahal kalau ada unit yang berhenti. |
| **Alokasi** | Jumlah MWh yang disepakati akan dikirim, hasil negosiasi bulanan. |
| **Realisasi** | Jumlah MWh yang benar-benar terkirim. |

---

## a. `unit_pembangkit.csv` — 6 baris

Reference table. Satu baris untuk satu unit; dipakai untuk melengkapi tabel lain lewat `merge`.

| Kolom | Tipe | Satuan | Rentang wajar | Keterangan |
|---|---|---|---|---|
| `kode_unit` | teks | — | ARL, BTL, CKR, DRG, EKL, FRS | Kunci penghubung ke semua tabel lain |
| `nama_unit` | teks | — | — | Arloka, Bantala, Cakrawana, Dirgantara, Ekalaya, Farasindo |
| `kapasitas_mw` | angka | MW | 20 – 110 | Kapasitas terpasang |
| `tahun_operasi` | angka | tahun | 2002 – 2011 | Tahun unit mulai beroperasi |
| `jenis_turbin` | teks | — | Single Flash / Double Flash / Binary | Teknologi pembangkitan |
| `jumlah_sumur` | angka | sumur | 4 – 22 | Jumlah sumur produksi yang memasok unit |

---

## b. `produksi_bulanan.csv` — 1.081 baris

Tabel utama. Satu baris = satu unit pada satu bulan.
Seharusnya 1.080 baris (6 unit × 15 tahun × 12 bulan); baris ke-1.081 adalah **duplikat yang
sengaja diselipkan** sebagai bahan latihan data cleaning.

| Kolom | Tipe | Satuan | Rentang wajar | Keterangan |
|---|---|---|---|---|
| `tanggal` | tanggal | — | 2011-01-01 … 2025-12-01 | Selalu tanggal 1, menandai bulan |
| `tahun` | angka | tahun | 2011 – 2025 | Dipisah agar mudah dipakai sebagai feature |
| `bulan` | angka | 1–12 | 1 – 12 | Idem |
| `kode_unit` | teks | — | 6 kode di atas | **Perhatian:** ada beberapa baris yang huruf besar-kecilnya salah ketik |
| `uap_rencana_ton` | angka | ton | 50.000 – 700.000 | Pasokan uap yang direncanakan |
| `uap_aktual_ton` | angka | ton | 0 – 700.000 | Pasokan uap yang terealisasi |
| `energi_rencana_mwh` | angka | MWh | 5.000 – 75.000 | Produksi listrik yang direncanakan |
| `energi_aktual_mwh` | angka | MWh | 0 – 75.000 | Produksi listrik yang terealisasi. **Ada 12 baris kosong** |
| `jam_operasi` | angka | jam | 0 – 744 | Jam unit benar-benar beroperasi dalam bulan itu |
| `cf_persen` | angka | % | 0 – 95 | Capacity factor. Nilai sangat rendah biasanya menandakan MO atau FO panjang |

> **Catatan cleaning.** Tiga cacat yang sengaja ada di file ini — 12 nilai kosong, beberapa
> `kode_unit` salah ketik huruf besar-kecil, dan 1 baris duplikat — akan ditemukan sendiri
> oleh peserta di Hari 2, lalu diperbaiki di Hari 3.

---

## c. `gangguan.csv` — 200 baris

Satu baris = satu kejadian gangguan. Sumber **label** untuk P2.

| Kolom | Tipe | Satuan | Rentang wajar | Keterangan |
|---|---|---|---|---|
| `id_gangguan` | teks | — | G0001 … G0200 | Nomor urut |
| `kode_unit` | teks | — | 6 kode | Unit yang terdampak |
| `jenis` | teks | — | MO / FO / PD / FD | Lihat tabel istilah di atas |
| `tanggal_mulai` | tanggal | — | 2011 – 2025 | |
| `tanggal_selesai` | tanggal | — | 2011 – 2025 | |
| `durasi_hari` | angka | hari | 1 – 30 | MO paling panjang, FD paling pendek |
| `mw_terdampak` | angka | MW | 2 – 110 | Untuk MO/FO = seluruh kapasitas; untuk PD/FD hanya sebagian |
| `kategori_penyebab` | teks | — | Turbin / Generator / Sumur & Uap / Kelistrikan / Eksternal | |

---

## d. `harga_alokasi.csv` — 1.080 baris

Satu baris = satu unit pada satu bulan. Sumber **target** untuk P3.

| Kolom | Tipe | Satuan | Rentang wajar | Keterangan |
|---|---|---|---|---|
| `tanggal`, `tahun`, `bulan`, `kode_unit` | | | | Kunci, sama dengan tabel produksi |
| `alokasi_mwh` | angka | MWh | 5.000 – 72.000 | Hasil kesepakatan rapat alokasi |
| `realisasi_mwh` | angka | MWh | 0 – 75.000 | Yang benar-benar terkirim |
| `harga_rp_per_kwh` | angka | Rp/kWh | 1.030 – 1.450 | **Target regresi P3** |

---

## e. `indikator_sistem.csv` — 180 baris

Kondisi sistem kelistrikan secara keseluruhan, satu baris per bulan (tidak per unit).
Dipakai dengan cara di-`merge` ke tabel produksi atau harga.

| Kolom | Tipe | Satuan | Rentang wajar | Keterangan |
|---|---|---|---|---|
| `tanggal`, `tahun`, `bulan` | | | | Kunci bulanan |
| `permintaan_sistem_gwh` | angka | GWh | 1.950 – 4.100 | Beban sistem. Naik dari tahun ke tahun |
| `cadangan_sistem_persen` | angka | % | 18 – 36 | Reserve margin. Makin kecil = sistem makin genting |
| `harga_batubara_usd_ton` | angka | USD/ton | 55 – 400 | Acuan harga energi primer pesaing |
| `kurs_rp_usd` | angka | Rp/USD | 9.000 – 17.000 | |
| `curah_hujan_mm` | angka | mm | 5 – 550 | Gambaran ketersediaan PLTA |

---

## f. `log_latihan.csv` — 20 baris

File kecil yang sengaja dibuat pendek, supaya seluruh isinya muat di satu layar.
Dipakai **hanya** pada Materi 3, saat pertama kali berkenalan dengan pandas.

| Kolom | Tipe | Keterangan |
|---|---|---|
| `tanggal` | tanggal | Juni 2025 |
| `kode_unit` | teks | 6 kode |
| `shift` | teks | Pagi / Siang / Malam |
| `operator` | teks | Nama operator (fiktif) |
| `cf_persen` | angka | Capacity factor pada shift itu |
| `catatan` | teks | Catatan bebas operator |

---

## g. `dokumen/` — 30 formulir laporan gangguan (gambar)

Formulir **Laporan Gangguan Pembangkit** fiktif, satu gambar per kejadian. Isinya diambil
dari 30 baris `gangguan.csv` tahun 2023–2025, jadi `gangguan.csv` sekaligus menjadi kunci
jawaban ketika formulir dibaca oleh model AI.

| Hal | Keterangan |
|---|---|
| Nama file | `LG-<id_gangguan>.png` atau `.jpg` — mis. `LG-G0167.png` ↔ `id_gangguan` G0167 |
| Kondisi | 18 **bersih** (diketik), 7 **scan** (miring, buram — file `.jpg`), 5 **tulisan tangan** |
| Isian | nomor laporan, unit, tanggal mulai & selesai (dua format penulisan), beban terdampak (MW), kotak centang jenis gangguan, uraian kejadian, tindakan |
| Sengaja tidak ada | **kategori penyebab** — harus disimpulkan dari uraian kejadian |
| `kunci_dokumen.csv` | isi sebenarnya dari tiap formulir, termasuk kondisinya |

---

## h. `citra_termal/` — 160 citra termal panel listrik (gambar)

Citra inframerah **simulasi** panel listrik (2–4 MCB/terminal beserta kabelnya), seperti hasil
inspeksi termografi rutin. Dipakai untuk latihan data gambar: baseline aturan, lalu model.

| Hal | Keterangan |
|---|---|
| Nama file | `T001.png` … `T160.png` — RGB, 160 × 120 piksel |
| Skala warna | tetap untuk semua gambar: palet *inferno*, hitam = 20 °C, kuning pucat = 100 °C |
| `label.csv` | `file`, `label`, `suhu_maks_c` (suhu tertinggi di gambar, °C — seperti yang dicatat kamera) |
| Label | 80 **normal** · 80 **titik_panas** |
| Aturan label | `titik_panas` bila ada titik **≥ 12 °C lebih panas** dari komponen di sekitarnya (ΔT, seperti praktik termografi). `normal` boleh punya titik hangat ringan (ΔT 2–8 °C) |
| Jebakan | suhu lingkungan (24–38 °C) dan beban berbeda tiap gambar, sehingga panel normal yang panas bisa lebih panas dari titik panas di panel yang dingin. Ambang `suhu_maks_c` saja **tidak sempurna** |

---

## Cara tabel-tabel ini saling terhubung

```
unit_pembangkit.csv ──┐
                      ├── kode_unit ──> produksi_bulanan.csv ──┐
gangguan.csv ─────────┘                                        │
                                                  tanggal ─────┤
indikator_sistem.csv ─── tanggal ──────────────────────────────┤
                                                               │
harga_alokasi.csv ─── tanggal + kode_unit ─────────────────────┘
```

- `unit_pembangkit.csv` dihubungkan lewat **`kode_unit`** saja.
- `indikator_sistem.csv` dihubungkan lewat **`tanggal`** saja (berlaku untuk semua unit).
- `produksi_bulanan.csv` dan `harga_alokasi.csv` dihubungkan lewat **`tanggal` + `kode_unit`**.
- `gangguan.csv` bukan data bulanan; perlu diubah dulu menjadi bulanan sebelum digabung.
  Kodenya sudah disediakan di notebook, tidak perlu dibuat sendiri.
