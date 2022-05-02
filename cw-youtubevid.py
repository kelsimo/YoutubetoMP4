from tkinter import *
from pytube import YouTube
win = Tk()
win.geometry("500x300")
win.config(bg="red")
win.resizable(0,0)

def download():
   url = YouTube(str(link.get()))
   video = url.streams.get_highest_resolution()
   #video = url.streams.first() will get the first quality video
   video.download()
   Label(win, text ="Your video has downloaded.").place(x=10, y=140)

Label(win, text="Download a video!", font="Arial 24 bold", fg="red", bg="white").place(x=10, y=50)

link = StringVar()

linkentry = Entry(win, width=25, textvariable=link, font='Century 16 bold', bg="black", fg="white", justify="center").place(x=10, y=100)

button1 = Button(win, text = "Click to Download", bg="white", fg="red", command=download).place(x=380, y=100)

lb1= Label(win, text="name").grid(row=1, column=1, padx=10)

win.mainloop()
