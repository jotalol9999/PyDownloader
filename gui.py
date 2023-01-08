import PySimpleGUI as sg
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\jlagu\Downloads\pygui\build\assets\frame0")

path= "./"



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    print(percentage_of_completion)
    while percentage_of_completion < 100:

        if percentage_of_completion == 100:
            msg = "Se ha descargado" + video.title 
            sg.popup_ok(str(msg))



def def_path ():
    path = sg.popup_get_folder("Selecciona una carpeta")
    return path
def video():

    link = sg.popup_get_text("Ingrese el link")
    yt=YouTube(link,on_progress_callback=on_progress)
    #print("Title: ", yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download(path)

def playlist():
    link = sg.popup_get_text("Ingrese el link")
    p = Playlist(link)
    play_name = sg.popup_get_text("Ingrese el nombre con el que sera guardada la Playlist")
    play_path = str ( path+ (play_name))
    """"f2 = open(play_path,"w") 
    f2.close()"""
    total = len(p)
    dir = os.path.join(path,play_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
    contador = 0
    print(f'Downloading: {p.title}')
    for video in p.videos:
        contador = contador +1

        print(f'Downloading: {video.title} ' + str(contador)+'/' +str(total))
        video.streams.first().download(play_path)
       # msg = "Se ha descargado " + video.title
       # sg.PopupAutoClose(str(msg))
        

    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    430.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

canvas.create_rectangle(
    646.9999999999999,
    152.0,
    822.9999999999999,
    202.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=video,
    relief="flat"
)
button_1.place(
    x=501.9999999999999,
    y=152.0,
    width=116.0,
    height=50.0
)

canvas.create_text(
    86.99999999999989,
    32.00000000000001,
    anchor="nw",
    text="Youtube Downloader",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    501.9999999999999,
    46.00000000000001,
    anchor="nw",
    text="Seleccione el tipo ",
    fill="#505485",
    font=("Roboto Bold", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    629.4999999999999,
    90.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=480.9999999999999,
    y=76.0,
    width=297.0,
    height=26.0
)

canvas.create_text(
    1.9999999999998863,
    0.0,
    anchor="nw",
    text="By: Jota\n",
    fill="#FCFCFC",
    font=("ArchivoRoman Regular", 24 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=def_path,
    relief="flat"
)
button_2.place(
    x=439.9999999999999,
    y=157.0,
    width=42.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("PLaylist.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=playlist,
    relief="flat"
)
button_3.place(
    x=645.9999999999999,
    y=152.0,
    width=180.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
