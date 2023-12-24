import tkinter
import customtkinter
from pytube import YouTube


def iniciarDescarga():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        audio.download()
        finishLabel.configure(text="Descarga terminada", text_color="green")
    except:
        finishLabel.configure(text="El enlace no es válido", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    porcentaje_completado = bytes_downloaded / total_size * 100
    per = str(int(porcentaje_completado))
    pPorcentaje.configure(text=per + ' %')
    pPorcentaje.update()

    barraProgreso.set(float(porcentaje_completado) / 100)


# Ajustes
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Estilo
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Audio Descarga")

# UI
title = customtkinter.CTkLabel(app, text="Pegar enlace de YouTube")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Barra de progreso
pPorcentaje = customtkinter.CTkLabel(app, text="0 %")
pPorcentaje.pack()

barraProgreso = customtkinter.CTkProgressBar(app, width=400)
barraProgreso.set(0)
barraProgreso.pack(padx=10, pady=10)

# Botón de descarga
descarga = customtkinter.CTkButton(app, text="Descargar", command=iniciarDescarga)
descarga.pack(padx=10, pady=10)

# Esto ejecuta el programa
app.mainloop()
