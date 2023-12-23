#from pytube import YouTube
#from sys import argv
#
##0 es el nombre del programa. 1 es la primera línea.
#link = argv[1]
#yt = YouTube(link)
#
#print("Título: ", yt.title)
#print("Vistas: ", yt.views)
#
#yd = yt.streams.get_audio_only()
#yd.download('F:\PyProjects\Pytube\Audio')
import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from threading import Thread
from sys import argv

def get_video_info():
    link = url_entry.get()
    try:
        yt = YouTube(link)
        title_label.config(text="Título: " + yt.title)
        views_label.config(text="Vistas: " + str(yt.views))
        status_label.config(text=":)")
    except Exception as e:
        status_label.config(text="Error: " + str(e))

def download_audio():
    link = url_entry.get()
    try:
        yt = YouTube(link)
        title_label.config(text="Título: " + yt.title)
        views_label.config(text="Vistas: " + str(yt.views))

        yd = yt.streams.get_audio_only()

        # Get the current working directory
        current_directory = os.getcwd()

        # Use the current directory as the download folder
        download_folder = os.path.join(current_directory, 'Audio')

        # Create the download folder if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)

        yd.download(download_folder)

        status_label.config(text="Descarga terminada :)")
    except Exception as e:
        status_label.config(text="Error: " + str(e))


def start_info_thread():
    info_thread = Thread(target=get_video_info)
    info_thread.start()

def start_download_thread():
    download_thread = Thread(target=download_audio)
    download_thread.start()

#GUI
root = tk.Tk()
root.title("Descarga de audio")

url_label = tk.Label(root, text="Pegar URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

url_entry = tk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

info_button = tk.Button(root, text="Ver info del video", command=start_info_thread)
info_button.grid(row=1, column=0, pady=10)

start_button = tk.Button(root, text="Descargar", command=start_download_thread)
start_button.grid(row=1, column=1, pady=10)

title_label = tk.Label(root, text="Título:")
title_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

views_label = tk.Label(root, text="Vistas:")
views_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

root.mainloop()
