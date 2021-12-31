# coding: utf-8

import get_playlist
import To_spotify
from tkinter import *

def main():
    netEast_key=NetEast_key.get()
    netEast_password=NetEast_password.get()
    s_key=Spotify_key.get()
    s_password=Spotify_password.get()

    url=get_playlist.get_web(netEast_key,netEast_password)
    true_url=url.replace('/#','')
    get_playlist.main(true_url)
    To_spotify.main(s_key,s_password)

root = Tk()
root.title("xxxskrt snitch program")
root.geometry('588x600')

label1=Label(root,text='phone number',font=14).place(x=40, y=60)

NetEast_key=Entry(root,width=30,font=14)
NetEast_key.place(x=200,y=60)

label2=Label(root,text='NetEast password',font=14).place(x=40,y=100)

NetEast_password=Entry(root,width=30,font=14)
NetEast_password.place(x=200,y=100)

label3=Label(root,text='Spotify key',font=14).place(x=40,y=140)

Spotify_key=Entry(root,width=30,font=14)
Spotify_key.place(x=200, y=140)

label4=Label(root,text='Spotify password',font=14).place(x=40,y=200)

Spotify_password=Entry(root,width=30,font=14)
Spotify_password.place(x=200,y=200)

button_start=Button(root,text='start synchronize', font=('Calibri',15), command=main)
button_start.place(x=0,y=500)

button_exit=Button(root,text='exit', font=('Calibri',15), command=root.quit)
button_exit.place(x=400,y=500)

root.mainloop()
