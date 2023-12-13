# Custom Botol Tumbler

Program ini memungkinkan pengguna untuk melakukan transformasi warna digital pada desain botol tumbler. Berikut langkah-langkah penggunaannya:

## Persyaratan

Pastikan telah terpasang beberapa pustaka Python berikut sebelum menjalankan program:
- OpenCV
- NumPy
- Matplotlib

## Cara Penggunaan

1. **Persiapan Citra:**
   - Masukkan dua citra: citra botol tumbler yang akan di-customize dan citra warna/desain pola yang ingin diaplikasikan pada tumbler.
  
2. **Jalankan Program:**
   - Buka terminal dan jalankan program Python: `python customize_tumbler.py`.
  
3. **Input Citra:**
   - Program akan meminta masukan citra botol tumbler dan citra desain pola yang diinginkan.

4. **Proses Transformasi:**
   - Program akan menjalankan serangkaian proses pengolahan citra seperti konversi citra ke grayscale, penghalusan citra, deteksi tepi menggunakan operator Laplacian dan Canny, serta pembuatan mask untuk identifikasi area tertentu dalam citra.

5. **Hasil Akhir:**
   - Setelah proses selesai, program akan menampilkan citra hasil transformasi berupa tampilan botol tumbler dengan desain yang sudah di-customize.

## Uji Coba Program

Anda juga dapat mencoba program ini dengan memasukkan beberapa citra desain yang berbeda untuk melihat hasilnya. Pastikan citra memiliki format yang didukung oleh program dan sesuaikan dengan ketentuan yang diminta.
