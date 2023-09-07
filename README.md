# python_project_selfservice_cashier

## Latar Belakang Persoalan

Code ini dibuat untuk menjawab tugas project Python Pacmann. Dalam tugas ini, Pacmann mengisahkan seorang pengusaha Supermarket besar online yang ingin mengembangkan bisnisnya. Terobosan yang dilakukan adalah dengan membuat sistem kasir self-service. Dengan sistem kasir seperti ini, pembeli dari berbagai penjuru kota dapat memasukkan sendiri nama barang yang ingin dibeli, jumlah barang yang mau diambil, dan harga barang tersebut. 

Sistem dibuat sefleksibel mungkin dengan mempertimbangkan skenario lain. Misal, ketika pembeli salah memasukkan nama, jumlah, atau harga barang, ia dapat mengubahnya dengan nama, jumlah, atau harga baru yang sesuai. Tidak hanya itu, pembeli juga memiliki opsi untuk menghapus nama barang yang akhirnya tidak jadi dibeli. Proses menghapus ini dapat terjadi secara satu per satu atau sekaligus. 

Berikutnya, ketika pembeli sudah mantap dengan pilihan barangnya, sistem memungkinkan pembeli melihat kembali barang yang sudah diletakkan di dalam daftar belanja dan melakukan validasi, apakah input dinyatakan benar atau salah: bertipe string untuk nama barang dan int untuk jumlah-harga. Input perlu divalidasi agar kalkulasi harga dapat dijalankan oleh sistem. Sebab, hanya tipe data angka dengan angka yang dapat dioperasi secara matematis. 

Terakhir, sistem mengeluarkan output harga yang harus dibayar. Karena si pengusaha ingin menarik minat pembeli sebanyak mungkin, diberlakukan diskon untuk total nominal tertentu. Oleh karena itu, sistem dimungkinkan juga untuk mensortir total nominal tersebut dan mengeluarkan harga akhir yang harus dibayar sesuai kriteria diskon yang ditawarkan. 

Karena ini adalah kasir online, si pengusaha menugaskan seseorang untuk membuat program kasir self service tersebut dengan bahasa pemrograman Python. Test case yang dibuat untuk menguji program kasir ini mendeskripsikan alur pemesanan seorang konsumen yang ingin membeli buah di Supermarket tersebut. 

## Requirements/Objectives

Tujuan dari pembuatan kasir self service online ini adalah menghasilkan sistem input yang dapat:

A. Merekam nama barang, jumlah, dan harga barang per satuan

B. Mengedit nama, jumlah, dan harga bila input tidak sesuai 

C. Menghapus item tertentu atau semua item yang tidak dibeli 

D. Menampilkan daftar belanja dan mengecek validitas input

E. Menampilkan total pembayaran, baik dengan atau tanpa diskon.


Kasir online ini terbangun dalam lingkup kelas yang dikonstruksi oleh 8 method, yaitu:

1. add_item(nama barang, jumlah barang, harga barang)
Fungsi yang memungkinkan pembeli memasukkan barang yang ingin dibeli, jumlah barang yang diambil, dan harga barang per satuan. 

2. update_item_name(nama barang [lama], nama barang [baru]) 
Fungsi yang memungkinkan pembeli mengganti nama barang, apabila ia merasa salah menginput nama barang. 

3. update_item_qty(nama barang, update jumlah barang)
Fungsi yang memungkinkan pembeli mengganti jumlah barang, jikalau ia merasa jumlah barang yang ia masukkan di awal kurang atau banyak. 

4. update_item_price(nama barang, update harga barang)
Fungsi berikut memungkinkan pembeli mengedit harga barang, sekiranya ia keliru memasukkan harga barang di awal. 

5. delete_item(nama barang)
Fungsi ini memungkinkan pembeli menghapus barang yang tidak jadi ia beli. Ketika nama barang dihapus, item jumlah dan harga juga ikut terhapus. 

6. reset_transaction()
Apabila fungsi di nomor 5 hanya dapat menghapus barang tertentu, fungsi di nomor 6 ini menghapus semua barang sekaligus. 

7. check_order()
Ini adalah fungsi yang menampilkan daftar belanja, lengkap dengan nama, jumlah, harga per item, dan total harga per item. 

8. total_price()
Fungsi ini menginformasikan jumlah uang yang harus dikeluarkan sebagai pembayaran setelah dipotong diskon, apabila sesuai ketentuan. 


## Alur Program/Flowchart

Tentu proses pembelian tidak selalu berjalan berurutan dalam langkah-langkah di atas. Alur yang terjadi dapat saja berlangsung dalam rangkaian yang melompat-lompat. Untuk lebih jelas, simak deskripsi dan flowchart di bawah ini: 

A. Proses pertama yang harus dilalui adalah memasukkan item barang yang ingin dibeli melalui fungsi add_item. Fungsi add_item dapat dipanggil berkali-kali seturut sekian item yang ingin dibeli. Di dalam fungsi add_item diinput parameter nama barang (string), jumlah barang (int), dan harga barang per satuan (int). 

B. Apabila dalam melakukan input terjadi suatu kesalahan, pembeli dapat mengganti nama barang, jumlah barang, dan harga dengan memanggil fungsi update_item_name, update_item_qty, dan update_item_price dengan mengisi parameter masing-masing, sebagaimana yang sudah dijelaskan dalam requirements/objectives di atas. 

C. Namun bisa saja skenario yang terjadi adalah bukan mengganti nama, jumlah, dan harga barang sebagaimana yang ada pada poin B, tetapi memilih untuk tidak menginput barang tersebut. Apabila ini terjadi, dari A pembeli dapat langsung ke C, yaitu memanggil fungsi delete_item untuk menghapus barang tertentu yang tidak jadi diambil atau memanggil fungsi reset_transaction bila ingin menghapus semua barang yang sudah diinput. 


Alur Program Self Service Kasir Online

![Diagram Tanpa Judul drawio (1)](https://github.com/fandisnggarang/python-online-cashier/assets/141505705/233a2101-c02c-4a49-8355-0ae0935c156e)
              

D. Setelah proses memasukkan item barang ke sistem selesai, pembeli dapat mengecek barang apa saja yang sudah dipesan melalui fungsi check_order, sekaligus memeriksa validasi input. Pembeli dapat mengecek pesanannya di fungsi check_order ini tepat setelah proses pemesanan selesai. Dengan kata lain, apa yang ditampilkan di check_order adalah apa yang diproses oleh add_item (A), fungsi update (B), serta hapus daftar barang (C) yang ditaruh pada sebuah list. 

E. Bisa saja setelah memeriksa input di check_order, pembeli merasa ada input yang kurang, sehingga ia perlu menambah, merevisi, atau bahkan menghapus kembali input yang ada. Untuk memenuhi skenario tersebut, pembeli dapat memanggil kembali fungsi di poin A sampai C. Bila sudah yakin dengan input di check_order, maka dari tahap D, pembeli menuju tahap E, yaitu memanggil fungsi total_price untuk mendapatkan harga akhir, dengan atau tanpa diskon. Fungsi total_price akan mengeluarkan harga, apabila input jumlah dan harga barang valid, yaitu bertipe data int. 

F. Bisa saja terjadi, input belum sama sekali dimasukkan dan pembeli secara tidak sengaja salah menekan check_order atau total_price. Apabila skenario ini terjadi, maka sistem akan mengingatkan bahwa kasir belum memiliki daftar barang dan menyarankan pembeli untuk segera menginput item barang. Kondisi ini dibangun agar ketika skenario ini terjadi, program tidak jatuh pada error. 

## Penjelasan Code
Script main.ipynb bertujuan untuk mengeluarkan item pembelian dan menghitung nominal uang yang harus dibayar pembeli, dengan atau tanpa diskon. Ada 8 method dengan fungsi dan tujuannya masing-masing. 

A. Inisialisasi dan penyimpanan nama barang, jumlah, dan harga

Ini adalah fungsi inisialisasi pembuatan objek yang diikuti oleh fungsi penyimpanan nama barang (str), jumlah (int), dan harga (int), di mana ketiganya berlaku sebagai parameter. Fungsi add_item mengembalikan sebuah daftar belanja (dict). 

<img width="600" alt="a" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/1db1f99f-1191-4310-927b-f7373b14583f">

B. Mengedit nama barang bila input sebelumnya tidak sesuai

Ini adalah fungsi untuk mengedit nama barang (str), apabila terjadi kesalahan input nama. Parameter fungsi ini adalah nama barang yang mau diganti dan nama barang yang menggantikan. Fungsi ini mengembalikan daftar belanja (dict). 

<img width="600" alt="b" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/2998f235-c40d-4257-a385-0f4723cb45f9">

C. Mengedit jumlah barang bila input sebelumnya tidak sesuai

Apabila pembeli ingin mengganti jumlah barang (dikurangi atau ditambah), mereka dapat memanggil fungsi ini. Input parameternya adalah nama barang (str) dan jumlah baru (int). Fungsi ini mengembalikan daftar belanja (dict).

<img width="600" alt="c" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/bb4fc55c-f259-46fb-84e7-a3567377d2d8">

D. Mengedit harga barang bila input sebelumnya tidak sesuai

Jika harga barang yang diinput sebelumnya salah, maka pembeli dapat memanggil fungsi berikut. Untuk dapat mengubah input, fungsi ini harus diberi masukan nama barang (str) dan harga baru (int). Fungsi ini mengembalikan daftar belanja (dict).

<img width="600" alt="d" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/c4217cbb-4116-48ee-8ed2-49842ea5e7fa">

E. Menghapus item tertentu yang tidak dibeli 

Fungsi ini dibangun untuk memungkinkan pembeli menghapus item yang sebelumnya sudah diinput. Parameter masukannya adalah nama barang (str). Dengan memanggil fungsi ini, nama barang yang diinput akan hilang dari daftar. Fungsi ini mengembalikan daftar belanja (dict). 

<img width="600" alt="e" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/bdf8b44d-9c29-4866-a8a1-2ce0333d555f">

F. Menghapus semua item yang tidak dibeli 

Apabila fungsi di atas (poin E) ditujukan untuk menghapus barang tertentu, maka fungsi di poin F ini bertujuan untuk menghapus seluruh barang sekaligus. Parameter fungsi ini adalah nama barang (str) dan fungsi ini mengembalikan daftar belanja (dict). 

<img width="600" alt="f" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/acac51ec-6ec6-45ad-b650-d4afe29ce62c">

G. Menampilkan daftar belanja dan mengecek validitas input

Fungsi ini memungkinkan pembeli untuk mengecek kembali seluruh barang yang telah diinput. Fungsi ini mengeluarkan tabel yang berisi nama (str), jumlah (int), harga per item (int), dan total harga (int).

<img width="600" alt="g" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/acd3d9a0-1bbb-442c-b110-84c72aff54fa">

H. Menampilkan total pembayaran, baik dengan atau tanpa diskon.

Fungsi ini menampilkan total harga (int) yang harus dibayar oleh pembeli. Adapun keluaran total harga yang ada dalam fungsi ini akan dimunculkan setelah perhitungan diskon dilakukan. 

<img width="600" alt="h" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/596f608d-6535-418b-8a56-12a8c0765304">

## Hasil Test Case

A. Uji fungsi penyimpanan dan update nama, jumlah, dan harga barang

#input

<img width="600" alt="11" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/1a10d37b-0630-4421-8843-a339f0bccc0e">

#output

<img width="600" alt="1" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/72ab2b79-dd9e-4b1f-b498-f06f87765be4">

B. Uji fungsi hapus (tertentu atau semua), cek order, dan kalkulasi biaya

#input

<img width="600" alt="22" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/1d73fbba-c185-4bfa-af9e-b9ad84205b5c">

#output

<img width="600" alt="2" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/bfd788a5-b369-4800-a6a1-f9af5052e116">

C. Uji fungsi penyimpanan, cek order, dan kalkulasi biaya

#input

<img width="600" alt="33" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/f35a4f23-37ba-49cd-8d10-cb3a159bf234">

#output

<img width="600" alt="3" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/d561a12a-f2d4-48cc-8b73-d9b292dca853">

D. Uji fungsi penyimpanan, cek order, dan kalkulasi biaya
(catatan: pembeli salah memasukkan input jumlah dan harga)

#input

<img width="600" alt="44" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/08c719c2-de5c-4f29-a0a5-bd34595fa121">

#output

<img width="600" alt="4" src="https://github.com/fandisnggarang/python-online-cashier/assets/141505705/faac5d7e-e43e-4df7-be54-a58adaf9038c">


## Conclusion/Future Work

Dari pengerjaan project ini, ada beberapa insight baru yang dapat diimplementasikan untuk menyempurnakan program kasir ini. Pertama adalah mengedit kembali code di main dan membuatnya lebih ringkas. Kedua, melakukan uji coba dengan menempatkan suatu fungsi dalam fungsi lainnya. Yang terpikirkan sekarang adalah menghubungkan fungsi total_price dengan check_order. Ketiga, mempertimbangkan skenario pembeli salah menginput nama barang ketika melakukan update, bukan dalam hal error huruf besar atau kecil, tetapi ketika nama yang diinput benar-benar berbeda (misal: alih-alih 'jeruk' untuk 'Jeruk' yang sudah diantisipasi dengan capitalize(), tetapi 'jeruk' untuk 'semangka'). Keempat, eksplorasi pertahanan kode dengan try dan except.  






