# Rencana koneksi: bila AI tidak bisa diakses

Jaringan tempat pelatihan bisa memblokir sebagian layanan AI. Pakai urutan di bawah. Jangan
menghabiskan lebih dari **10 menit** mencoba satu rencana — langsung turun ke rencana
berikutnya; kelas tetap berjalan.

| Rencana | Alat | Butuh | Cocok bila |
|---|---|---|---|
| **A** | Antigravity atau VS Code + Copilot | akses Google / GitHub | semuanya lancar (alat utama) |
| **B** | OpenCode (agent open-source, model gratis) | akses `opencode.ai` | Antigravity/Copilot terblokir atau kuota habis |
| **C** | Google Colab + Gemini (di browser) | akun Google, browser | laptop gagal instalasi, atau editor tidak bisa tersambung |
| **D** | Notebook rekaman prompt | tidak butuh internet | semua rencana di atas gagal |

Data pelatihan bersifat **simulasi**, jadi boleh dikirim ke AI cloud. Data operasional nyata
hanya boleh diproses dengan AI yang disetujui perusahaan.

## Uji cepat (2 menit)

1. Buka `https://github.com`, `https://gemini.google.com`, dan `https://opencode.ai` di browser.
2. Di Antigravity atau VS Code + Copilot, ketik di panel chat: *"Balas dengan kata OK."*

Jawaban muncul dalam ±10 detik → **Rencana A berjalan**. Tidak muncul / error jaringan → lanjut.

## Rencana A — Antigravity / VS Code + Copilot

Alat utama pelatihan. Bila jaringan lokasi memblokir, coba **VPN** yang diizinkan kebijakan IT
perusahaan atau **hotspot HP** (satu HP untuk satu pasangan cukup; ±50–150 MB per jam untuk
agent).

## Rencana B — OpenCode

OpenCode adalah AI coding agent open-source. Ia otomatis membaca `AGENTS.md` di repo ini, dan
menyediakan beberapa **model gratis tanpa akun** (OpenCode Zen).

1. Unduh *OpenCode Desktop* untuk Windows dari `https://opencode.ai/download`, lalu pasang.
2. Buka folder `pltp-ml-starter` di OpenCode. Di VS Code: buka terminal di folder ini lalu ketik
   `opencode`.
3. Ketik `/models` dan pilih model yang bertanda **free**.
4. Ketik prompt seperti biasa. OpenCode bisa membuat dan menjalankan file, sama seperti agent di
   Antigravity — **tetap baca setiap perubahan sebelum menyetujuinya**.

Model gratis bisa lambat atau kena batas pemakaian di jam ramai, dan daftar modelnya berganti
dari waktu ke waktu. Kalau satu model lambat, pilih model gratis lain lewat `/models`.

## Rencana C — Google Colab + Gemini

Tidak perlu instalasi apa pun: notebook berjalan di server Google, dan Gemini sudah ada di
dalamnya.

1. Buka `https://colab.research.google.com`, masuk dengan akun Google, buat notebook baru.
2. Di sel pertama, ambil repo ini:

   ```python
   !git clone https://github.com/gunturbudi/pltp-ml-starter.git
   %cd pltp-ml-starter
   ```

   Tidak bisa `git clone`? Unggah file dari folder `data/` lewat ikon folder di panel kiri.
3. Klik tombol **Gemini** (ikon bintang) atau *"Generate"* di sel kosong, lalu ketik prompt
   seperti biasa. Gemini di Colab bisa menulis sel kode dan menjelaskan error.
4. Simpan pekerjaan: **File → Download → .ipynb**, lalu taruh di folder `notebook/` laptop Anda.

Catatan:

- File di Colab **hilang** saat sesi berakhir. Unduh hasil (`.ipynb`, `data/olahan/*.csv`)
  sebelum menutup tab.
- Path di Colab mengikuti `%cd` di atas: tulis `data/produksi_bulanan.csv`, bukan
  `../data/produksi_bulanan.csv`.
- Dashboard Streamlit dan skrip `.py` dijalankan di laptop, bukan di Colab.

## Rencana D — rekaman prompt (tanpa internet sama sekali)

Buka notebook di folder `notebook/`:

| Sesi | Notebook |
|---|---|
| Hari 1, 15.00 — Eksperimen EDA | `ai-rekaman-hari1-eda.ipynb` |
| Hari 2, 10.00 — Langkah 1–3, 7 (kualitas data) | `ai-rekaman-hari2-cleaning.ipynb` |
| Hari 2, 10.40 — Langkah 4–6 (EDA lapis 2–4) | `ai-rekaman-hari2-eda-lapis.ipynb` |

Setiap langkah berisi prompt (sama dengan di slide) dan kode yang dihasilkan AI untuk prompt
itu. Tugas Anda sama dengan vibe coding: **baca kodenya, tebak hasilnya, jalankan, periksa.**
Begitu akses AI tersedia, ketik prompt yang sama ke agent dan bandingkan hasilnya.
