from tkinter import *
from pytube import YouTube
from pytube.cli import on_progress

# Initialize tkinter


root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Youtube Video Downloader")

# Label Header


Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

# Create field to enter youtube link


link = StringVar()
Label(root, text="Paste link here: ", font="arial 15 bold").place(x=32, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# Define download function


def downloader():
    url = YouTube(str(link.get()), on_progress_callback=on_progress)
    video = url.streams.first()
    print("Downloading...")
    video.download()
    Label(root, text="VIDEO DOWNLOADED!", font="arial 15",
          fg="green").place(x=140, y=210)

# Define stop function


def cancel():
    root.destroy()


# Buttons
Button(root, text="DOWNLOAD", font="arial 15 bold", bg="pale green",
       padx=2, command=downloader).place(x=100, y=150)
Button(root, text="CANCEL", font="arial 15 bold", bg="pale violet red",
       padx=2, command=cancel).place(x=260, y=150)

root.mainloop()

# Find the downloaded video in the folder/path where you run this python script
