from tkinter import *
mw=Tk()
mw.title("VIDHYA VARADHI")
mw.geometry("900x720")

frame1=LabelFrame(mw,text="THIS IS FRAME1",padx=10,pady=10,font=("",14))
frame1.grid(row=0,column=0,padx=20,pady=10)
exit_btn= Button(frame1,text="Exit",padx=60,pady=20,font=("",14),command=mw.quit)
exit_btn.pack()

def rv_res():
    rv_lbl.config(text=rv.get())
rv = IntVar()
Radiobutton(frame1,text="option1",value=1,variable=rv,font=("",14),command=rv_res).pack(pady=(30,10))
Radiobutton(frame1,text="option2",value=2,variable=rv,font=("",14),command=rv_res).pack(pady=(0,20))
rv_lbl=LabelFrame(frame1,text="",font=("",14))
rv_lbl.pack()



















mw.mainloop()