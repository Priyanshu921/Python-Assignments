from tkinter import *
import winsound
def voice():
    q=n.get()
    m=0
    for i in q:
        if i=='0':
            m+=1
        else:
            p=len(q)-m
            a='0'*(p-1)
            i=i+''+a+'.wav'
            winsound.PlaySound(i, winsound.SND_FILENAME)
            m+=1
root=Tk()
n=StringVar()
root.geometry('200x100')
root.maxsize('200','100')
Label(root,text='Enter Any Number Below 10000').grid(row=1,column=2)
Entry(root,textvariable=n).grid(row=2,column=2)
Button(root,text='Conver to Voice',command=voice).grid(rows=3,column=2)
root.mainloop()
