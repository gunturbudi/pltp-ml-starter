# Rencana koneksi: bila AI cloud tidak bisa diakses

Jaringan tempat pelatihan bisa memblokir layanan AI cloud (Google Antigravity, GitHub Copilot).
Pakai urutan di bawah. Jangan menghabiskan lebih dari **10 menit** mencoba satu rencana —
langsung turun ke rencana berikutnya; kelas tetap berjalan.

## Uji cepat (2 menit)

1. Buka `https://github.com` dan `https://gemini.google.com` di browser.
2. Di Antigravity atau VS Code + Copilot, ketik di panel chat: *"Balas dengan kata OK."*

Jawaban muncul dalam ±10 detik → **Rencana A berjalan**. Tidak muncul / error jaringan → lanjut.

## Rencana A — AI cloud lewat VPN atau hotspot

- **VPN** yang diizinkan kebijakan IT perusahaan, atau
- **hotspot HP** (satu HP untuk satu pasangan cukup; pemakaian ±50–150 MB per jam untuk agent).

Data pelatihan bersifat simulasi, jadi boleh dikirim ke AI cloud.

## Rencana B — AI lokal perusahaan (Qwen) di VS Code

Data tidak keluar dari jaringan perusahaan. Model lokal lebih lemah untuk mode agent, tetapi
cukup untuk chat dan potongan kode.

1. Di VS Code, pasang ekstensi **Continue** (`Continue.continue`).
2. Buka konfigurasi Continue (ikon roda gigi → *config.yaml*) dan isi dengan alamat dari
   instruktur:

   ```yaml
   name: PGE Lokal
   version: 1.0.0
   schema: v1
   models:
     - name: Qwen lokal PGE
       provider: openai                       # server kompatibel OpenAI (vLLM, Ollama, LM Studio)
       model: NAMA-MODEL-DARI-INSTRUKTUR
       apiBase: http://ALAMAT-SERVER:PORT/v1
       apiKey: KUNCI-BILA-ADA
       roles: [chat, edit, apply]
   ```

3. Ketik prompt di panel Continue, salin kode ke notebook, jalankan, periksa.

Alamat server, nama model, dan kunci **tidak** ditulis di repositori publik ini — diberikan
langsung oleh instruktur di kelas.

## Rencana C — rekaman prompt (tanpa internet sama sekali)

Buka notebook di folder `notebook/`:

| Sesi | Notebook |
|---|---|
| Hari 1, 15.00 — Eksperimen EDA | `ai-rekaman-hari1-eda.ipynb` |
| Hari 2, 10.00 — Data cleaning | `ai-rekaman-hari2-cleaning.ipynb` |

Setiap langkah berisi prompt (sama dengan di slide) dan kode yang dihasilkan AI untuk prompt
itu. Tugas Anda sama dengan vibe coding: **baca kodenya, tebak hasilnya, jalankan, periksa.**
Begitu akses AI tersedia, ketik prompt yang sama ke agent dan bandingkan hasilnya.
