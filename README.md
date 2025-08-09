# Personal Recommendation System

## Deskripsi
Personal Recommendation System adalah sebuah produk digital yang bertujuan untuk memberikan saran konten (film) yang relevan kepada pengguna berdasarkan riwayat interaksi dan preferensi genre mereka. Sistem ini membantu pengguna menemukan film yang sesuai dengan minat mereka secara efisien. Versi MVP ini berfokus pada fungsionalitas inti dengan antarmuka yang sederhana.

## Fitur Utama
- **Rekomendasi Film Berbasis Genre**: Sistem merekomendasikan film berdasarkan genre favorit yang telah ditentukan oleh pengguna.
- **Profil Pengguna Sederhana**: Setiap pengguna memiliki profil yang menyimpan preferensi genre dan riwayat film yang telah ditonton.
- **Pemilihan Profil**: Aplikasi memungkinkan untuk beralih antar profil pengguna yang berbeda untuk melihat rekomendasi yang dipersonalisasi.
- **Umpan Balik Pengguna**: Pengguna dapat memberikan umpan balik ("relevan" atau "tidak relevan") pada setiap rekomendasi untuk potensi penyempurnaan di masa depan.

## Teknologi yang Digunakan
- **Bahasa:** Python
- **Kerangka Kerja:** Flask
- **Penyimpanan Data:** File JSON (untuk versi MVP)

## Instalasi
Berikut adalah langkah-langkah untuk menginstal dan menyiapkan proyek ini di lingkungan lokal Anda.

1.  **Clone Repositori**
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <NAMA_DIREKTORI_PROYEK>
    ```

2.  **Buat dan Aktifkan Virtual Environment** (Direkomendasikan)
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Di Windows, gunakan: venv\Scripts\activate
    ```

3.  **Instal Dependensi**
    Instal semua paket yang dibutuhkan menggunakan file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan
Setelah instalasi selesai, Anda dapat menjalankan aplikasi dengan cara berikut:

1.  **Jalankan Server Flask**
    Dari direktori utama proyek, jalankan perintah berikut:
    ```bash
    python3 app/app.py
    ```

2.  **Akses Aplikasi**
    Buka browser web Anda dan kunjungi alamat berikut:
    ```
    http://127.0.0.1:5001
    ```

3.  **Pilih Profil**
    Di halaman utama, klik salah satu nama pengguna (misalnya, Andi, Budi) untuk melihat rekomendasi film yang telah disesuaikan untuk mereka.

## Kontribusi
Kami menyambut baik kontribusi dari siapa saja. Jika Anda ingin berkontribusi, silakan ikuti panduan berikut:
1.  *Fork* repositori ini.
2.  Buat *branch* baru untuk fitur Anda (`git checkout -b fitur/NamaFitur`).
3.  *Commit* perubahan Anda (`git commit -m 'Menambahkan Fitur X'`).
4.  *Push* ke *branch* Anda (`git push origin fitur/NamaFitur`).
5.  Buka *Pull Request*.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
