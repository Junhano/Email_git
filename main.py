'''
Created on Mar 31, 2020

@author: jimmy
'''
import tkinter as tk
import smtplib

root = tk.Tk()
root.geometry("400x650")
myLabel = tk.Label(root, text = "Email app", width = 50).grid()
myUsername = tk.Label(root, text = "Username").place(x = 10, y = 30, width = 70, height = 20)
myUserEntry = tk.Entry(root)
myUserEntry.place(x = 90, y = 30, width = 200, height = 20)
myPassword = tk.Label(root, text = "Password").place(x = 10, y = 60, width = 70, height = 20)
myPasswordEntry = tk.Entry(root)
myPasswordEntry.place(x = 90, y = 60, width = 200, height = 20)
To = tk.Label(root, text = "Destination").place( x = 10, y = 90, width = 70, height = 20)
To_entry = tk.Entry(root)
To_entry.place(x = 90, y = 90, width = 200, height = 20)
myEntry = tk.Text(root)
myEntry.place(x = 10, y = 120, width = 380, height = 460)


def on_release():
    Username = myUserEntry.get()
    Password = myPasswordEntry.get()
    Destination = To_entry.get()
    text = myEntry.get('1.0',tk.END)
    myEntry.delete('1.0', tk.END)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(Username,Password)
        server.sendmail(Username,Destination,text)
    except:
        print('Something went wrong')
    
    
    
    
myBtn = tk.Button(root,text = "Submit email", command = on_release)
myBtn.place(x = 310, y = 600)
root.resizable(width=False, height=False)
root.mainloop()
