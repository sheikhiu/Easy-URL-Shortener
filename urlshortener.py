import pyshorteners
import tkinter as tk
from tkinter import messagebox
import webbrowser



shortener = pyshorteners.Shortener()

#This method shortens the URL using pyshorteners
def URLshort():
    x=pyshorteners.Shortener()
    a=x.tinyurl.short(entry.get())
    shortened.insert(0, a)


#start of the GUI window
window=tk.Tk()

#label of the GUI
window.title("Easy URL Shortener")
window.geometry("450x450")

label = tk.Label(text="What's the URL you want to shorten: ")
entry = tk.Entry()
shortened = tk.Entry()


bottomlabel = tk.Label(text = "This is the shortened URL: ")
label.pack(padx=10, pady=10)
entry.pack(padx=10, pady=10)

bottom=tk.Button(text="Click to shorten the Url",command=URLshort, padx=10, pady=10).pack()

bottomlabel.pack(padx=10, pady=10)
shortened.pack(padx=20,pady=20)

image = tk.PhotoImage(file="linkz.png")
imageput= tk.Label(image=image,padx=50,pady=50)
imageput.place(x=0,y=0,relwidth=1,relheight=1)

imageput.pack()

#end of the window GUI
window.mainloop()
