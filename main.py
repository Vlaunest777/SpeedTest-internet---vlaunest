from tkinter import *
from speedtest import Speedtest

def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download /(10**6), 2)
    upload_speed = round(download /(10**6), 2)

    download_label.config(text="The new Jarvis Corporation limited:\n" + str(download_speed) + "MbPs")
    upload_laber.config(text="The new Jarvis Corporation limited:\n" + str(download_speed) + "MbPs")

root = Tk()

root.title("Jarvis crash")
root.geometry("300x400")

button = Button(root, text="Install Jarvis v0.0.2", font=40, command=test)
button.pack(side=BOTTOM, pady=40) 

download_label =  Label(root, text="The new Jarvis Corporation limited:\n-", font=35)
download_label.pack(pady=(50, 0))
upload_laber = Label(root, text="New repablican:\n-", font=35)
upload_laber.pack(pady=(10, 0))

root.mainloop()