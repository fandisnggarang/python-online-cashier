
# TEST CASE

from cashier import Transaction

"""
Berikut adalah beberapa test_case sesuai permintaan soal. Test case dibangun menurut skenario yang mungkin
terjadi ketika seorang pembeli melakukan input pesanannya. Penguji juga dapat mencoba kapasitas program dengan
mengganti tipe data item jumlah dan item harga dari int ke str.
"""

user_1 = Transaction()

# pilih barang yang ingin dibeli ('Mau beli apa, ya?')
pilih_barang = user_1.add_item('Mangga', 35, 7000)
pilih_barang = user_1.add_item('Jeruk', 25, 8000)
pilih_barang = user_1.add_item('Semangka', 15, 10000)
pilih_barang = user_1.add_item('Apel', 20, 9000)
print(f'Item yang dibeli adalah: {pilih_barang}')

# ganti nama barang ('Oh bukan yang itu, tapi yang ini')
ganti_nama_barang = user_1.update_item_name('Semangka', 'Kelapa')
print(ganti_nama_barang)

# ganti jumlah barang ('ga jadi deh, jumlahnya dikurangin ah')
ganti_jumlah_barang = user_1.update_item_qty('Mangga', 12)
print(ganti_jumlah_barang)

# ganti harga barang ('waduh salah masukkan item harga nih')
ganti_harga_barang = user_1.update_item_price('Jeruk', 5_000)
print(ganti_harga_barang)

# hapus nama barang ('hm, apa betul aku butuh mangga?')
hapus_nama_barang = user_1.delete_item('Mangga')
print(hapus_nama_barang)

# hapus semua barang ('hm. buahnya dipesan sekarang, gak ya?')
hapus_semua_barang = user_1.reset_transaction()
print(hapus_nama_barang)

# cek barang pesanan (tiba-tiba pesan lagi tapi salah menu)
cek_pesanan = user_1.check_order()
print(cek_pesanan)

# tampilkan harga akhir (tiba-tiba pesan lagi tapi salah menu)
tampilkan_harga = user_1.total_price()
print(tampilkan_harga)

# pilih barang yang ingin dibeli ('hm yang tadi dibeli sekarang aja deh')
pilih_barang = user_1.add_item('Nangka', 35, 7_000)
pilih_barang = user_1.add_item('Lemon', 25, 8_000)
pilih_barang = user_1.add_item('Jambu', 15, 10_000)
pilih_barang = user_1.add_item('Durian', 20, 9_000)
print(f'Item yang dibeli adalah: {pilih_barang}')

# cek pesanan buah ('cek pesanan dulu ah. Mau pesan apa lagi, ya?')
cek_pesanan = user_1.check_order()
print(cek_pesanan)


# tampilkan harga akhir ('kayaknya udah pas. Berapa ya total harganya?')
tampilkan_harga = user_1.total_price()
print(tampilkan_harga)