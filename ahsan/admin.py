import sqlite3

from abc import ABC, abstractmethod

connection = sqlite3.connect("data.db")

#USERNAME : agik
#PASSWORD : gantengpol

class Awal (ABC):
    def setting (self, id, username, password) :
        pass
    def database (self):
        pass
    @abstractmethod
    def tambahAkun (self):
        pass
    def getDataAkun (self):
        pass
    def ubahAkun (self):
        pass
    def hapusAkun (self):
        pass
    @abstractmethod
    def ubahAkun(self, id, password) :
        pass

class Admin(Awal):
    def setting(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def tambahAkun(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO admin(id, username, password) VALUES (?, ?, ?)", (self.id, self.username, self.password))
        conn.commit()
        conn.close()

    def getDataAkun(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor().execute("SELECT * FROM admin")
        for row in cursor:
            print (f'{row[0]} {row[1]} {row [2]}')
    
    def ubahAkun(self, id, password):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "UPDATE admin SET id = ?, password = ? WHERE id = ?"
        isian = (id, password, id)
        cursor.execute(query, isian)
        conn.commit()
        conn.close()
        
    def hapusAkun(self, id):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM admin where id = ?", (id))
        conn.commit()
        conn.close()

    def login():
        while True:
            print("=============== LOGIN RESTUKU =================")
            username = input("masukkan username : ")
            password = input("masukkan password : ")
            with sqlite3.connect("data.db") as db:
                cursor = db.cursor()
            admin = ("SELECT * FROM admin WHERE username = ? AND password = ?")
            cursor.execute(admin,[(username),(password)])
            result = cursor.fetchall()

            if result:
                for i in result:
                    print("Welcome ")
                break

            else:
                print("Username dan password salah")
                again = input("coba lagi? (y/n) : ")
                if again.lower() == "n":
                    print("okay")
                    break

    login()    
menu1 = Admin()

while True:
    print("================= RESTUKU ==================")
    print("""
        1. Lihat Akun
        2. Tambah Akun
        3. Ubah Akun
        4. Hapus Akun
        5. Daftar Menu
        9. Keluar
    """)
    pilihan = int(input('### Pilihan: '))

    if (pilihan == 1):
        menu1.getDataAkun()
    elif (pilihan == 2):
        menu1.getDataAkun()
        menu1.setting (input("ID Baru :"), input("Username Baru : "), input("Password Baru : "))
        menu1.tambahAkun()
        print("-------------- AKUN ---------------")
        menu1.getDataAkun ()
    elif (pilihan == 3):
        menu1.getDataAkun()
        menu1.ubahAkun (input("masukkan ID yang akan diubah : "), input("masukkan password baru : "))
    elif (pilihan == 4):
        menu1.getDataAkun()
        menu1.hapusAkun (input("masukkan id yang akan dihapus : "))
    elif (pilihan == 5):
        from main import Menu
    elif (pilihan == 9):
        break
    else:
        print('Menu tidak valid!')
