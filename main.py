import tkinter as tk
import Email_extractor
import joblib
from tkinter import messagebox

class AppGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Spam email detection")

        self.label = tk.Label(self.root,text="Enter the Email text here",font=('Arial',20))
        self.label.pack(padx=20,pady=20)

        self.textbox = tk.Text(self.root,height=10,font=('Arial',12))
        self.textbox.pack(padx=10,pady=10)


        self.button = tk.Button(self.root,text="Check for spam",height=2,font=('Arial',12),background='yellow',command=self.check_text)
        self.button.pack(pady=40)

        self.root.mainloop()
    
    def check_text(self):
       self.features = Email_extractor.extractFeatures(self.textbox.get('1.0',tk.END))
       self.model = joblib.load('Spam_detect.pkl')
       self.prediction = self.model.predict(self.features) 
       mytext=""
       if self.prediction[0]:
           mytext = "SPAM"
       else:
           mytext = "NOT SPAM"
       messagebox.showinfo(title="Spam or not", message=mytext)



AppGUI()