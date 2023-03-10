# Tugas-ASD-Kevin-Aditya-Agusto-Awang

Nama: Kevin Aditya Agusto Awang

Nim: 2209116101

Kelas: Sistem Informasi B 2022

Program searching

Program ini adalah sebuah program yang menggunakan teknik searching dengan metode Jump Search untuk mencari indeks dari elemen-elemen dalam array rudi.
Pada bagian awal program, array rudi didefinisikan dengan beberapa elemen yang berisi nama-nama. Kemudian terdapat sebuah fungsi bernama jump, yang akan digunakan untuk melakukan pencarian dengan metode Jump Search.

Fungsi jump mengambil dua parameter, yaitu sebuah array arr dan sebuah nilai x yang ingin dicari di dalam array arr. Pada fungsi ini, dilakukan proses untuk mencari indeks dari nilai x dalam array arr dengan menggunakan algoritma Jump Search.

Setelah fungsi jump didefinisikan, program melanjutkan dengan memanggil fungsi Gass. Fungsi ini akan menampilkan menu pada console yang meminta pengguna untuk memilih metode searching yang akan digunakan. Jika pengguna memilih menu pertama, maka fungsi jump akan dipanggil untuk melakukan pencarian indeks dari setiap elemen yang ingin dicari dalam array rudi. Jika pengguna memilih menu kedua, maka program akan berhenti dan keluar.

Pada program utama, setelah memanggil fungsi Gass, program akan terus berjalan dalam sebuah loop hingga pengguna memilih untuk keluar. Selama program berjalan, setiap hasil pencarian indeks dari setiap elemen dalam array 'rudi' akan ditampilkan pada console. Jika nilai x tidak ditemukan dalam array arr, maka fungsi jump akan mengembalikan nilai -1 dan pesan akan ditampilkan pada console bahwa nilai tersebut tidak ditemukan dalam array.

Pada akhir program, setelah pengguna memilih untuk keluar, program akan berhenti.

Fungsi "jump()"
untuk melakukan Jump Search pada array/list "rudi". Fungsi ini akan mencari indeks dari elemen "Arsel", "Avivah", "Daiva", "Wahyu", dan "Wibi" secara berurutan. Fungsi ini juga akan mencetak daftar data yang akan dicari indeksnya sebelum melakukan pencarian, dan jika elemen yang dicari ditemukan, maka fungsi ini akan mencetak pesan yang memberitahukan indeks dari elemen tersebut.

Fungsi "Gass()"
Fungsi ini akan menampilkan menu pilihan antara menggunakan Jump Search atau keluar dari program. Jika pengguna memilih opsi Jump Search, maka fungsi ini akan memanggil fungsi "jump()" dan menampilkan hasil pencarian. Setelah itu, pengguna diminta untuk menekan Enter untuk kembali ke menu pilihan. Jika pengguna memilih opsi keluar dari program, maka program akan berhenti.

Selain itu, program ini juga menggunakan beberapa modul, yaitu "os", "time", dan "math". 
Modul "os" 
digunakan untuk membersihkan layar terminal. 
Modul "time" 
digunakan untuk memberi jeda waktu pada program.
Modul "math"
digunakan untuk menghitung nilai akar kuadrat dari suatu bilangan.
