from tkinter import *

root = Tk()
root.geometry("500x300+400+100")
root.resizable(False,False)
a =0
def start():
    global a
    a+=1
    lbl1.configure(text=f"{a}",bg="red")

def stop():
    global a
    a +=2
    lbl1.configure(text=f"{a}",bg="blue")

lbl1= Label(root,text="0")
lbl1.pack()

btn1 = Button(root,text="btn1",command=start)
btn1.pack()

btn2 = Button(root,text="btn2",command=stop)
btn2.pack()


root.mainloop()
