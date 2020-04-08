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
        self.word_limit = 200
        self.create_widget()
        

    def create_widget(self):
        
        self.myLabel = tk.Label(root, text = "Email app").place(x = 170, y = 5, width = 60, height = 20)
        self.setting = tk.Button(root, text = "setting", command = self.pop_up_word_limit_setting)
        self.setting.place(x = 300, y = 5, width = 70, height = 20)
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
        self.Textlength = tk.Label(root, textvariable = self.strVal)
        self.Textlength.place(x = 320, y = 70, width = 120, height = 30)
        
        
        self.wordLimitDisplay = tk.StringVar()
        self.wordLimitDisplay.set(f"Current word limit {self.word_limit} words")
        self.LimitDisplay = tk.Label(root, textvariable = self.wordLimitDisplay)
        self.LimitDisplay.place(x = 290, y = 50, width = 160, height = 30)
        
        

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
        elif length > 1 and length <= self.word_limit:
            self.strVal.set(f"Word: {length} words")
        if length > self.word_limit:
            self.myEntry.delete("end-2c")
    

    def pop_up_word_limit_setting(self):
        popup = tk.Toplevel()
        popup.title("Word Limit Setting")
        tk.Label(popup, text = "Enter the word limit you want below").grid(row = 0, column = 0)
        word_limit = tk.Entry(popup)
        word_limit.grid(row = 1, column = 1)
        tk.Button(popup, text = 'save', command = lambda : action(popup)).grid(row = 2, column = 3)
        
        def action(root):
            try:
                self.word_limit = int(word_limit.get())
                self.wordLimitDisplay.set(f"Current word limit {self.word_limit} words")
                root.destroy()
            except:
                pass

    
root = tk.Tk()
root.geometry("450x650")
root.resizable(width=False, height=False)
Email_app_main = Email_app(root)
Email_app_main.mainloop()