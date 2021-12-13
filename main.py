import requests
import tkinter as tk

def getNews():
    api_key="78d0f3812c7045f7975309d0f6fd42ed"
    url = "https://newsapi.org/v2/top-headlines?country=India&apikey="+api_key
    news= requests.get(url).json()



canvas= tk.TK()
canvas.geometry("900x600")
canvas.title("My News App")

button=tk.button(canvas,font=24,text="Reload",command ="getNews")
button.pack(pady =20)

label = tk.label(canvas, font=18,justify="left")
label.pack(pady=20)

