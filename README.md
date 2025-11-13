# **Laporan Analisis Data**
<img width="1920" height="1008" alt="Screenshot 2025-11-13 230655" src="https://github.com/user-attachments/assets/5e3ef6a7-787d-4303-8fb8-945a7aeb2119" />

# **Deskripsi**

Program ini dibuat untuk menganalisis data nilai siswa dari file nilai_siswa.csv menggunakan bahasa pemrograman Python.
Analisis dilakukan dengan bantuan library Pandas, Matplotlib, dan Seaborn untuk menampilkan ringkasan statistik dan visualisasi data.

# **Library yang Digunakan**
1. pandas → untuk membaca dan mengolah data dari file CSV
2. matplotlib.pyplot → untuk membuat grafik batang (bar chart)
3. seaborn → untuk membuat boxplot yang menunjukkan sebaran nilai

   Dataset

# **File data bernama nilai_siswa.csv berisi tiga kolom utama:**
| Kolom   | Keterangan                 |
| ------- | -------------------------- |
| `Nama`  | Nama siswa                 |
| `Mapel` | Mata pelajaran             |
| `Nilai` | Nilai yang diperoleh siswa |

# **Output yang Dihasilkan**

Menampilkan semua data siswa seperti di terminal 
#

<img width="1920" height="1008" alt="Screenshot 2025-11-13 231522" src="https://github.com/user-attachments/assets/a2989470-d9bf-4e3a-8450-8d491729d38a" />

# **Visualisasi Data**
**1. Grafik Batang** — Rata-Rata Nilai per Mapel
   Grafik batang di atas menunjukkan rata-rata nilai siswa untuk setiap mata pelajaran. Dari hasil perhitungan data.groupby('Mapel')['Nilai'].mean(), didapatkan rata-rata nilai seperti hasil output di atas.

**Penjelasan:**
- Rata-rata nilai tertinggi terdapat pada Matematika (91.5), menandakan siswa paling unggul di pelajaran ini.
- Nilai rata-rata terendah terdapat pada Produktif (83.33), menunjukkan perlu adanya peningkatan pemahaman atau latihan pada mata pelajaran ini.
- Bahasa Indonesia dan Bahasa Inggris memiliki nilai rata-rata yang cukup stabil di kisaran 84-an.

**2. Boxplot** — Sebaran Nilai per Mata Pelajaran
   Visualisasi ini menunjukkan sebaran nilai siswa (distribusi) di setiap mata pelajaran menggunakan boxplot.

**Keterangan:**
- Garis tengah pada kotak menunjukkan median (nilai tengah).
- Bagian atas dan bawah kotak menunjukkan kuartil atas dan bawah.
- Titik di luar whisker (jika ada) menunjukkan outlier atau nilai yang menyimpang dari kebanyakan data.

**Analisis dari grafik:**
- Matematika memiliki sebaran nilai tinggi dengan median tertinggi (sekitar 90–95), menandakan performa sangat baik secara keseluruhan.
- Fisika menunjukkan variasi yang cukup besar — terdapat beberapa siswa dengan nilai rendah (~75), namun juga banyak yang tinggi (~95).
- Bahasa Indonesia dan Bahasa Inggris memiliki distribusi nilai yang lebih rapat, menandakan konsistensi performa siswa.
- Produktif memiliki rentang nilai yang cukup lebar, menunjukkan perbedaan kemampuan antar siswa yang cukup signifikan.
