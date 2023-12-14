from tkinter import *
from PIL import ImageTk
from random import randint
from tkinter import simpledialog


root=Tk()

root.iconbitmap('num.ico')
root.geometry('300x500')
root.configure(background="#5AA8D2")
root.title('Guess The Number')

bg=ImageTk.PhotoImage(file='bg.png')
c=Canvas(root)
c.create_image(0,0,image=bg,anchor='nw')



def restart():
    global r
    global tries
    rb.set(str(r)+' !')#update the result value
    c.itemconfigure(rev, text=root.getvar(str(rb)))#show old result
    r=randint(1,100)
    tri = simpledialog.askstring(title="Tries", prompt="How Many Tries ? : ")
    tries = int(tri)
    trt.set('Tries left:\n       '+str(tries))
    c.itemconfigure(ttt, text=root.getvar(str(trt)))



def check():
    global tries
    if tries==0:
        restart()
    else:
        guess=int(e.get())
        if guess<r:
            res.set('Too Little !')
            c.itemconfigure(txt, text=root.getvar(str(res)))
            tries-=1
        elif guess>r:
            res.set('Too Much !')
            c.itemconfigure(txt, text=root.getvar(str(res)))
            tries-=1
        else:
            res.set('Good Job !')
            c.itemconfigure(txt, text=root.getvar(str(res)))
            tries-=1
    trt.set('Tries left:\n       '+str(tries))
    c.itemconfigure(ttt, text=root.getvar(str(trt)))


r=randint(1,100)
tri = simpledialog.askstring(title="Tries", prompt="How Many Tries ? : ")
tries = int(tri)


trt=StringVar()
trt.set('Tries left:\n       '+str(tries))
tr=Label(root, textvariable=trt, bg="white", font=('Helvatical bold',11))
ttt=c.create_text(50, 50, text=trt.get(),fill='black', font=('Helvatical', 11, 'bold'))


c.create_text(150, 115, text="Insert a number from 1 to 100",fill='white', font=('Helvatical', 14, 'bold'))

e=Entry(root)
c.create_window(150,140,window=e,anchor='center')

b=Button(root, text='Submit', command=check)
c.create_window(120,180,window=b,anchor='center')

rt=Button(root, text='Reset', command=restart)
c.create_window(180,180,window=rt,anchor='center')

res=StringVar()
txt=c.create_text(150, 220, text=res.get(),fill='white', font=('Helvatical', 14, 'bold'))
res.set('')

rb=StringVar()
rb.set('...')
rev=c.create_text(232, 282, text=rb.get(),fill='black', font=('Helvatical', 14, 'bold'))

c.pack(fill='both',expand=True)

root.mainloop()