def Databarang(data_barang_new,nama,stok): 
    data_barang_new[nama] = stok
    print('Data Barang Berhasil Ditambahkan')

def HapusData( data_barang_new,nama):
    if  nama in data_barang_new:
            del  data_barang_new[nama]
            print("Data barang telah dihapus.")
    else:
        print("Data barang tidak ditemukan.")

def show_data(data_barang_new):
   if not  data_barang_new:
        print("Data Barang Kosong")
   else:
        for index, data_barang_new in enumerate( data_barang_new):
             print(f"{index+1}. Nama: { data_barang_new['nama'], 'Stok': { data_barang_new['stok']}}")

def cari_data_barang( data_barang_new,nama):
    if nama in  data_barang_new:
        return nama,  data_barang_new[nama]
    else:
        return None
    
def edit_data( data_barang_new, nama, stok_baru):
    if nama in  data_barang_new:
       data_barang_new[nama] = stok_baru
       print(f"Stok barang '{nama}' telah diperbarui menjadi {stok_baru}.")
    else:
        print(f"Barang '{nama}' tidak ditemukan.")

def jumlah_data( data_barang_new):
    return len( data_barang_new)

def menu():
    data_barang_new={}
    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data ")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")
        pilihan = input("Masukan Pilihan Menu : ")

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            stok = input("Masukkan stok barang: ")
            Databarang(data_barang_new,nama,stok)
        elif pilihan == "2":
            indeks = int(input("Masukkan indeks data yang akan diedit: "))
            nama_baru = input("Masukkan nama baru: ")
            stok_baru = int(input("Masukkan stok baru: "))
            edit_data(indeks, nama_baru, stok_baru)
            print("Data barang berhasil diedit.")
        elif pilihan == "3":
            jumlah = jumlah_data()
            print(f"Jumlah data barang: {jumlah}")
        elif pilihan == "4":
            nama = input("Masukkan nama barang yang akan dihapus: ")
            HapusData(data_barang_new,nama)
        elif pilihan == "5":
            show_data()
        elif pilihan == "6":
            nama = input("Masukkan nama barang yang dicari: ")
            cari_data_barang(nama)
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")