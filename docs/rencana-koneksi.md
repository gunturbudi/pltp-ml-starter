# Rencana koneksi: bila AI tidak bisa diakses

Jaringan tempat pelatihan bisa memblokir sebagian layanan AI. Pakai urutan di bawah. Jangan
menghabiskan lebih dari **10 menit** mencoba satu rencana — langsung turun ke rencana
berikutnya; kelas tetap berjalan.

| Rencana | Alat | Butuh | Cocok bila |
|---|---|---|---|
| **A** | Antigravity, VS Code + Copilot, Cursor, Kiro, atau Windsurf | akses situs editor + akun | semuanya lancar (alat utama: Antigravity) |
| **B** | OpenCode (agent open-source, model gratis) — atau agent terminal lain | akses `opencode.ai` | editor Rencana A terblokir atau kuota habis |
| **C** | Google Colab + Gemini (di browser) | akun Google, browser | laptop gagal instalasi, atau editor tidak bisa tersambung |
| **D** | Notebook rekaman prompt | tidak butuh internet | semua rencana di atas gagal |

Data pelatihan bersifat **simulasi**, jadi boleh dikirim ke AI cloud. Data operasional nyata
hanya boleh diproses dengan AI yang disetujui perusahaan.

## Uji cepat (2 menit)

1. Buka `https://github.com`, `https://gemini.google.com`, dan `https://opencode.ai` di browser.
2. Di editor pilihan Anda (Antigravity, VS Code + Copilot, Cursor, Kiro, …), ketik di panel chat: *"Balas dengan kata OK."*

Jawaban muncul dalam ±10 detik → **Rencana A berjalan**. Tidak muncul / error jaringan → lanjut.

## Rencana A — editor ber-AI

Alat utama pelatihan adalah **Antigravity**. Semua editor di bawah dibangun di atas VS Code, jadi
langkah *Open Folder*, *Select Kernel*, dan menjalankan notebook sama persis:

| Editor | Akun | Panel agent |
|---|---|---|
| Antigravity (Google) | akun Google | panel *Agent* |
| VS Code + GitHub Copilot Free | akun GitHub | ikon Copilot → *Chat*, mode *Agent* |
| Cursor | email / Google / GitHub | panel *Agent* (`Ctrl+L`) |
| Kiro (AWS) | Google / GitHub / AWS Builder ID | panel chat, mode *Vibe* atau *Spec* |
| Windsurf | email / Google | panel *Cascade* |

Semuanya gratis dengan kuota; kuota itu bisa habis di tengah hari. Lihat bagian
**Kuota habis** di bawah. Bila jaringan lokasi memblokir, coba **VPN** yang diizinkan kebijakan IT
perusahaan atau **hotspot HP** (satu HP untuk satu pasangan cukup; ±50–150 MB per jam untuk
agent).

## Rencana B — OpenCode (atau agent terminal lain)

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

Agent terminal lain yang juga bisa dipakai dari terminal VS Code bila Anda punya akunnya:
**Gemini CLI** (`gemini`, akun Google), **Codex CLI** (`codex`, akun ChatGPT), **Claude Code**
(`claude`, berbayar). Ekstensi VS Code **Cline**, **Roo Code**, atau **Continue** bisa memakai
model dari OpenRouter atau model lokal **Ollama** (tanpa internet, tetapi lambat di laptop).

## Kuota habis: ganti alat, bukan mulai ulang

Riwayat chat tidak ikut pindah ke editor lain, tetapi **file di folder ini ikut**. Karena aturan
proyek ada di `AGENTS.md` dan kemajuan dicatat di `docs/catatan-kerja.md`, editor baru bisa
langsung melanjutkan.

1. **Sebelum pindah** (kalau agent lama masih bisa menjawab):
   > *Perbarui docs/catatan-kerja.md: tujuan, yang sudah selesai, file yang diubah, keputusan
   > saya, langkah berikutnya, masalah terbuka.*
2. Simpan semua file (`Ctrl+K S`), tutup editor lama.
3. Buka **folder yang sama** di editor lain → *Select Kernel* → `anaconda3 (base)`.
4. **Prompt pertama** di editor baru:
   > *Baca AGENTS.md, data/kamus_data.md, dan docs/catatan-kerja.md. Ringkas posisi kita dalam
   > 3 kalimat, lalu lanjutkan "Langkah berikutnya". Jangan mengulang yang sudah selesai.*
5. Catat perpindahan di `prompt-log.md` dan di bagian *Alat yang dipakai* catatan kerja.

Yang **tidak** ikut pindah: riwayat chat, "memori" agent, dan aturan yang disimpan di pengaturan
khusus satu editor (`.cursor/rules/`, `.kiro/steering/`, dll.). Karena itu aturan proyek cukup
ditulis di `AGENTS.md`. Cursor, Kiro, Windsurf, Copilot, OpenCode, dan Codex membaca
`AGENTS.md`; `GEMINI.md` dan `CLAUDE.md` di repo ini isinya sama, untuk Gemini dan Claude Code.

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
