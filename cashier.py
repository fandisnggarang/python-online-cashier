from tabulate import tabulate

class Transaction:

  # inisialisasi list yang menyimpan daftar belanja
  def __init__(self):
    self.shopping_list = {}

  # method yang memungkinkan user untuk memasukkan item belanja
  def add_item(self, item_name, item_qty, price_per_item):
    """
    Fungsi tempat user memasukkan item belanja

    Parameters
    ---------
    item_name: string
      input nama barang
    item_qty: int
      input jumlah barang
    price_per_item: int
      input harga barang

    Returns
    ---------
    shopping_list: dict
      daftar belanja
    """
    self.shopping_list[item_name.capitalize()] = [item_qty, price_per_item]

    """
    capitalize() dipakai untuk mengubah semua input berbentuk string ke dalam konstruksi kata berhuruf kapital awal.
    Ini diperlukan agar error tidak tercipta ketika pembeli melakukan input string dengan format huruf yang berbeda
    dalam fungsi-fungsi update di bawah ini.
    """

    return self.shopping_list

  # method yang memungkinkan user mengganti (nama) barang belanja
  def update_item_name(self, item_name, updated_name):
    """
    Fungsi tempat user mengganti (nama) barang

    Parameters
    ---------
    item_name: string
      input (nama) barang lama
    updated_name: string
      input (nama) barang baru

    Returns
    ---------
    shopping_list: dict
      daftar belanja
    """
    for key in self.shopping_list.keys():
      if key == item_name.capitalize():
        self.shopping_list[updated_name.capitalize()] = self.shopping_list[key]
        print('-------')
        print('Update Item Name :')
        print(f'Item {item_name.capitalize()} diganti {updated_name.capitalize()}')
        del self.shopping_list[key]
        return self.shopping_list

  # method yang memungkinkan user mengganti jumlah barang belanja
  def update_item_qty(self, item_name, updated_item_qty):
    """
    Fungsi tempat user mengganti jumlah barang

    Parameters
    ---------
    item_name: string
      input nama barang
    updated_item_qty: int
      input jumlah (baru) barang

    Returns
    ---------
    shopping_list: dict
      daftar belanja
    """
    for key, value in self.shopping_list.items():
      if key == item_name.capitalize():
        value[0] = updated_item_qty
    print('-------')
    print('Update Item Qty :')
    print(f'Jumlah {item_name.capitalize()} diubah menjadi {updated_item_qty}')
    return self.shopping_list

  # method yang memungkinkan user mengganti harga barang belanja
  def update_item_price(self, item_name, updated_price_per_item):
    """
    Fungsi tempat user mengganti harga barang

    Parameters
    ---------
    item_name: string
      input nama barang
    updated_price_per_item: int
      input harga (baru) barang

    Returns
    ---------
    shopping_list: dict
      daftar belanja
    """
    for key, value in self.shopping_list.items():
      if key == item_name.capitalize():
        value[1] = updated_price_per_item
    print('-------')
    print('Update Item Price :')
    print(f'Harga {item_name.capitalize()} diubah menjadi Rp. {updated_price_per_item} per item')
    return self.shopping_list

  # method yang memungkinkan user menghapus item belanja satu per satu
  def delete_item(self, item_name):
    """
    Fungsi tempat user menghapus barang satu per satu

    Parameters
    ---------
    item_name: string
      input nama barang

    Returns
    ---------
    shopping_list: dict
      daftar belanja
    """
    del self.shopping_list[item_name.capitalize()]
    print('-------')
    print('Update Item Deleted :')
    print(f'{item_name.capitalize()} dihapus dari daftar')
    return self.shopping_list


  # method yang memungkinkan user menghapus item belanja sekaligus
  def reset_transaction(self):
    """
    Fungsi tempat user menghapus semua barang sekaligus

    Returns
    ---------
    clear_all_items: dict
      daftar kosong
    """
    clear_all_items = self.shopping_list.clear()
    print('-------')
    print('Update Reset List :')
    print(f'Item-item barang berhasil dihapus')
    return clear_all_items

  # method yang memungkinkan user melihat semua item belanja yang sudah dipesan
  def check_order(self):
    """
    Fungsi yang menampilkan semua item belanja yang sudah dipesan

    Returns
    ---------
    tabel: tabulate
      daftar belanja
    """
    self.shopping_list_2 = {}

    """
    Kondisi if-else di bawah ini ditujukan untuk memeriksa apakah pembeli sudah melakukan input item barang atau belum.
    Apabila keranjang sudah diisi barang pesanan, sistem akan lanjutkan proses validasi dan memunculkan tabel.

    Kalau pembeli belum lakukan input, sistem akan ingatkan bahwa keranjang masih kosong. Kondisi ini dibangun agar
    bila pembeli panggil check_order setelah reset_transaction atau sebelum lakukan add_item, error tidak muncul.

    Dengan kata lain, untuk memunculkan kembali tabel pada check_order, pembeli harus menginput kembali item barang.
    Ini juga sekaligus sebagai syarat bagi kalkulasi harga dalam fungsi total_price.
    """

    if len(self.shopping_list) == 0:

      print('-------')
      print('Update Order Lists :')
      print('Daftar belanja kosong. Silakan input item belanja!')

    else:
      for key, value in self.shopping_list.items():
        self.shopping_list_2[key] = tuple(value)

        """
        self.shopping_list_2 mengambil data dict (key, values) dari self.shopping_list, dibentuk untuk menampung value
        bertipe data tuple, yang dipakai untuk memudahkan proses penyimpanan key, value dalam tabulate.
        """

      tables  = []
      for idx, (key, value) in enumerate(self.shopping_list_2.items(), start = 1):
        if type(value[0]) != int or type(value[1]) != int:
          print('-------')
          print(f'Terdapat kesalahan input data {idx, key, value}. Harap input data dengan benar')
        else:
          total_price = value[0] * value[1]
          self.shopping_list_2[key] = (idx, value[0], value[1], total_price)
          tables.append((idx, key, value[0], value[1], total_price))
      headers = ['Nomor', 'Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
      tabel   = tabulate(tables, headers, tablefmt='grid')
      print('-------')
      print('Update Order Lists :')
      validation = 'Input barang, jumlah, dan harga yang dimasukkan sudah benar!'
      print(validation)
      return tabel


  # method yang memungkinkan user menerima harga total belanja
  def total_price(self):
    """
    Fungsi yang menampilkan harga total belanja setelah melewati validasi input
    dan persyaratan diskon

    Returns
    ---------
    final_price: int
      (stored in info_on_price variable)
      total harga yang harus dibayar
    """

    bag_of_prices = [ ]

    """
    # kondisi if-else berikut ditujukan untuk mengecek, apakah daftar item sudah diinput atau belum. Apabila item belum
    diinput dan pembeli sudah menekan total_price, maka sistem akan ingatkan pembeli untuk melakukan input terlebih dahulu.
    """

    if len(self.shopping_list) == 0:
      print('-------')
      print('Update Final Price :')
      print('Daftar belanja kosong. Total harga tidak dapat dihitung. Silakan input item barang!')
      print('-------')
    else:
      for value in self.shopping_list.values():
        if type(value[0]) == int and type(value[1]) == int:
          bag_of_prices.append(value[0] * value[1])
          if sum(bag_of_prices) > 500_000:
            diskon = 0.10
            final_price = sum(bag_of_prices) - (sum(bag_of_prices) * diskon)
          elif sum(bag_of_prices) > 300_000:
            diskon = 0.08
            final_price = sum(bag_of_prices) - (sum(bag_of_prices) * diskon)
          elif sum(bag_of_prices) > 200_000:
            diskon = 0.05
            final_price = sum(bag_of_prices) - (sum(bag_of_prices) * diskon)
          else:
            final_price = sum(bag_of_prices)
          info_on_price = f'Total harga barang yang harus dibayar: Rp. {round(final_price)}'
        else:
          info_on_price = 'Total harga tidak dapat dihitung. Harap memasukkan data dengan benar'
      print('-------')
      print('Update Final Price :')
      return info_on_price
