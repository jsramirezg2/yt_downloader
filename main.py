from pytube import YouTube
import os
from tkinter import *
from customtkinter import *
from time import sleep


# ------------------------------------------ |
# ----------functions & variables----------- |
# ------------------------------------------ |
set_default_color_theme("green")


def yt_video_download(url, download_type, loading_message):

    loading_message.set("downloading content")
    root.update_idletasks()

    yt = YouTube(url)

    if download_type == "audio":

        video = yt.streams.get_audio_only()

    elif download_type == "video":

        video = yt.streams.get_highest_resolution()

    output_video = video.download()

    if download_type == "audio":
        fileName, ext = os.path.splitext(output_video)
        new_file = fileName + '.mp3'
        os.rename(output_video, new_file)

    loading_message.set("download completed")
    root.update_idletasks()
    sleep(2)

    loading_message.set("")


# ------------------------------------------ |
# -------------window and UI---------------- |
# ------------------------------------------ |
root = CTk()
root.title("yt downloader")


title = CTkLabel(root, text="Youtube video downloader",
                 text_font=("Roboto", 22))
title.pack(pady=45)

url_str = StringVar()
url_input = CTkEntry(root, width=350, textvariable=url_str)
url_input.pack()


switch_var = StringVar(value="video")
convert_audio = CTkSwitch(root, text="Download mp3", variable=switch_var,
                          offvalue="video", onvalue="audio")
convert_audio.pack(pady=20)


loading_message = StringVar()
loading_label = CTkLabel(root, textvariable=loading_message)
loading_label.pack()


download_button = CTkButton(
    root, text="Download", command=lambda: yt_video_download(url_str.get(), switch_var.get(), loading_message))

download_button.pack()

root.mainloop()
