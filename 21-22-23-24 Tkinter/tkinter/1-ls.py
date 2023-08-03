# from tkinter import *
# root = Tk()
# root.geometry("500x300+150+150")
# root.title("Darmen")
# root.resizable(False, False)
# Label(root,text="Hello World!",
#       relief=RIDGE,anchor=CENTER,padx=30,pady=30,
#
#
#       fg="green",bg="red").pack()
# Button(root,text="Start",fg="cyan",bg="yellow").pack()
#
#
#
#
#
# root.mainloop()










#
# from tkinter import *
# root = Tk()
# root.geometry("600x800+150+150")
# root.title("tkinter")
# a = 0
# def start():
#     global a
#     if a %2 ==1:
#         label['text']= "start"
#     else:
#         label['text'] = "Darmen"
#     a+=1
#     print(a)
# # # relief=FLAT,SUNKEN,RAISED,GROOVE,RIDGE,
# label = Label(root,text="Hello World!",
#                 relief=GROOVE,anchor=N,pady=5,padx=5,
#                 font=("Arial", 40), bg="red", fg="blue")
# label.pack()
# # # cursor="plus", arrow, hand2,cross, watch, xterm, fleur, circle,
# button = Button(root,cursor="watch", text="start",
#                 font=("Arial", 18),command=start,
#                 activebackground="red",
#                 activeforeground="blue")
# button.pack()
# root.mainloop()

#
#
#
# ################# pack,place,grid #####################
# from tkinter import *
# root = Tk()
# root.geometry("500x300+150+150")
# root.resizable(True,True)
# root.title("tkinter")
# label = Label(root,text="label",bg="red")
# label1 = Label(root,text="labe1",bg="red")
# label2= Label(root,text="labe2",bg="red")
# label3 = Label(root,text="labe3",bg="red")
# label4 = Label(root,text="labe4",bg="red")
# label5 = Label(root,text="label5",bg="red")
# # label.pack()  # pack()
# # label.place(x=370,y=70)   # place  # relx=1/2, rely=1/2, bordermode=INSIDE,OUTSIDE
# label.grid(row=0, column=0)  # row-qatar, column-bag'ana
# label1.grid(row=0,column=1)
# label2.grid(row=1, column=0)
# label3.grid(row=1, column=1)
# label4.grid(row=2, columnspan=2)
# label5.grid(row=0, column=2, rowspan=2)  # sticky=S,N,W,E
# #
# root.mainloop()
######################################class#############################################
# from tkinter import *
#
# class Window:
#     def __init__(self, width, height,title="Python tkinter", resizable=(False,False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.a = IntVar()
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.l1 = Label(self.root,text="Darmen")
#         self.l1.pack()
#         self.b1 = Button(self.root, text="start", command=self.start)
#         self.b1.pack()
#         self.a = 1
#
#     def start(self):
#         if self.a % 2 == 1:
#             self.l1['text'] = "start"
#         else:
#             self.l1['text'] = "Darmen"
#         self.a+=1
#
#
# if __name__ == "__main__":
#     window = Window(500,500, "TKINTER")
#     window.run()

################################Messagebox################################################
# from tkinter import *
# from tkinter import messagebox
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#        Button(self.root, text="info", width=10,command=lambda: messagebox.showinfo("Info","Info message")).pack()
#        Button(self.root, text="warning", width=10,command=lambda: messagebox.showwarning("Warnig","Warning message")).pack()
#        Button(self.root, text="error", width=10,command=lambda: messagebox.showerror("Error","Error message")).pack()
#        Button(self.root, text="quit", width=10,command=self.exit).pack()
#
#     def exit(self):
#         choice = messagebox.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()
##################################Entry######################################################
# from tkinter import *
# from tkinter import messagebox as mb
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.login_entry = Entry(self.root)
#         self.age_entry = Entry(self.root)
#         self.password_entry = Entry(self.root, show="*")
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         Label(self.root, text="Login:", justify=LEFT).grid(row=0, column=0, sticky=W)
#         self.login_entry.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
#         Label(self.root, text="Age:", justify=LEFT).grid(row=1, column=0, sticky=W)
#         self.age_entry.grid(row=1, column=1, sticky=W + E, padx=5, pady=5)
#         Label(self.root, text="Password:", justify=LEFT).grid(row=2, column=0, sticky=W)
#         self.password_entry.grid(row=2, column=1, sticky=W + E, padx=5, pady=5)
#
#         Button(self.root, text="Clear", width=10, command=self.clear).grid(row=3, column=2, padx=5, sticky=E)
#
#         Button(self.root, text="Save", width=10, command=self.save_data).grid(row=3, column=0, padx=5, sticky=E)
#         Button(self.root, text="Quit", width=10, command=self.exit).grid(row=3, column=1, sticky=E)
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#     def save_data(self):
#         login = self.login_entry.get()
#         age = int(self.age_entry.get())
#         password = self.password_entry.get()
#
#         mb.showinfo("User Data", f"Hello, {login}! You're {age} y.o.")
#
#     def clear(self):
#         self.login_entry.delete(0, END)
#         self.age_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

####################################RadioButton#############################################################
#
# from tkinter import *
# from tkinter import messagebox as mb
#
#
# RED = 0
# ORANGE = 1
# YELLOW = 2
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.choice = IntVar(value=1)
#         self.info = Label(self.root)
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         Radiobutton(self.root, text="Sea", variable=self.choice, value=0, indicatoron=1, width=10,  #indicatoron=0
#                     command=lambda: self.show_info("sea")).pack(anchor=E)
#         Radiobutton(self.root, text="Forest", variable=self.choice, value=1, indicatoron=1, width=10,  #indicatoron=0
#                     command=lambda: self.show_info("forest")).pack(anchor=E)
#         Radiobutton(self.root, text="Jungle", variable=self.choice, value=2, width=10,  #indicatoron=0
#                     command=lambda: self.show_info("jungle")).pack(anchor=E)
#
#         self.info.pack(anchor=CENTER)
#
#         # Button(self.root, text="Save", width=10, command=self.command).pack()
#         Button(self.root, text="Quit", width=10, command=self.exit).pack()
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#     def show_info(self, place):
#         if place == "sea":
#             self.info.configure(text="Sea radiobutton basildi", bg="blue", fg="white")
#         elif place == "forest":
#             self.info.configure(text="forest radiobutton basildi", bg="green", fg="brown")
#         else:
#             self.info.configure(text="jungle radiobutton basildi", bg="red", fg="blue")
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

############################CheckButton#########################################
#
#
# from tkinter import *
# from tkinter import messagebox as mb
#
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.a = IntVar()
#         self.b = IntVar()
#
#         self.l1 = Label(self.root, text="Hello World!")
#         # self.a = IntVar()
#         self.a = 0
#
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.l1.pack()
#         Checkbutton(self.root, text="one", variable=self.a, command=self.aa).pack()
#         Checkbutton(self.root, text="two", variable=self.b, command=self.bb).pack()
#         Button(self.root, text="start",command=self.start).pack()
#
#         Button(self.root, text="Quit", width=10, command=self.exit).pack()
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#     def start(self):
#         if self.a == 1 and self.b == 1:
#             self.l1.configure(text="one and two")
#         elif self.a == 1:
#             self.l1.configure(text="one")
#         elif self.b == 1:
#             self.l1.configure(text="two")
#         else:
#             self.l1.configure(text="Hello World!")
#
#     def aa(self):
#         self.a = 1
#
#     def bb(self):
#         self.b = 1
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()
######################  Combobox  ###########################
# from tkinter import *
# from tkinter import messagebox as mb
# from tkinter.ttk import Combobox
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.numbers = Combobox(self.root, values=(1, 3, 5), state="readonly")
#         self.color = Combobox(self.root, values=("red", "blue", "green"), justify=CENTER)
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.numbers.pack()
#         self.color.pack()
#
#         Button(self.root, text="Get", width=10, command=self.get_number).pack()
#         Button(self.root, text="Quit", width=10, command=self.exit).pack()
#
#     def get_number(self):
#         index = self.numbers.get()
#         index1 = self.color.get()
#
#         mb.showinfo("Get info", f"Index Numbers: {index}, Index Colors: {index1},")
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

#####################Spinbox################################
# from tkinter import *
# from tkinter import messagebox as mb
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.s = Spinbox(self.root, values=list(range(10)))
#         self.l = Label(self.root,text="Python")
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.s.pack()
#         self.l.pack()
#
#         Button(self.root, text="Save", width=10, command=self.save).pack()
#         Button(self.root, text="Quit", width=10, command=self.exit).pack()
#
#     def save(self):
#         choice_1 = self.s.get()
#         self.l.configure(text=f"{choice_1}", bg="red")
#         mb.showinfo("Info_1", f"Got value_1 {choice_1}")
#
#
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()


######################### menu1 ###################################
# from tkinter import *
# from tkinter import messagebox as mb
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         menu_bar = Menu(self.root)
#
#         menu_bar.add_command(label="Hey", command=self.cmd)
#         menu_bar.add_command(label="Edit", command=self.cmd1)
#         menu_bar.add_command(label="Help")
#
#         self.root.configure(menu=menu_bar)
#
#     def cmd(self):
#         mb.showinfo("123", "123")
#
#     def cmd1(self):
#         win = Tk()
#         win.title("menu")
#         win.geometry("400x500+200+200")
#         win.resizable(False, False)
#
#         win.mainloop()
#
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

####################   menu2   ###########################
# from tkinter import *
# from tkinter import messagebox as mb
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.auto_save = BooleanVar(value=0)
#         self.age = IntVar()
#
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.draw_menu()
#         Label(self.root, text="Just a label").pack()
#         Button(self.root, text="Quit", width=10, command=self.exit).pack()
#
#     def draw_menu(self):
#         menu_bar = Menu(self.root)
#
#         file_menu = Menu(menu_bar, tearoff=0)
#         file_menu.add_command(label="Сохранить", command=self.cmd)
#         file_menu.add_command(label="Сохранить как...")
#         file_menu.add_separator()
#         file_menu.add_checkbutton(label="Автосохранение", offvalue=0, onvalue=1, variable=self.auto_save,
#                                   command=self.auto_save_changed)
#         file_menu.add_separator()
#         file_menu.add_radiobutton(label="1 год", value=1, variable=self.age, command=self.age_changed)
#         file_menu.add_radiobutton(label="2 года", value=2, variable=self.age, command=self.age_changed)
#         file_menu.add_radiobutton(label="3 года", value=3, variable=self.age, command=self.age_changed)
#         file_menu.add_separator()
#         file_menu.add_command(label="Выйти", command=self.exit)
#
#         menu_bar.add_cascade(label="Файл", menu=file_menu)
#         self.root.configure(menu=menu_bar)
#
#     def auto_save_changed(self):
#         mb.showinfo("AutoSave", f"Value: {self.auto_save.get()}")
#
#     def age_changed(self):
#         mb.showinfo("Age", f"Value: {self.age.get()}")
#
#     def cmd(self):
#         mb.showinfo("123", "123")
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

#######################  menu3  ##########################
#
# from tkinter import *
# from tkinter import messagebox as mb
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#
#         self.auto_save = BooleanVar(value=0)
#         self.auto_load = BooleanVar(value=0)
#         self.value = IntVar()
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         self.draw_menu()
#         Label(self.root, text="Tkinter").pack()
#
#     def draw_menu(self):
#         menu_bar = Menu(self.root)
#
#         file_menu = Menu(menu_bar, tearoff=0)
#         file_menu.add_command(label="Сохранить", command=self.cmd)
#         file_menu.add_separator()
#         file_menu.add_command(label="Выйти", command=self.exit)
#
#         edit_menu = Menu(menu_bar, tearoff=0)
#         parameters_menu = Menu(edit_menu, tearoff=0)
#         parameters_menu.add_checkbutton(label="Автосохранение", offvalue=0, onvalue=1, variable=self.auto_save)
#         parameters_menu.add_checkbutton(label="Автозагрузка", offvalue=0, onvalue=1, variable=self.auto_load,
#                                         command=self.check_auto_load)
#         edit_menu.add_cascade(label="Параметры", menu=parameters_menu)
#         edit_menu.add_separator()
#
#         values_menu = Menu(edit_menu, tearoff=0)
#         values_menu.add_radiobutton(label="Один", value=1, variable=self.value)
#         values_menu.add_radiobutton(label="Два", value=2, variable=self.value)
#         values_menu.add_radiobutton(label="Три", value=3, variable=self.value)
#         edit_menu.add_cascade(label="Значения", menu=values_menu)
#
#         info_menu = Menu(menu_bar, tearoff=0)
#         info_menu.add_command(label="О приложении", command=self.show_info)
#
#         menu_bar.add_cascade(label="Файл", menu=file_menu)
#         menu_bar.add_cascade(label="Настройки", menu=edit_menu)
#         menu_bar.add_cascade(label="Справка", menu=info_menu)
#         self.root.configure(menu=menu_bar)
#
#     def check_auto_load(self):
#         if not self.auto_save.get() and self.auto_load.get():
#             if mb.askyesno("Ошибка", "Автозагрузка без автосохранения. Хотите установить автосохранение?"):
#                 self.auto_save.set(True)
#
#     def show_info(self):
#         mb.showinfo("Информация", "Лучшее графическое приложение на свете")
#
#     def auto_save_changed(self):
#         mb.showinfo("AutoSave", f"Value: {self.auto_save.get()}")
#
#     def age_changed(self):
#         mb.showinfo("Age", f"Value: {self.age.get()}")
#
#     def cmd(self):
#         mb.showinfo("123", "123")
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

from tkinter import *
from tkinter import Button
from tkinter import messagebox as mb
import tkinter as tk

class Window:
    def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0],resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.entry = tk.Entry(self.root, font="Helvetica 20 bold", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Button(self.root, text="7",command=lambda x=7: self.entry.insert(tk.END, x),
            font="Helvetica 20 bold",
               relief="ridge").grid(row=1, column=0, sticky="nsew")
        Button(self.root, text="8", command=lambda x=8: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=1, column=1, sticky="nsew")
        Button(self.root, text="9", command=lambda x=9: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=1, column=2, sticky="nsew")
        Button(self.root, text="/", command=lambda x="/": self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=1, column=3, sticky="nsew")
        Button(self.root, text="4", command=lambda x=4: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=2, column=0, sticky="nsew")
        Button(self.root, text="5", command=lambda x=5: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=2, column=1, sticky="nsew")
        Button(self.root, text="6", command=lambda x=6: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=2, column=2, sticky="nsew")
        Button(self.root, text="*", command=lambda x="*": self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=2, column=3, sticky="nsew")
        Button(self.root, text="1", command=lambda x=1: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=3, column=0, sticky="nsew")
        Button(self.root, text="2", command=lambda x=2: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=3, column=1, sticky="nsew")
        Button(self.root, text="3", command=lambda x=3: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=3, column=2, sticky="nsew")
        Button(self.root, text="-", command=lambda x="-": self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=3, column=3, sticky="nsew")
        Button(self.root, text="0", command=lambda x=0: self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=4, column=0, sticky="nsew")
        Button(self.root, text="C", command=lambda x="C": self.on_click(x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=4, column=1, sticky="nsew")
        Button(self.root, text="=", command=lambda x="=": self.on_click(x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=4, column=2, sticky="nsew")
        Button(self.root, text="+", command=lambda x="+": self.entry.insert(tk.END, x),
               font="Helvetica 20 bold",
               relief="ridge").grid(row=4, column=3, sticky="nsew")

    def on_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)


if __name__ == "__main__":
    window = Window(305, 260, "TKINTER")
    window.run()







