import process, general
import streamlit as st

st.write("# Aplikasi Test Kalimat Bahasa Indonesia")
kalimat = st.text_input("Masukkan Kalimat yang Ingin Diuji")
cek = st.button("Cek")

if cek:
    if general.check_alphabet(kalimat.lower().split()) == False:
        st.info("Kalimat TIDAK VALID karena Terdapat Kata yang Tidak Masuk dalam Bahasa Indonesia")
    elif process.table_filling_process(kalimat.lower().split()) == True:
        st.info("Kalimat DITERIMA karena Sesuai dengan Pola Kalimat Bahasa Indonesia dan Frasa yang Disyaratkan")
    else:
        st.info("Kalimat DITOLAK karena Tidak Sesuai dengan Pola Kalimat Bahasa Indonesia dan Frasa yang Disyaratkan")




# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# window = tk.Tk()

# window.configure(bg="white")
# window.geometry("400x400")
# window.resizable(False, False)
# window.title("Tugas Final Project")

# frame = ttk.Frame(window)
# frame.pack(padx=20, pady=20, fill="x", expand=True)

# label_entry = ttk.Label(frame, text="Masukkan Kalimat Yang Ingin Diuji")
# label_entry.pack(padx=10, fill="x", expand=True)

# kalimat = tk.StringVar()
# entry = ttk.Entry(frame, textvariable=kalimat)
# entry.pack(padx=10, fill="x", expand=True)

# def event():
#     if general.check_alphabet(kalimat.get().lower().split()) == False:
#         showinfo(title="Notifikasi", message="Kalimat TIDAK VALID Karena Terdapat Kata Yang Tidak Masuk Dalam Bahasa Indonesia")
#     elif process.table_filling_process(kalimat.get().lower().split()) == True:
#         showinfo(title="Notifikasi", message="Kalimat DITERIMA Karena Sesuai Dengan Pola Kalimat Bahasa Indonesia Dan Frasa Yang Disyaratkan")
#     else:
#         showinfo(title="Notifikasi", message="Kalimat DITOLAK Karena Tidak Sesuai Dengan Pola Kalimat Bahasa Indonesia Dan Frasa Yang Disyaratkan")

# button = ttk.Button(frame, text="Cek", command=event)
# button.pack(padx=10, pady=10, fill="x", expand=True)

# window.mainloop()