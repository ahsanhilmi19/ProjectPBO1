import sqlite3, time

connection = sqlite3.connect('data.db')


class Pesanan():
    def __init__(self, nama, tanggal, no_meja):
        self.nama = nama
        self.tanggal = tanggal
        self.no_meja = no_meja

    def buat_menu(self):
        global connection
        id_transaksi = None
        status = 0
        connection.execute("INSERT INTO pesanan (id_transaksi, nama, tanggal, no_meja, status) VALUES (?,?,?,?,?)", (id_transaksi, self.nama, self.tanggal, self.no_meja, status))
        connection.commit()

    def update_status(status):
        global connection
        status = 1
        connection.execute("UPDATE pesanan SET status = ? WHERE status = 0", (status))
        connection.commit()

    def sum():
        global connection
        connection.execute("SELECT SUM harga FROM detail_pesanan WHERE id_transaksi = id_transaksi")
        connection.commit()
        
    #def updateTotal(self):
        #global connection
        #connection.execute("SELECT SUM(IF( id_transaksi()")
        #connection.commit()

        

class Detail():
    def __init__(self, id_menu, banyak, harga):
        self.id_menu = id_menu
        self.banyak = banyak
        self.harga = harga

    def detail(self):
        global connection
        id_pesanan = None
        id_trans = connection.cursor().execute("SELECT id_transaksi FROM pesanan WHERE status = 0 ").fetchone()
        id_transaksi = id_trans[0]
        # print(id_transaksi)
         
        connection.execute("INSERT INTO detail_pesanan (id_pesanan, id_transaksi, id_menu, banyak, harga) VALUES (?,?,?,?,?)", (id_pesanan, id_transaksi, self.id_menu, self.banyak, self.harga))
        # connection.execute("INSERT INTO detail_pesanan 
        connection.commit()
    
    
    def update(self,banyak, harga):
        global connection
        connection.execute("UPDATE detail_pesanan SET banyak = ?, harga = ? WHERE id_transaksi = id_transaksi", (self.banyak, self.harga))
        connection.commit()

    def total(self, total):
        global connection
        connection.execute("SELECT (harga * banyak) as total FROM detail_pesanan")
        connection.commit()
        

        
    """
    SELECT SUM(detail_pesanan.harga * detail_pesanan.banyak) FROM pesanan
    """


# while True:
#     print("Pilihan Menu")
#     print("""
#         1. Tambah Transaksi
#         2. Lihat Transaksi
#         3. Ubah Transaksi
#         4. Hapus Transaksi
#         9. Keluar
#     """)
#     pilihan = int(input('Pilihan: '))
    
#     if (pilihan == 1):
        
#         # detail1 = Detail('Masukkan id pilihan') ('Jumlah')
#         # dataMenu()
#         # pesanan1.buat_menu()   
#     elif (pilihan == 9):
#         break
#     else:
#         print('Menu tidak valid!')
