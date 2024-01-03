import tkinter
import customtkinter
from pytube import YouTube

# links to check 1 min videolink: "https://www.youtube.com/watch?v=zBjJUV-lzHo"
# "https://www.youtube.com/watch?v=UwvAMkH9tTU&t=358s"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def onprogress(stream, chunk, bytes_remaining):
    totalsize = stream.filesize
    bytes_downloaded = totalsize-bytes_remaining
    percentage = bytes_downloaded/totalsize * 100
    ppercentage.configure(text = f"{percentage}%")
    ppercentage.update()
    progressbar.set(float(percentage/100))


def dojob():
    try:
        yt_video_link = link.get()
        yt = YouTube(yt_video_link, on_progress_callback=onprogress)
        label.configure(text = f"Title: {yt.title}" , text_color = "white")
        present_res = []
        stream_videos = yt.streams.filter(res = ["240p","360p", "480p", "720p", "1080p"], progressive=True)
    except:
        label.configure(text = "Type url correctly" , text_color = "red")

    def dwnld240():
        stream_videos.get_by_resolution("240p").download()
        label.configure(text = "Downloaded...!", text_color = "green")
    def dwnld360():
        stream_videos.get_by_resolution("360p").download()
        label.configure(text = "Downloaded...!", text_color = "green")
    def dwnld720():
        stream_videos.get_by_resolution("720p").download()
        label.configure(text = "Downloaded...!", text_color = "green")
    def dwnld1080():
        stream_videos.get_by_resolution("1080p").download()
        label.configure(text = "Downloaded...!", text_color = "green")

    for i in stream_videos:
        present_res.append(i.resolution)
    
    if "240p" in present_res:
        button0 = customtkinter.CTkButton(app, text= "Download 240p", width=250, command=dwnld240)
        button0.pack()
    if "360p" in present_res:
        button1 = customtkinter.CTkButton(app, text= "Download 360p", width=250, command=dwnld360)
        button1.pack()
    if "720p" in present_res:
        button2 = customtkinter.CTkButton(app, text= "Download 720p", width=250, command=dwnld720)
        button2.pack()
    if "1080p" in present_res:
        button3 = customtkinter.CTkButton(app, text= "Download 1080p", width=250, command=dwnld1080)
        button3.pack()



app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube-Downloader")


title = customtkinter.CTkLabel(app, text = "Insert a youtube link ")
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

label = customtkinter.CTkLabel(app, text = "")
label.pack()


ppercentage = customtkinter.CTkLabel(app, text = "0%")
ppercentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx = 10, pady = 5)

download = customtkinter.CTkButton(app, text = "Check", command=dojob)
download.pack(padx = 10, pady = 5)


app.mainloop()

