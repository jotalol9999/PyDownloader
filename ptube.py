from pytube import YouTube
import PySimpleGUI as sg
from pytube.cli import on_progress
import tkinter as Tk
from tkinter import *
from pytube import Playlist
path = "alo"
Ventana = Tk()
Ventana.geometry("500x500")
Ventana.title("Mi interfaz")
def def_path ():
    path = sg.popup_get_folder("Selecciona una carpeta")
    return path
def video():
    def_path


    link = sg.popup_get_text("Ingrese el link")
    yt=YouTube(link,on_progress_callback=on_progress)
    #print("Title: ", yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download(path)





L1 =Label(Ventana,text="Ingresa la moneda",font="BW.TLabel")
L1.place(x = 180, y = 15)



B1 = Button(Ventana,text="Video")
B1.place(x=150,y=40)

B2 = Button(Ventana,text="Lista de Reproducción")
B2.place(x=300,y= 40)


B3 = Button(Ventana,text="Carpeta destino",command=def_path)
B3.place(x=0,y= 40)


Ventana.mainloop()