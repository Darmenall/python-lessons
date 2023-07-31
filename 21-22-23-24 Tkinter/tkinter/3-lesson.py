import tkinter
from tkinter import *
from tkinter import messagebox as mb
from googletrans import Translator


class Window:
    def __init__(self,wigth,heigth,title="python",resizable=(False,False),icon=None):
        self.root = Tk()
        self.root.geometry(f"{wigth}x{heigth}+150+150")
        self.root.title(title)
        self.root.resizable(resizable[0],resizable[1])
        self.translator = Translator()

        self.txt1 = Text(self.root, width=26, height=10, undo=True)
        self.txt2 = Text(self.root, width=26, height=10, undo=True)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Translate").place(x=223, y=5)

        self.txt1.place(x=10, y=25)
        self.txt2.place(x=275, y=25)

        btn1 = Button(self.root,text="start",width=6,command=self.start)
        btn1.place(x=223, y=200)

    def start(self):
        a = self.txt1.get
        b = self.translator.translate(a, dest="en")
        self.txt2.insert(tkinter.END, str(b))


    def exit(self):
        choice = mb.askokcancel("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    app = Window(500,300,"Perevod")
    app.run()