import tkinter as tk
from tkinter.filedialog import askdirectory
from pytube import YouTube
from tkinter import messagebox

window = tk.Tk()
# create title
window.title("Youtube Downloader")

# set size for the app
window.minsize(width=550, height=400)
window.resizable(width=False, height=False)


def widgets():
    # create link label
    link_label = tk.Label(window, text="Video Link")
    link_label.grid(row=0, column=0, padx=30, pady=30)
    link_label.config(font=("None", 15), fg="Blue")

    # create an input for link
    link_input = tk.Entry(window, width=40, textvariable=video_link)
    link_input.grid(row=0, column=1)

    # create location for saving video
    place_label = tk.Label(window, text="Location")
    place_label.grid(row=1, column=0)
    place_label.config(font=("None", 15), fg="Blue")

    # create an input for that location
    place_input = tk.Entry(window, width=30, textvariable=download_dir)
    place_input.grid(row=1, column=1, sticky="W")

    # create open file button
    place_btn = tk.Button(window, text="open", width=10, bg="blue", fg="black", command=browse)
    place_btn.grid(row=1, column=2)

    # download button 480
    download_btn_480 = tk.Button(window, text="Download 480p Now", command=download480)
    download_btn_480.grid(row=2, column=1, padx=0, pady=30)
    download_btn_480.config(height=2, width=20, bg="green", fg="black")

    # download button 720
    download_btn_720 = tk.Button(window, text="Download 720p Now", command=download720)
    download_btn_720.grid(row=3, column=1, padx=0, pady=20)
    download_btn_720.config(height=2, width=25, bg="green", fg="black")

    # download button high resolution
    download_btn_720 = tk.Button(window, text="Download high resolution Now", command=download_highest_resolution)
    download_btn_720.grid(row=4, column=1, padx=0, pady=20)
    download_btn_720.config(height=2, width=30, bg="green", fg="black")


# file explore function
def browse():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH", title="save")
    download_dir.set(directory)


# download functions
def download720():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(res="720p").first().download(save_dir)
    messagebox.showinfo(title="Success", message="Your video was downloaded successfully ! ")


def download480():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(res="480p").first().download(save_dir)
    messagebox.showinfo(title="Success", message="Your video was downloaded successfully ! ")


def download_highest_resolution():
    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(save_dir)
    messagebox.showinfo(title="Success", message="Your video was downloaded successfully ! ")


# -------------------
download_dir = tk.StringVar()
video_link = tk.StringVar()

widgets()

window.mainloop()
