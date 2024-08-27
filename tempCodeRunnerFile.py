import customtkinter as ctk
from customtkinter import *
import sqlite3

# Membuat aplikasi utama
app = ctk.CTk()
app.geometry("1080x720")
set_appearance_mode("dark")

# Koneksi ke SQLite
conn = sqlite3.connect('prodi.db')
cursor = conn.cursor()

# Membuat tabel prodi jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS prodi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matematika INTEGER,
    bahasa_inggris INTEGER,
    geografi INTEGER,
    prediksi TEXT)''')

# Fungsi validasi untuk memastikan hanya angka yang bisa diinput
def only_numbers(input):
    return input.isdigit() or input == ""

# Registrasi validasi
validate_numeric = app.register(only_numbers)

# Fungsi untuk menyimpan data dan menghitung prediksi
def simpan_data():
    # Mengambil nilai dari input user
    nilai_matematika = int(matematika.get())
    nilai_bahasa_inggris = int(bahasa_inggris.get())
    nilai_geografi = int(geografi.get())

    # Menentukan prediksi prodi berdasarkan nilai tertinggi
    if nilai_matematika > nilai_bahasa_inggris and nilai_matematika > nilai_geografi:
        prediksi_prodi = "Teknik"
    elif nilai_bahasa_inggris > nilai_matematika and nilai_bahasa_inggris > nilai_geografi:
        prediksi_prodi = "Bahasa"
    elif nilai_geografi > nilai_matematika and nilai_geografi > nilai_bahasa_inggris:
        prediksi_prodi = "Geografi"
    elif nilai_matematika == nilai_bahasa_inggris and nilai_matematika == nilai_geografi:
        prediksi_prodi = "Teknik atau Bahasa"
    elif nilai_matematika == nilai_geografi and nilai_matematika == nilai_bahasa_inggris:
        prediksi_prodi = "Teknik atau Geografi"
    elif nilai_bahasa_inggris == nilai_geografi and nilai_bahasa_inggris == nilai_matematika:
        prediksi_prodi = "Bahasa atau Geografi"
    else:
        prediksi_prodi = "Anda terlalu pintar"  # Jika ada nilai yang sama besar

    # Menyimpan data ke database
    cursor.execute("INSERT INTO prodi (matematika, bahasa_inggris, geografi, prediksi) VALUES (?, ?, ?, ?)",
                   (nilai_matematika, nilai_bahasa_inggris, nilai_geografi, prediksi_prodi))
    conn.commit()

    # Menampilkan hasil prediksi
    hasil_label.configure(text=f"{prediksi_prodi}")

# Membuat frame
frame1 = CTkFrame(master=app, fg_color="#0C356A", height=70, width=1200, corner_radius=15)
frame1.pack(expand=True)
frame1.place(relx=0.5, rely=0.08, anchor="center")

frame2 = CTkFrame(master=app, fg_color="#0C356A", height=640, width=720, corner_radius=15)
frame2.pack(expand=True)
frame2.place(relx=0.345, rely=0.55, anchor="center")

frame3 = CTkFrame(master=app, fg_color="#0C356A", height=640, width=450, corner_radius=15)
frame3.pack(expand=True)
frame3.place(relx=0.742, rely=0.55, anchor="center")

# Label judul aplikasi
label = CTkLabel(master=frame1, text="Prediksi Prodi", font=("Gilroy-ExtraBold", 40), text_color="#FFFFFF")
label.place(relx=0.5, rely=0.5, anchor="center")

# Label Masukan Nilai Mata Pelajaran
subjudul = CTkLabel(master=frame2, text="Masukan Nilai Mata Pelajaran", font=("Gilroy-Bold", 36), text_color="#FFFFFF")
subjudul.place(relx=0.5, rely=0.1, anchor="center")

# Input nilai mata pelajaran Matematika
matematika_label = CTkLabel(master=frame2, text="Matematika", font=("Gilroy-SemiBold", 28), text_color="#FFFFFF")
matematika_label.place(relx=0.19, rely=0.29, anchor="w")

matematika = CTkEntry(master=frame2, font=("Gilroy-Regular", 14), height=35, width=400, text_color="#FFFFFF",
                      border_color="#FFFFFF", border_width=2, validate="key", 
                      validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
matematika.place(relx=0.19, rely=0.36, anchor="w")

# Input nilai mata pelajaran Bahasa Inggris
bahasa_inggris_label = CTkLabel(master=frame2, text="Bahasa Inggris", font=("Gilroy-SemiBold", 28), text_color="#FFFFFF")
bahasa_inggris_label.place(relx=0.19, rely=0.465, anchor="w")

bahasa_inggris = CTkEntry(master=frame2, font=("Gilroy-Regular", 14), height=35, width=400, text_color="#FFFFFF",
                          border_color="#FFFFFF", border_width=2, validate="key", 
                          validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
bahasa_inggris.place(relx=0.19, rely=0.535, anchor="w")

# Input nilai mata pelajaran Geografi
geografi_label = CTkLabel(master=frame2, text="Geografi", font=("Gilroy-SemiBold", 28), text_color="#FFFFFF")
geografi_label.place(relx=0.19, rely=0.65, anchor="w")

geografi = CTkEntry(master=frame2, font=("Gilroy-Regular", 14), height=35, width=400, text_color="#FFFFFF",
                    border_color="#FFFFFF", border_width=2, validate="key", 
                    validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
geografi.place(relx=0.19, rely=0.72, anchor="w")

#subjudul hasil
subjudul2 = CTkLabel(master=frame3, text="Prediksi Prodi", font=("Gilroy-Bold", 36), text_color="#FFFFFF")
subjudul2.place(relx=0.5, rely=0.1, anchor="center")

# Label hasil
hasil_label = CTkLabel(master=frame3, text="", font=("Gilroy-Bold", 40), text_color="#FFFFFF")
hasil_label.place(relx=0.5, rely=0.5, anchor="center")

# Button prediksi
button = CTkButton(master=frame3, text="Prediksi Sekarang", text_color="#0C356A",
                   font=("Gilroy-SemiBold", 16), fg_color="#FFC436", height=40, width=400, 
                   corner_radius=8, hover_color="#f99107",
                   border_color="#FFF0CE", border_width=2, command=simpan_data)
button.place(relx=0.5, rely=0.92, anchor="center")

# Menjalankan aplikasi
app.mainloop()

# Menutup koneksi database saat aplikasi selesai dijalankan
conn.close()
