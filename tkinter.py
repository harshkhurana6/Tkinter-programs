from tkinter import *
root=Tk()
root.geometry("350x200")
root.title("welcome screen")
l=Label(root,text="Welcome to tkinter")
l.place(x=100,y=100)
l=Label(root,text="Welcome to tkinter",font=("Arial Black",50),bg="yellow",fg="red")
l.place(x=100,y=100)

def clicked():
  l.configure(text="Happy learning tkinter")

b1=Button(root,text="Click me",command=clicked)
b1.grid(row=0,column=1)
root.mainloop()


from tkinter import *
window=Tk()
window.title("Button demo")
window.geometry("350x200")
def button1_clicked():
  window.configure(background="red")
def button2_clicked():
  window.configure(background="green")
def button3_clicked():
  window.configure(background="blue")
b1=Button(text="red",command=button1_clicked)
b2=Button(text="green",command=button2_clicked)
b3=Button(text="blue",command=button3_clicked)
b4=Button(text="Exit",command=window.destroy)
b1.place(x=0,y=0)
b2.place(x=160,y=0)
b3.place(x=320,y=0)
b4.place(x=320,y=170)
window.mainloop()


from tkinter import *
window=Tk()
window.title("welcome")
window.geometry('350x200')
lbl=Label(window,text="Enter your name")
lbl.place(x=0,y=0)
txt=Entry(window,width=10)
txt.place(x=160,y=0)
def clicked():
  res="Welcome:"+txt.get()
  lbl.configure(text=res)
btn=Button(window,text="click me",command=clicked)
btn.place(x=300,y=0)
window.mainloop()



from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('350x200')
vtxtuname=StringVar()
def fnlogin():
  nm=str(txtuname.get())
  messagebox.showwarning("Login Info","Login successful__"+nm)
vtxtuname.set("Enter the name")
def fncancel():
  messagebox.showinfo('Cancel Info','Quitting App')
  window.destroy()
lblname=Label(window,text='Username')
lblname.place(x=0,y=0)
lblpass=Label(window,text='Password')
lblpass.place(x=0,y=70)
txtuname=Entry(window,textvariable=vtxtuname)
txtuname.place(x=160,y=0)
txtpass=Entry(window,show='*')
txtpass.place(x=70,y=70)
b1=Button(text='Login',command=fnlogin)
b2=Button(text='Cancel',command=fncancel)
b1.place(x=0,y=120)
b2.place(x=160,y=120)
window.mainloop()



from tkinter import *
from tkinter.ttk import *
window=Tk()
window.geometry('350x200')
chk_red=BooleanVar()
chk_green=BooleanVar()
def oncheckboxchanged():
  if (chk_red.get()==True and chk_green.get()==False):
    window.configure(background='red')
  elif (chk_red.get()==False and chk_green.get()==True):
    window.configure(background='green')
  elif (chk_red.get()==True and chk_green.get()==True):
    window.configure(background='yellow')
  else:
    window.configure(background='white')
chk1=Checkbutton(window,text='Red',var=chk_red,command=oncheckboxchanged)
chk2=Checkbutton(window,text='green',var=chk_green,command=oncheckboxchanged)
chk1.place(x=0,y=0)
chk2.place(x=280,y=0)
window.mainloop()

from tkinter import *
from tkinter.ttk import *
window=Tk()
window.geometry('350x200')
selected=IntVar()
size=IntVar()
def clicked():
  choice=selected.get()
  if(choice==1):
    window.configure(background='red')
  elif (choice==2):
    window.configure(background='green')

def changesize():
  choice=size.get()
  if (choice==1):
    window.geometry('500x300')
  elif (choice==2):
    window.geometry('350x200')
rd1=Radiobutton(window,text='Red',value=1,variable=selected,command=clicked)
rd2=Radiobutton(window,text='Green',value=2,variable=selected,command=clicked)

size1=Radiobutton(window,text='Big',value=1,variable=size,command=changesize)
size2=Radiobutton(window,text='Small',value=2,variable=size,command=changesize)

rd1.place(x=0,y=0)
rd2.place(x=150,y=0)
size1.place(x=0,y=75)
size2.place(x=150,y=75)
window.mainloop()



from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("combo box demo")
window.geometry("350x200")
def onclicked(event):
  print(var.get())
var=StringVar()
combo=Combobox(window,textvariable=var)
combo.bind("<<combobox selected>>",onclicked)
combo['values']=(1,2,3,4,5,"Text")
combo.current(1)
combo.place(x=0,y=0)
window.mainloop()


from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("List box demo")
window.geometry('350x200')
parentlist=['one','two','three']
l1=Listbox()
for item in parentlist:
  l1.insert(END,item)
l1.place(x=0,y=0)
l2=Listbox()
l2.place(x=150,y=0)

def onSelect(event):
  w=event.widget
  index=w.curselection()[0]
  val=w.get(w.curselection())
  print("You selected:{0} and that variable in {1}".format(index,val))
  l2.insert(END,str(index)+""+val)

  
l1.bind("<<ListboxSelect>>",lambda event:onSelect(event))
window.mainloop()


from tkinter import filedialog
from tkinter import *
def Newfile():
  print("Newfile")
def Openfile():
  name=filedialog.askopenfilename()
  print(name)
def About():
  print("this is a simple example")
root=Tk()
mymenu=Menu(root)
root.configure(menu=mymenu)
filemenu=Menu(mymenu)
mymenu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label="New",command=Newfile)
filemenu.add_command(label="Open",command=Openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
helpmenu=Menu(mymenu)
mymenu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=About)
root.mainloop()



from tkinter import *
import sqlite3
window=Tk()
window.title("STOCK ENTRY SCREEN")
window.geometry('350x200')
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt4=StringVar()

l=Label(window,text="STOCK ENTRY SCREEN")
l.place(x=100,y=0)
l1=Label(window,text="Item Code:")
l1.place(x=0,y=30)
t1=Entry(window,textvariable=txt1)
t1.place(x=150,y=30)
l2=Label(window,text="Item Name:")
l2.place(x=0,y=60)
t2=Entry(window,textvariable=txt2)
t2.place(x=150,y=60)
l3=Label(window,text="Rate:")
l3.place(x=0,y=90)
t3=Entry(window,textvariable=txt3)
t3.place(x=150,y=90)
l4=Label(window,text="Quantity in Hand:")
l4.place(x=0,y=120)
t4=Entry(window,textvariable=txt4)
t4.place(x=150,y=120)

def button1_clear():
  txt1.set("")
  txt2.set("")
  txt3.set("")
  txt4.set("")
  t1.focus()

def button2_insert():
  sqlite_file='inventory.sqlite'
  conn=sqlite3.connect(sqlite_file)
  c=conn.cursor()
  c.execute('create table if not exists stock(icode Text,iname Text,rate Text,QIH Text)')

  c.execute('insert into stock(icode,iname,rate,QIH) values (?,?,?,?)',(txt1.get(),txt2.get(),txt3.get(),txt4.get()))
  conn.commit()
  button1_clear()
  
b1=Button(text="Clear",command=button1_clear)
b2=Button(text="Insert",command=button2_insert)
b3=Button(text="Exit",command=window.destroy)

b1.place(x=150,y=150)
b2.place(x=0,y=150)
b3.place(x=300,y=150)
t1.focus()
window.mainloop()




import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
c.execute("Select* from stock")
data=c.fetchall()
print(data)
print("Item Code,Item Name,Rate,QOH")
for row in c.fetchall():
  print(row[0],row[1])
conn.commit()
conn.close()


import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
icode='1001'
iname1='shirt'
rate1='5'
QIH1='7'
c.execute("update stock set iname=(?),rate=(?),QIH=(?) where icode=(?)",(iname1,rate1,QIH1,icode))
conn.commit()
conn.close()

import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
c.execute("delete from stock")
conn.commit()
conn.close()

import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
icode='1001'
c.execute("delete from stock where icode=(?)",(icode,))
conn.commit()
conn.close()
