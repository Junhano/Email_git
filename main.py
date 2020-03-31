'''
Created on Mar 31, 2020

@author: jimmy
'''
import tkinter as tk

root = tk.Tk()
root.geometry("400x800")
myLabel = tk.Label(root, text = "Email app", width = 50).pack()
myEntry = tk.Text(root)
myEntry.place(x = 10, y = 30, width = 380, height = 700)


def on_release():
    text = myEntry.get('1.0',tk.END)
    print(text)
myBtn = tk.Button(root,text = "Submit email", command = on_release)
myBtn.place(x = 310, y = 750)
root.mainloop()
