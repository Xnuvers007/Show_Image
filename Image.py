from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
import requests
from io import BytesIO
import os

print('''
code by Xnuvers007
name = dispay show image with tkinter
version = 1.0.0
using python 3.9x
coding in Windows 10 Pro and Kali Linux Terminal
Tidak terima Recode kecuali jika izin untuk mengembangkannya dan menaruh nama saya di codingan tersebut
''')

def ulang():
    root = tk.Tk()
    root.title("Show Image")
    icon = Image.open('Kanao.jpeg')
    foto = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(False, foto)
    try:
        print("Contoh : https://hdwallpaperim.com/wp-content/uploads/2017/08/22/81312-Angel_Beats-Tachibana_Kanade.jpg\nAtau dengan cara mengcopy link image\n")
        img_url = input("Masukan Link gambar : ")
    #For Example = "https://hdwallpaperim.com/wp-content/uploads/2017/08/22/81312-Angel_Beats-Tachibana_Kanade.jpg"
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        panel = tk.Label(root, image=img)
        panel.pack(side="bottom",fill="both", expand="yes")
        root.mainloop()
    except (OSError, KeyboardInterrupt, ValueError):
        print("Link Tidak ada / Gambar tidak tersedia")
        print("Akan Mengulang dalam 3 Detik")
        for i in range (1,4):
            i += 0
            print (i)
            time.sleep(0.5)
        ulang()
    #################

ulang()
