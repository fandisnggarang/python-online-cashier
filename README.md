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

![jadi](https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/ccac309d-55d9-4ef7-a81e-75ed4553de72)
              

D. Setelah proses memasukkan item barang ke sistem selesai, pembeli dapat mengecek barang apa saja yang sudah dipesan melalui fungsi check_order, sekaligus memeriksa validasi input. Pembeli dapat mengecek pesanannya di fungsi check_order ini tepat setelah proses pemesanan selesai. Dengan kata lain, apa yang ditampilkan di check_order adalah apa yang diproses oleh add_item (A), fungsi update (B), serta hapus daftar barang (C) yang ditaruh pada sebuah list. 

E. Bisa saja setelah memeriksa input di check_order, pembeli merasa ada input yang kurang, sehingga ia perlu menambah, merevisi, atau bahkan menghapus kembali input yang ada. Untuk memenuhi skenario tersebut, pembeli dapat memanggil kembali fungsi di poin A sampai C. Bila sudah yakin dengan input di check_order, maka dari tahap D, pembeli menuju tahap E, yaitu memanggil fungsi total_price untuk mendapatkan harga akhir, dengan atau tanpa diskon. Fungsi total_price akan mengeluarkan harga, apabila input jumlah dan harga barang valid, yaitu bertipe data int. 

F. Bisa saja terjadi, input belum sama sekali dimasukkan dan pembeli secara tidak sengaja salah menekan check_order atau total_price. Apabila skenario ini terjadi, maka sistem akan mengingatkan bahwa kasir belum memiliki daftar barang dan menyarankan pembeli untuk segera menginput item barang. Kondisi ini dibangun agar ketika skenario ini terjadi, program tidak jatuh pada error. 

## Penjelasan Code
Script main.ipynb bertujuan untuk mengeluarkan item pembelian dan menghitung nominal uang yang harus dibayar pembeli, dengan atau tanpa diskon. Ada 8 method dengan fungsi dan tujuannya masing-masing. 

A. Inisialisasi dan penyimpanan nama barang, jumlah, dan harga

Ini adalah fungsi inisialisasi pembuatan objek yang diikuti oleh fungsi penyimpanan nama barang (str), jumlah (int), dan harga (int), di mana ketiganya berlaku sebagai parameter. Fungsi ini mengembalikan sebuah daftar belanja (dict). 

<img width="331" alt="1" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/f48cb50d-4196-4907-b45f-147f9c2aeb20">

B. Mengedit nama barang bila input sebelumnya tidak sesuai

Ini adalah fungsi untuk mengedit nama barang (str), apabila terjadi kesalahan input nama. Parameter fungsi ini adalah nama barang yang mau diganti dan nama barang yang menggantikan. Fungsi ini mengembalikan daftar belanja (dict). 

<img width="331" alt="2" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/fd4d32a4-608b-405e-a8c3-9efa060f7f3e">

C. Mengedit jumlah barang bila input sebelumnya tidak sesuai

Apabila pembeli ingin mengganti jumlah barang (dikurangi atau ditambah), mereka dapat memanggil fungsi ini. Input parameternya adalah nama barang (str) dan jumlah baru (int). Fungsi ini mengembalikan daftar belanja (dict). 

<img width="329" alt="3" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/25bf8f40-7d7f-4c38-af95-b644ac65713f">

D. Mengedit harga barang bila input sebelumnya tidak sesuai

Jika harga barang yang diinput sebelumnya salah, maka pembeli dapat memanggil fungsi berikut. Untuk dapat mengubah input, fungsi ini harus diberi masukan nama barang (str) dan harga baru (int). Fungsi ini mengembalikan daftar belanja (dict). 

<img width="331" alt="4" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/b9c6d08c-9cbd-48f4-8d7a-8c8f5195d6a3">

E. Menghapus item tertentu yang tidak dibeli 

Fungsi ini dibangun untuk memungkinkan pembeli menghapus item yang sebelumnya sudah diinput. Parameter masukannya adalah nama barang (str). Dengan memanggil fungsi ini, nama barang yang diinput akan hilang dari daftar. Fungsi ini mengembalikan daftar belanja (dict). 

<img width="331" alt="5" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/0b91ce1a-811e-4721-9842-71c8f7c48c17">

F. Menghapus semua item yang tidak dibeli 

Apabila fungsi di atas (poin E) ditujukan untuk menghapus barang tertentu, maka fungsi di poin F ini bertujuan untuk menghapus seluruh barang sekaligus. Parameter fungsi ini adalah nama barang (str) dan fungsi ini mengembalikan daftar belanja (dict). 

<img width="331" alt="6" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/1d6f625b-57d3-4697-bc8c-5ebd2dfaaaac">

G. Menampilkan daftar belanja dan mengecek validitas input

Fungsi ini memungkinkan pembeli untuk mengecek kembali seluruh barang yang telah diinput. Fungsi ini mengeluarkan tabel yang berisi nama (str), jumlah (int), harga per item (int), dan total harga (int).

<img width="329" alt="7" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/8dadee8b-2de1-4bf5-8641-5cf2c44cbef9">

H. Menampilkan total pembayaran, baik dengan atau tanpa diskon.

Fungsi ini menampilkan total harga (int) yang harus dibayar oleh pembeli. Adapun keluaran total harga yang ada dalam fungsi ini akan dimunculkan setelah perhitungan diskon dilakukan. 

<img width="329" alt="8" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/45a6c1b3-8bff-4fa4-98da-14e09b2d1e60">

## Hasil Test Case

A. Penyimpanan nama, jumlah, dan harga barang

#input

<img width="413" alt="1_!" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/628501c1-57e4-4409-873b-3c71b19c9b35">

#output

<img width="506" alt="1a" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/c8429739-e11e-420e-9149-59b841b1e2a8">


B. Peng-update-an nama barang

#input

<img width="415" alt="2" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/b1c8a5b0-ed94-4047-8060-ec71dadb3178">

#output

<img width="453" alt="2b" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/053f9069-5d1f-4b94-9c9d-6f471e3fae74">


C. Peng-update-an jumlah barang

#input

<img width="410" alt="5" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/2b5d7444-cf43-4abb-91d5-a93b5f333206">

#output

<img width="460" alt="2" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/cee918aa-4bd8-4400-b2bb-e604b47f2cb5">


D. Peng-update-an harga barang 

#input

<img width="415" alt="3" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/5476f214-d8ae-4b3a-b3c8-65aead894f74">

#output

<img width="484" alt="33" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/be6f7751-d226-4e36-abb4-19124bcfb594">


E. Penghapusan item tertentu 

#input

<img width="415" alt="6" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/19b621ac-e173-4f6a-aa1d-76cf00e8ce34">

#output

<img width="443" alt="6a" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/955f2c5e-ec3a-40aa-b674-a481745d37f7">


F. Penghapusan semua item 

#input

<img width="413" alt="7" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/46d99253-7f8b-4d9c-9727-17a8018035a8">

#output

<img width="435" alt="7a" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/568ac956-d44b-4a40-b8d4-c5b61ec5da37">


G. Input - Output daftar belanja

#input

<img width="416" alt="8" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/a58efe92-3ce7-44e0-954a-48de63c709f6">

#output

<img width="472" alt="1" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/3338e242-87b8-4941-872e-c386d0429201">


H. Input - Output total pembayaran (dapat diskon, jika sesuai syarat)

#input

<img width="421" alt="1234" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/d3bcf1cd-d15c-4dbf-9a27-ce2fcb00d23b">

#output

<img width="526" alt="2" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/b4ac4533-ff24-4c9c-a7bd-b2f017afbeed">


I. Penyimpanan nama, jumlah, dan harga barang

#input

<img width="370" alt="3" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/695bb69e-e661-4ef1-acc1-3aa663741bc6">

#output

<img width="539" alt="4" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/469ef3f2-a11a-4ea1-8737-66c2b49f16d0">


J. Input - Output daftar belanja

#input

<img width="371" alt="a" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/f295091e-9b9e-41ac-89b7-e11ac520c42a">

#output

<img width="378" alt="aa" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/1cb102a2-2ca1-4c9f-b644-1fe3653415d2">


K. Input - Output total pembayaran (dapat diskon, jika sesuai syarat)

#input

<img width="368" alt="b" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/e54e05e5-377f-4127-b34b-a3927d3eed75">

#output

<img width="391" alt="bb" src="https://github.com/fandisnggarang/python-project-selfservice-cashier/assets/141505705/cfaf3a49-91b2-4b39-a410-6ea9c8819ebb">




## Conclusion/Future Work

Dari pengerjaan project ini, ada beberapa insight baru yang dapat diimplementasikan untuk menyempurnakan program kasir ini. Pertama adalah mengedit kembali code di main dan membuatnya lebih ringkas. Kedua, melakukan uji coba dengan menempatkan suatu fungsi dalam fungsi lainnya. Yang terpikirkan sekarang adalah menghubungkan fungsi total_price dengan check_order. Ketiga, mempertimbangkan skenario pembeli salah menginput nama barang ketika melakukan update, bukan dalam hal error huruf besar atau kecil, tetapi ketika nama yang diinput benar-benar berbeda (misal: alih-alih 'jeruk' untuk 'Jeruk' yang sudah diantisipasi dengan capitalize(), tetapi 'jeruk' untuk 'semangka'). Keempat, eksplorasi pertahanan kode dengan try dan except.  






