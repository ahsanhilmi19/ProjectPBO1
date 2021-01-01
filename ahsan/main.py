import sqlite3
from pesanan import *

from abc import ABC, abstractmethod

connection = sqlite3.connect("data.db")

class Akhir (ABC):
    def setting (self, id_menu, nama_menu, harga) :
        pass
    def database (self):
        pass
    @abstractmethod
    def tambahMenu (self):
        pass
    def getDataMenu (self):
        pass
    def ubahMenu (self):
        pass
    def hapusMenu (self):
        pass
    @abstractmethod
    def ubahMenu(self, id_menu, nama_menu, harga) :
        pass

class Menu(Akhir):
    def setting(self, id_menu, nama_menu, harga) :
        self.id_menu = id_menu
        self.nama_menu = nama_menu
        self.harga = harga
    
    def tambahMenu(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu(id_menu, nama_menu, harga) VALUES (?, ?, ?)", (self.id_menu, self.nama_menu, self.harga))
        conn.commit()
        conn.close()

    def getDataMenu(self):
        cursor = connection.cursor().execute("SELECT * FROM menu")
        for row in cursor:
            print (f'{row[0]} {row[1]} {row [2]}')
    
    def ubahMenu(self, id_menu, nama_menu, harga):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "UPDATE menu SET id_menu = ?, nama_menu = ?, harga = ? WHERE id_menu = ?"
        isian = (id_menu, nama_menu, harga, id_menu)
        cursor.execute(query, isian)
        conn.commit()
        conn.close()
        
    def hapusMenu(self, id_menu):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu where id_menu = ?", (id_menu))
        conn.commit()
        conn.close()
 
menu2 = Menu()

while True:
        print("================= MENU RESTUKU ==================")
        print("""
            1. Lihat Menu
            2. Tambah Menu
            3. Ubah Menu
            4. Hapus Menu
            5. Pesan Menu (PESANAN)
            6. Atur Akun
            9. Keluar
        """)
        pilihan = int(input('### Pilihan: '))

        if (pilihan == 1):
            menu2.getDataMenu()
        elif (pilihan == 2):
            menu2.getDataMenu()
            menu2.setting (input("ID Menu Baru :"), input("Nama Menu : "), input("Harga Menu : "))
            menu2.tambahMenu()
            print("-------------- MENU ---------------")
            menu2.getDataMenu ()
        elif (pilihan == 3):
            menu2.getDataMenu()
            menu2.ubahMenu (input("masukkan ID yang akan diubah : "), input("Nama menu : "), input("harga menu : "))
        elif (pilihan == 4):
            menu2.getDataMenu()
            menu2.hapusMenu(input("masukkan id yang akan dihapus : "))
        elif (pilihan == 5):
            print("-------------- DATA PELANGGAN ---------------")
            nama =  input('Nama Customer: ')
            tanggal = input('Tanggal: ')
            no_meja = input('No Meja: ')
            pesanan1 = Pesanan(nama, tanggal, no_meja)
            pesanan1.buat_menu()
            
            while True:
                print("-------------- PILIH MENU ---------------")
                menu2.getDataMenu()
                id = input('### Pilih Id Menu: ')
                banyak = int(input('Masukkan banyak: '))
                price = connection.cursor().execute("SELECT harga FROM menu WHERE id_menu ="+id+"").fetchone()
                total = price[0]
                harga = (banyak * total)
                print(harga)
                detail1 = Detail(id, banyak, harga) 
                id_pesan = connection.cursor().execute("SELECT id_transaksi FROM pesanan WHERE status = 0").fetchone()
                id_pesanan = str(id_pesan[0])
                print(id_pesanan)
                cek_id = connection.cursor().execute("SELECT * FROM detail_pesanan WHERE id_menu ="+id+" AND id_transaksi ="+id_pesanan+"").fetchall()
                
                if cek_id == []:
                    detail1.detail()  
                else:
                    detail1.update(banyak, harga)
                print("Lanjut(1)/Selesai(2)")
                pilih = int(input('masukan pilih: '))
                if pilih == 1:
                    pass
                else:
                    cursor = connection.cursor().execute("SELECT * FROM pesanan ORDER BY id_transaksi DESC LIMIT 1") 
                    for row in cursor:
                        print ("-------------- STRUK PEMESANAN ---------------")
                        print ('nama             : ', row[1], '\n''tanggal          : ', row[2], '\n''no meja          : ', row[3])
                    cursor = connection.cursor().execute("SELECT detail_pesanan.id_menu, detail_pesanan.harga, menu.nama_menu, menu.harga FROM detail_pesanan INNER JOIN menu ON detail_pesanan.id_menu = menu.id_menu ORDER BY id_pesanan DESC LIMIT 1")
                    for row in cursor:
                        print ('total pembayaran : ',row[1])
                    #cursor = connection.cursor().execute("SELECT detail_pesanan.id_menu, detail_pesanan.harga, detail_pesanan.banyak, menu.nama_menu, menu.harga FROM detail_pesanan INNER JOIN menu ON detail_pesanan.id_menu = menu.id_menu ORDER BY id_transaksi DESC LIMIT 1")
                    #for row in cursor:
                        #print (row)
                    break


#SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

            # from pesanan import Pesanan
            #MENU
        elif (pilihan == 6):
            from admin import Admin
        elif (pilihan == 9):
            break
        else:
            print('Menu tidak valid!')
