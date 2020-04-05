'''
Created on Mar 31, 2020

@author: jimmy
'''
import tkinter as tk
import smtplib


def find_word_length(text):
    return len([i for i in text.split() if i != '\n'])

class Email_app(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.create_widget()

    def create_widget(self):
        
        self.myLabel = tk.Label(root, text = "Email app", width = 50).grid()
        self.myUsername = tk.Label(root, text = "Username").place(x = 10, y = 30, width = 70, height = 20)
        self.myUserEntry = tk.Entry(root)
        self.myUserEntry.place(x = 90, y = 30, width = 200, height = 20)
        self.myPassword = tk.Label(root, text = "Password").place(x = 10, y = 60, width = 70, height = 20)
        self.myPasswordEntry = tk.Entry(root)
        self.myPasswordEntry.place(x = 90, y = 60, width = 200, height = 20)
        self.To = tk.Label(root, text = "Destination").place( x = 10, y = 90, width = 70, height = 20)
        self.To_entry = tk.Entry(root)
        self.To_entry.place(x = 90, y = 90, width = 200, height = 20)
        
        
        #from here is about the entry box
        self.myEntry = tk.Text(root, wrap = tk.WORD)
        self.myEntry.bind('<KeyRelease>',lambda _: self.callback())
        self.myEntry.place(x = 10, y = 120, width = 430, height = 460)
        
        
        self.strVal = tk.StringVar() 
        self.strVal.set("Word: 0 word")
        self.Textlength = tk.Label(root, textvariable = self.strVal, width = 70)
        self.Textlength.place(x = 320, y = 50, width = 120, height = 30)

        self.myBtn = tk.Button(root,text = "Submit email", command = self.on_release)
        self.myBtn.place(x = 350, y = 600)
        
    def on_release(self):
        Username = self.myUserEntry.get()
        Password = self.myPasswordEntry.get()
        Destination = self.To_entry.get()
        text = self.myEntry.get('1.0',tk.END)
        self.myEntry.delete('1.0', tk.END)
        self.strVal.set("Word: 0 word")
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(Username,Password)
            server.sendmail(Username,Destination,text)
        except:
            print('Something went wrong')
    
    def callback(self):
        length = find_word_length(self.myEntry.get('1.0',tk.END))
        if length == 1 or length == 0:
            self.strVal.set(f"Word: {length} word")
        elif length > 1 and length <= 200:
            self.strVal.set(f"Word: {length} words")
        if length > 200:
            self.myEntry.delete("end-2c")
    


    
root = tk.Tk()
root.geometry("450x650")
root.resizable(width=False, height=False)
Email_app_main = Email_app(root)
Email_app_main.mainloop()