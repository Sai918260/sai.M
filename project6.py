import tkinter as tk
from tkinter import ttk,filedialog,messagebox
from tkinter.scrolledtext import ScrolledText

import pyttsx3
import threading

def convertAndplay():
    voices = bot.getProperty("voices")
    bot.setProperty("voice",voices[voice_var.get()].id)
    bot.setProperty("rate",speed_scale.get())
    text = text_box.get(0.0,tk.END)
    if len(text)>1:
        bot.say(text)
        bot.runAndWait()
    else:
        messagebox.showwarning("warning","First Enter some text to convert into audio")
def saveAudio():
    bot = pyttsx3.init()
    voices=bot.getProperty("voices")
    bot.setProperty("voice",voices[voice_var.get()].id)
    bot.setProperty("rate",speed_scale.get)
    text=text_box.get(0.0,tk.END)
    if len(text.strip())>1:
        filename=filedialog.asksaveasfilename(defaultextension=".wav")
        if filename:
            bot.save_to_file(text,filename)
            bot.runAndWait()
            messagebox.showinfo("successful","Audio is saved")
        else:
            messagebox.showwarning("warning","first entry some text to convert into audio")

def stopEngine():
    if bot.isBusy():
        print(bot.isBusy())
        bot.stop()
root=tk.Tk()
root.title("Text to speech converter app")
root.geometry("600x280")
root.configure(bg="#999")
root.resizable(0,0)

bot = pyttsx3.init()
voice_var = tk.IntVar()
text_box = ScrolledText(root,font=("sitka small",11),bd=2,relief=tk.GROOVE,wrap=tk.WORD,undo=True)
text_box.place(x=5,y=5,height=320,width=480)

frame=tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame.place(x=395,y=5,height=270,width=200)

frame2=ttk.LabelFrame(frame,text="change Speed")
frame2.grid(row=0,column=0,pady=5,padx=4)

speed_scale=tk.Scale(frame2,from_=100,to=300,orient=tk.HORIZONTAL,length=170,bg="#ffffff")
speed_scale.set(200)
speed_scale.grid(row=2,columnspan=1,ipadx=5,ipady=5)

frame3=ttk.LabelFrame(frame,text="Change Voice")
frame3.grid(row=1,column=0,pady=5)

R1=tk.Radiobutton(frame3,text="Male",variable=voice_var,value=0)
R1.grid(row=0,column=0,ipadx=7,ipady=5,padx=5)

R2=tk.Radiobutton(frame3,text="Female",variable=voice_var,value=1)
R2.grid(row=0,column=1,ipady=5,ipadx=7,padx=5)

frame4=tk.Frame(frame,bd=2,relief=tk.SUNKEN)
frame4.grid(row=2,column=0,pady=10)

btn_1 = ttk.Button(frame4,text="convert & play",width=15,command= lambda:threading.Thread(target=convertAndplay,daemon= True).start())
btn_1.grid(row=0,column=0,ipady=5,padx=4,pady=5)

btn_2 = ttk.Button(frame4,text="save as audio",width=15,command=saveAudio)
btn_2.grid(row=1,column=0,ipady=5,padx=4,pady=5)

btn_3 = ttk.Button(frame4,text="clear",width=10,command=lambda :text_box.delete(0.0,tk.END))
btn_3.grid(row=0,column=1,ipady=5,padx=4,pady=5)

btn_4 = ttk.Button(frame4,text="Exit",width=10,command=root.quit)
btn_4.grid(row=1,column=1,ipady=5,padx=4,pady=5)

root.mainloop()