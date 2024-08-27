import customtkinter as ctk
from customtkinter import *
import sqlite3

# Membuat aplikasi utama
app = ctk.CTk()
app.geometry("1920x1080")
set_appearance_mode("dark")

# Koneksi ke SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT)''')

# Fungsi validasi untuk memastikan hanya angka yang bisa diinput
def only_numbers(input):
    return input.isdigit() or input == ""

# Registrasi validasi
validate_numeric = app.register(only_numbers)

# Fungsi untuk menyimpan data dan menghitung prediksi
def simpan_data():
    # Mengambil nilai dari input user
    nama_value = nama.get()
    nilai_biologi_value = int(biologi.get())
    nilai_fisika_value = int(fisika.get())
    nilai_inggris_value = int(inggris.get())

    # Menentukan prediksi fakultas berdasarkan nilai tertinggi
    if nilai_biologi_value > nilai_fisika_value and nilai_biologi_value > nilai_inggris_value:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika_value > nilai_biologi_value and nilai_fisika_value > nilai_inggris_value:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris_value > nilai_biologi_value and nilai_inggris_value > nilai_fisika_value:
        prediksi_fakultas = "Bahasa"
    elif nilai_biologi_value == nilai_fisika_value and nilai_biologi_value > nilai_inggris_value:
        prediksi_fakultas = "Kedokteran atau Teknik"
    elif nilai_biologi_value == nilai_inggris_value and nilai_biologi_value > nilai_fisika_value:
        prediksi_fakultas = "Kedokteran atau Bahasa"
    elif nilai_fisika_value == nilai_inggris_value and nilai_fisika_value > nilai_biologi_value:
        prediksi_fakultas = "Teknik atau Bahasa"
    else:
        prediksi_fakultas = "Anda terlalu pintar"  # Jika ada nilai yang sama besar

    # Menyimpan data ke database
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_value, nilai_biologi_value, nilai_fisika_value, nilai_inggris_value, prediksi_fakultas))
    conn.commit()

    # Menampilkan hasil prediksi
    hasil_label.configure(text=f"{prediksi_fakultas}")

# Membuat frame
frame1 = CTkFrame(master=app, fg_color="#0C356A", height=100, width=1200, corner_radius=15)
frame1.pack(fill="both", expand=True)
frame1.place(relx=0.5, rely=0.08, anchor="center")

frame2 = CTkFrame(master=app, fg_color="#0C356A", height=150, width=720, corner_radius=15)
frame2.pack(fill="both", expand=True)
frame2.place(relx=0.345, rely=0.27, anchor="center")

frame3 = CTkFrame(master=app, fg_color="#0C356A", height=440, width=720, corner_radius=15)
frame3.pack(fill="both", expand=True)
frame3.place(relx=0.345, rely=0.68, anchor="center")

frame4 = CTkFrame(master=app, fg_color="#0C356A", height=623, width=450, corner_radius=15)
frame4.pack(fill="both", expand=True)
frame4.place(relx=0.742, rely=0.57, anchor="center")

# Label judul aplikasi
label = CTkLabel(master=frame1, text="Path2Faculty", font=("Gilroy-ExtraBold", 40), text_color="#FFFFFF")
label.place(relx=0.5, rely=0.5, anchor="center")

# Input nama siswa
nama_label = CTkLabel(master=frame2, text="Masukan Nama Anda:", font=("Gilroy-SemiBold", 28), text_color="#FFF0CE")
nama_label.place(relx=0.5, rely=0.35, anchor="center")

nama = CTkEntry(master=frame2, font=("Gilroy-Regular", 16), height=37.5, width=600, text_color="#FFFFFF", border_color="#FFF0CE", border_width=2)
nama.place(relx=0.5, rely=0.65, anchor="center")

# Label Masukan Nilai Mata Pelajaran
subjudul = CTkLabel(master=frame3, text="Masukan Nilai Mata Pelajaran", font=("Gilroy-Bold", 28), text_color="#FFF0CE")
subjudul.place(relx=0.5, rely=0.12, anchor="center")

# Input nilai mata pelajaran Biologi
biologi_label = CTkLabel(master=frame3, text="Biologi", font=("Gilroy-SemiBold", 24), text_color="#FFF0CE")
biologi_label.place(relx=0.5, rely=0.26, anchor="center")

biologi = CTkEntry(master=frame3, font=("Gilroy-Regular", 14), height=35, width=200, text_color="#FFFFFF", border_color="#FFF0CE", border_width=2, validate="key", 
                   validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
biologi.place(relx=0.5, rely=0.35, anchor="center")

# Input nilai mata pelajaran Fisika
fisika_label = CTkLabel(master=frame3, text="Fisika", font=("Gilroy-SemiBold", 24), text_color="#FFF0CE")
fisika_label.place(relx=0.5, rely=0.48, anchor="center")

fisika = CTkEntry(master=frame3, font=("Gilroy-Regular", 14), height=35, width=200, text_color="#FFFFFF", border_color="#FFF0CE", border_width=2, validate="key", 
                  validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
fisika.place(relx=0.5, rely=0.57, anchor="center")

# Input nilai mata pelajaran Bahasa Inggris
inggris_label = CTkLabel(master=frame3, text="Bahasa Inggris", font=("Gilroy-SemiBold", 24), text_color="#FFF0CE")
inggris_label.place(relx=0.5, rely=0.70, anchor="center")

inggris = CTkEntry(master=frame3, font=("Gilroy-Regular", 14), height=35, width=200, text_color="#FFFFFF", border_color="#FFF0CE", border_width=2, validate="key", 
                   validatecommand=(validate_numeric, '%P'))  # Validasi input hanya angka
inggris.place(relx=0.5, rely=0.79, anchor="center")

#subjudul hasil
subjudul2 = CTkLabel(master=frame4, text="Fakultas", font=("Gilroy-Bold", 28), text_color="#FFF0CE")
subjudul2.place(relx=0.5, rely=0.1, anchor="center")

# Label hasil
hasil_label = CTkLabel(master=frame4, text="", font=("Gilroy-Bold", 40), text_color="#FFFFFF")
hasil_label.place(relx=0.5, rely=0.5, anchor="center")

# Button prediksi
button = CTkButton(master=frame4, text="Prediksi Sekarang", text_color="#0C356A", font=("Gilroy-SemiBold", 16), fg_color="#FFC436", height=40, width=400, 
                   corner_radius=8, hover_color="#f99107", border_color="#FFF0CE", border_width=2, command=simpan_data)
button.place(relx=0.5, rely=0.92, anchor="center")

# Menjalankan aplikasi
app.mainloop()

# Menutup koneksi database saat aplikasi selesai dijalankan
conn.close()
