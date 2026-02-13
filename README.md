# 🕌 SunnahSearch - Information Retrieval System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

> **Sistem Temu Kembali Informasi (Search Engine) untuk Hadits menggunakan Algoritma BM25.**

---

## 📖 Tentang Projek

**SunnahSearch** adalah sebuah aplikasi mesin pencari (search engine) berbasis web yang dikembangkan untuk memudahkan pengguna dalam menelusuri koleksi Hadits dan Sunnah.

Projek ini dibuat sebagai bagian dari pemenuhan tugas mata kuliah **Information Retrieval (Temu Kembali Informasi)**. Sistem ini mengimplementasikan algoritma **Okapi BM25** (Best Matching 25) untuk melakukan *ranking* (perangkingan) dokumen, sehingga hasil pencarian yang ditampilkan adalah yang paling relevan dengan kata kunci pengguna.

### 🧮 Algoritma: BM25
Sistem ini tidak hanya mencocokkan kata (exact match), tetapi menghitung skor relevansi berdasarkan probabilitas kemunculan kata dalam dokumen (Hadits) dibandingkan dengan keseluruhan koleksi data.

---

## 📂 Dataset

Data yang digunakan dalam aplikasi ini bersumber dari Kaggle:
* **Nama Dataset:** Sunnah Dataset (`Sunnah.csv`)
* **Sumber:** [Kaggle - Ronnie Aban Sunnah Dataset](https://www.kaggle.com/datasets/ronnieaban/sunnah)
* **Konten:** Berisi teks Hadits dalam Bahasa Arab, Terjemahan (Indonesia/Inggris), dan Nama Perawi.

---

## ✨ Fitur Utama

Aplikasi ini dilengkapi dengan berbagai fitur untuk memaksimalkan pengalaman pencarian:

* **🔍 Search Engine Hadits:** Pencarian cepat dan akurat menggunakan indexing BM25.
* **⚡ Mode Pencarian Fleksibel:**
    1.  **Pencarian Umum:** Mencari kata kunci di seluruh database hadits.
    2.  **Perawi Spesifik:** Menampilkan seluruh hadits dari perawi tertentu (misal: Bukhari, Muslim).
    3.  **Kombinasi (Teks & Perawi):** Mencari topik tertentu (misal: "puasa") hanya di dalam koleksi perawi tertentu (misal: "Bukhari").
* **🎚️ Filter Hasil:** Batasi jumlah hasil yang ditampilkan (5, 15, 30, 50, atau Tampilkan Semua) untuk memudahkan navigasi.
* **📱 Responsif:** Tampilan antarmuka yang modern dan rapi (menggunakan Tailwind CSS).

---

## 📸 Dokumentasi (Screenshots)

Berikut adalah tampilan antarmuka aplikasi **SunnahSearch**:

### 1. Tampilan Awal (Beranda)
*Halaman utama dengan kolom pencarian yang bersih dan opsi filter.*
<img src="https://github.com/user-attachments/assets/b55b49e4-aa3e-4eb5-924a-3f3512833b63" alt="Tampilan Awal SunnahSearch" width="800" />

---

### 2. Hasil Pencarian
*Menampilkan teks Arab, Terjemahan, dan Skor Relevansi BM25.*
<img src="https://github.com/user-attachments/assets/a969c7a9-1934-43db-945b-dcb119d4797d" alt="Hasil Pencarian Hadits" width="800" />

---

### 3. Halaman Tentang
*Informasi mengenai pengembang dan dataset.*
<img src="https://github.com/user-attachments/assets/90d223c8-77ac-493e-934d-00c46b1153f3" alt="Halaman Tentang" width="800" />

---

## 🛠️ Instalasi & Cara Menjalankan

Jika Anda ingin menjalankan projek ini di komputer lokal Anda, ikuti langkah berikut:

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/aliridwan15/SearchHadist-Information-Retrieval-.git](https://github.com/aliridwan15/SearchHadist-Information-Retrieval-.git)
    cd SearchHadist-Information-Retrieval-
    ```

2.  **Install Library yang Dibutuhkan**
    Pastikan Python sudah terinstal, lalu jalankan:
    ```bash
    pip install flask pandas rank_bm25
    ```

3.  **Jalankan Aplikasi**
    ```bash
    python app/__init__.py
    ```

4.  **Buka di Browser**
    Akses alamat berikut di browser Anda:
    `http://127.0.0.1:5000`

---

## 👨‍💻 Tim Pengembang

Projek ini dikembangkan oleh:

| Nama | NIM | Peran |
| :--- | :--- | :--- |
| **Ali Ridwan Nurhasan** | **230411100154** | **Fullstack Developer** |

---

<div align="center">
  <small>Dibuat dengan ❤️ untuk Tugas Information Retrieval</small>
</div>
