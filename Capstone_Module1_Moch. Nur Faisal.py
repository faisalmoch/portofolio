#Capstone Module 1 Project, Moch. Nur Faisal

from prettytable import PrettyTable
#Def Functions

#fungsi untuk melihat tabel seluruh data
def show_seluruh_data():
    table = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Item Terjual", "Harga Modal"])
    for i in range(len(list_barang)):
        table.add_row([list_barang[i][0],list_barang[i][1],list_barang[i][2],list_barang[i][3],list_barang[i][4],list_barang[i][5],list_barang[i][6]])
    print(table)

#fungsi untuk melihat tabel data yang dipilih
def show_selected_data():
    primary_key = int(input('''
        Masukan ID Barang yang Dicari: '''))
    for i in range(len(list_barang)):
        if list_barang[i][0] == primary_key:
                table = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Item Terjual", "Harga Modal"])
                table.add_row([list_barang[i][0],list_barang[i][1],list_barang[i][2],list_barang[i][3],list_barang[i][4],list_barang[i][5],list_barang[i][6]])
                print(table)
                break
    else:
        print("\n")
        print("Data Tidak Tersedia")

#fungi untuk menambahkan data
def menambah_data():
    primary_key = int(input("Masukan ID Barang: "))
    for i in range(len(list_barang)):
            if list_barang[i][0] == primary_key:
                print("Data Sudah Tersedia")
                break
    else:
        nama_barang = input("Masukan Nama Item: ")
        kategori = input("Masukan Kategori Item: ")
        stock = int(input("Masukan Stock Item: "))
        harga_jual = int(input("Masukan Harga Jual Barang: "))
        jumlah_pembelian = int(input("Masukan Jumlah Item Terjual: "))
        harga_modal = int(input("Masukan Harga Modal: "))
        print("\n")
        save = input("Save Data? (Y/N)").upper()
        if save == "Y":
            list_barang.append([primary_key, nama_barang, kategori, stock, harga_jual, jumlah_pembelian, harga_modal])  
            print("Data Berhasil Disimpan")
            return 
        else:
            return 

#fungsi untuk merubah data
def merubah_data():
    primary_key = int(input("Masukan ID Barang: "))
    for i in range(len(list_barang)):
            if list_barang[i][0] == primary_key:
                table = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Item Terjual", "Harga Modal"])
                table.add_row([list_barang[i][0],list_barang[i][1],list_barang[i][2],list_barang[i][3],list_barang[i][4],list_barang[i][5],list_barang[i][6]])
                print(table)
                print("\n")
                update = input(" Lanjutkan Update? (Y/N): ").upper()
                if update == "Y":
                    nama_barang = input("Masukan Nama Item: ")
                    kategori = input("Masukan Kategori Item: ")
                    stock = int(input("Masukan Stock Item: "))
                    harga_jual = int(input("Masukan Harga Jual Barang: "))
                    jumlah_pembelian = int(input("Masukan Jumlah Item Terjual: "))
                    harga_modal = int(input("Masukan Harga Modal: "))
                    list_barang[i][0] = primary_key
                    list_barang[i][1] = nama_barang
                    list_barang[i][2] = kategori
                    list_barang[i][3] = stock
                    list_barang[i][4] = harga_jual
                    list_barang[i][5] = jumlah_pembelian
                    list_barang[i][6] = harga_modal
                    break
                elif update == "N":
                    print("Perubahan Data Dibatalkan")
                    break
                else:
                    return

    else:
        print("\n")
        print("Data Tidak Tersedia")
        return 

#fungsi untuk menghapus data  
def menghapus_data():
    primary_key = int(input("Masukan ID Barang: "))
    for i in range(len(list_barang)):
            if list_barang[i][0] == primary_key:
                index = i
                table = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Item Terjual", "Harga Modal"])
                table.add_row([list_barang[i][0],list_barang[i][1],list_barang[i][2],list_barang[i][3],list_barang[i][4],list_barang[i][5],list_barang[i][6]])
                print(table)
                print("\n")
                hapus_data = input(f"Apakah Data Inventory ID {primary_key} Akan Dihapus? (Y/N) ").upper()
                if hapus_data == "Y":
                    del list_barang[index]
                    print("Data Berhasil Dihapus")
                    break
                elif hapus_data == "N":
                    print("Data Batal DIhapus")
                    break
                else:
                    print("Input Tidak Valid")
                    break
    else:
        print("\n")
        print("Data Tidak Tersedia")

#fungsi untuk melakukan sorting data
def sort_data():
    sort = (input('''
        1. Sort berdasarkan stock
        2. Sort berdasarkan harga jual
        3. Sort berdasarkan jumlah item terjual
        4. Sort berdasarkan harga modal
        Silahkan Pilih Sub Menu Create Data (1-4): '''))
    if sort == "1":
        index = 3
    elif sort == "2":
        index = 4
    elif sort == "3":
        index = 5
    elif sort == "4":
        index = 6
    else:
        print("Submenu yang anda input tidak valid")
        return 
    asc_desc = input("Urutkan dari nilai terbesar? (Y/N)").upper()
    if asc_desc == "Y":
        rank_list_barang = list_barang.copy()
        n = len(rank_list_barang)
        for i in range(n):
            for j in range(0, n-i-1):
                if rank_list_barang[j][index] < rank_list_barang[j+1][index]:
                    rank_list_barang[j], rank_list_barang[j+1] = rank_list_barang[j+1], rank_list_barang[j]
        tablerank = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Order", "Harga Modal"])
        for i in range(len(rank_list_barang)):
            tablerank.add_row([rank_list_barang[i][0],rank_list_barang[i][1],rank_list_barang[i][2],rank_list_barang[i][3],rank_list_barang[i][4],rank_list_barang[i][5],rank_list_barang[i][6]])
        print(tablerank)
    elif asc_desc == "N":
        rank_list_barang = list_barang.copy()
        n = len(rank_list_barang)
        for i in range(n):
            for j in range(0, n-i-1):
                if rank_list_barang[j][index] > rank_list_barang[j+1][index]:
                    rank_list_barang[j], rank_list_barang[j+1] = rank_list_barang[j+1], rank_list_barang[j]
        tablerank = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Order", "Harga Modal"])
        for i in range(len(rank_list_barang)):
            tablerank.add_row([rank_list_barang[i][0],rank_list_barang[i][1],rank_list_barang[i][2],rank_list_barang[i][3],rank_list_barang[i][4],rank_list_barang[i][5],rank_list_barang[i][6]])
        print(tablerank)

#fungsi untuk mencari profit dari tiap item di inventory
def data_profit():
    list_profit = list_barang.copy()
    for i in range(len(list_barang)):
        profit = (list_barang[i][4]-list_barang[i][6])*list_barang[i][5]
        list_barang[i].append(profit)
    tablerank = PrettyTable(["ID Item", "Nama Item", "Kategori Item", "Stock","Harga Jual", "Jumlah Item Terjual", "Harga Modal", "Profit"])
    for i in range(len(list_profit)):
        tablerank.add_row([list_profit[i][0],list_profit[i][1],list_profit[i][2],list_profit[i][3],list_profit[i][4],list_profit[i][5],list_profit[i][6],list_profit[i][7]])
    print(tablerank)

#fungi untuk mencari biaya yang dibutuhkan untuk melakukan restock barang sesuai jumlah yang dicari 
def harga_stock():
    primary_key = int(input("Masukan ID Barang: "))
    for i in range(len(list_barang)):
        if list_barang[i][0] == primary_key:
            index = i
            jumlah_stock = int(input(f"Masukan Jumlah Stock Item {list_barang[i][1]} yang Akan Dibeli: "))
            harga_stock = jumlah_stock*list_barang[i][6]
            print(f"Jumlah Harga yang Perlu Dibayarkan untuk Restock Item {list_barang[i][1]} sebanyak {jumlah_stock} adalah Rp.{harga_stock}")
            break
    else:
        print("\n")
        print("Data Tidak Tersedia")
        return

#Data
list_barang = [[101, "Popsodent", "Toiletries", 100, 10000, 50, 8000],
               [102, "Lofeboy", "Toiletries", 150, 15000, 70, 12000],
               [103, "Punten", "Toiletries", 120, 20000, 40, 15000],
               [104, "Chatoti", "Makanan", 500, 8000, 250, 5000],
               [105, "Tenggo", "Makanan", 400, 10000, 150, 8000],
               [106, "Ponari Sweat", "Makanan", 200, 6000, 80, 4000]]

#Program

while(True):
    pilihan_menu = input('''
Selamat datang program data barang Toko Selalu Makmur:
List Menu:
1. Menampilkan daftar inventory
2. Menambah data inventory
3. Merubah data inventory
4. Menghapus data inventory
5. Sorting data
6. Analisa data
7. Keluar

Masukan angka menu yang anda pilih (1-7): ''')
    if(pilihan_menu == "1"):
        while(True):
            try:
                pilihan_submenu = input('''
                    1. Menampilkan Seluruh Data
                    2. Menampilkan Data Tertentu
                    3. Kembali ke Menu
                    Masukan angka sub menu yang anda pilih (1-3): ''')
                if(pilihan_submenu == "1"):
                    if len(list_barang) != 0:
                        show_seluruh_data()
                    else:
                        print("Data Tidak Tersedia")
                        continue
                elif(pilihan_submenu == "2"):
                    if len(list_barang) != 0:
                        show_selected_data()
                    else:
                        print("Data Tidak Tersedia")
                        continue
                elif(pilihan_submenu == "3"):
                    break
                else:
                    print("Submenu yang Anda Masukan Tidak Valid")
                    continue
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    elif(pilihan_menu == "2"):
        while(True):
            try:
                print("Menambahkan Data Inventory")
                pilihan_submenu = input('''
                        1. Tambah Data Inventory
                        2. Kembali ke Menu Utama
                        Silahkan Pilih Sub Menu Create Data: ''')
                if(pilihan_submenu == "1"):
                    menambah_data()       
                elif(pilihan_submenu == "2"):
                    break
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    elif(pilihan_menu == "3"):
        while(True):
            try:
                print("Merubah Data Inventory")
                pilihan_submenu = input('''
                        1. Merubah Data Inventory
                        2. Kembali ke Menu Utama
                        Silahkan Pilih Sub Menu Create Data: ''')
                if(pilihan_submenu == "1"):
                    merubah_data()
                elif(pilihan_submenu == "2"):
                    break
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    elif(pilihan_menu == "4"):
        while(True):
            try:
                print("Menghapus Data Inventory")
                pilihan_submenu = input('''
                        1. Menghapus Data Inventory
                        2. Kembali ke Menu Utama
                        Silahkan Pilih Sub Menu Delete Data: ''')
                if(pilihan_submenu == "1"):
                    menghapus_data()
                elif(pilihan_submenu == "2"):
                    break
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    
    elif(pilihan_menu == "5"):
        while(True):
            try:
                pilihan_submenu = input('''
                    1. Sort data inventory
                    2. Kembali ke Menu
                    Masukan angka sub menu yang anda pilih (1-2): ''')
                if(pilihan_submenu == "1"):
                    sort_data()
                elif (pilihan_submenu == "2"):
                    break
                else:
                    print("Submenu yang Anda Masukan Tidak Valid")
                    continue
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    elif(pilihan_menu == "6"):
         while(True):
            try:
                print("Analisa Data")
                pilihan_submenu = input('''
                        1. Data Profit Tiap Item 
                        2. Biaya untuk Stock Barang
                        3. Kembali ke Menu
                        Silahkan Pilih Sub Menu Analisa Data: ''')
                if(pilihan_submenu == "1"):
                    data_profit()
                elif(pilihan_submenu == "2"):
                    harga_stock()
                elif (pilihan_submenu == "3"):
                    break
            except:
                print("\n")
                print("Data yang Dimasukan Tidak Valid")
    elif(pilihan_menu == "7"):
        break
    else:
        print("Menu yang Anda Pilih Tidak Valid")
        continue