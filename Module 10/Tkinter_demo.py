
from tkinter import *
from tkinter import messagebox
'''window=Tk()
window.title('Python Training')
window.geometry('50x100')
Label(window,text='First Label').pack()
b1=Button(window,text='Reset Everything',fg='Red')
b1.pack()
window.pack()'''


'''
window=Tk()
window.title('Frame')
top_frame=Frame(window).pack()
bottom_frame=Frame(window).pack(side='bottom')
butn1=Button(top_frame,text='Button 1',fg='Red',bg='black').pack()
butn2=Button(top_frame,text='Button 2').pack()
butn3=Button(bottom_frame,text='Button 3').pack()
butn4=Button(bottom_frame,text='Button 4').pack()
window.mainloop()'''
'''
window=Tk()
CheckVar1=IntVar()
CheckVar2=IntVar()
Checkbutton(window,text='Machine Learning',variable=CheckVar1,onvalue=1,offvalue=0).grid(row=0,sticky=S)
Checkbutton(window,text='Deep Learning',variable=CheckVar2,onvalue=0,offvalue=1).grid(row=1,sticky=W)
window.mainloop()
'''
'''
window=Tk()
def Login():
    messagebox.showinfo('Alert Message','You are being watched')
Label(window,text='Username').grid(row=0,column=0)
Entry(window).grid(row=0,column=1)
Label(window,text='Password').grid(row=1,column=0)
Entry(window).grid(row=1,column=1)
Checkbutton(window,text='Keep me Logged in').grid(columnspan=2)
b1=Button(window,text='Login',fg='black',bg='red',command=Login).grid(row=3,columnspan=2,)
window.mainloop()'''
from tkinter import *
window=Tk()
a="C:\\Users\\Priyanshu Patidar\\AppData\\Local\\Programs\\Python\\Python37\\tkinter_Learning\\chtbot.png"
icon=PhotoImage(file=a)
label=Label(window,image=icon).pack()
window.mainloop()
