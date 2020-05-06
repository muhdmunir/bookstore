from tkinter import *
from backend import Database #import database class from backend script

database=Database("books.db")

class ux(object):

    def __init__(self,window):
        self.window=window
        self.window.wm_title("My Book Database")

        l1 = Label(window, text="Title").grid(row=0, column=0)
        l1 = Label(window, text="Author").grid(row=1, column=0)
        l1 = Label(window, text="Year").grid(row=2, column=0)
        l1 = Label(window, text="ISBN").grid(row=3, column=0)

        self.title_e1=StringVar()
        self.e1=Entry(window,textvariable=self.title_e1)
        self.e1.grid(row=0, column=1) #entry widget

        self.author_e2=StringVar()
        self.e2=Entry(window,textvariable=self.author_e2)
        self.e2.grid(row=1, column=1) #entry widget

        self.year_e3=StringVar()
        self.e3=Entry(window,textvariable=self.year_e3)
        self.e3.grid(row=2, column=1) #entry widget

        self.isbn_e4=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_e4)
        self.e4.grid(row=3, column=1) #entry widget

        self.list1=Listbox(window, height=12,width=25, selectmode=EXTENDED)
        self.list1.grid(row=5, column=1, rowspan=6, columnspan=2)

        sb1=Scrollbar(window) #add scroll Scrollbar
        sb1.grid(row=5,column=0, rowspan=6)

        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b7=Button(window,text="clear",width = 12, command=self.clear_title)
        b7.grid(row=0,column=2)
        b8=Button(window,text="clear",width = 12, command=self.clear_author)
        b8.grid(row=1,column=2)
        b9=Button(window,text="clear",width = 12, command=self.clear_year)
        b9.grid(row=2,column=2)
        b10=Button(window,text="clear",width = 12, command=self.clear_isbn)
        b10.grid(row=3,column=2)
        b11=Button(window,text="Clear All",width = 12, command=self.clear_all)
        b11.grid(row=0,column=3)

        b1=Button(window,text="View All",width = 12, command=self.view_command)
        b1.grid(row=5,column=3)

        b2=Button(window,text="Search Entry",width = 12, command=self.search_command)
        b2.grid(row=6,column=3)

        b3=Button(window,text="Add New Entry",width = 12, command=self.add_command)
        b3.grid(row=7,column=3)

        b4=Button(window,text="Update Selected",width = 12, command=self.update_command)
        b4.grid(row=8,column=3)

        b5=Button(window,text="Delete Selected",width = 12, command=self.delete_command)
        b5.grid(row=9,column=3)

        b6=Button(window,text="Close Program",width = 12, command=window.destroy)
        b6.grid(row=10,column=3)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END) #delete from a range
        for row in database.view():
            self.list1.insert(END,row) #list.insert(index, element)

    def search_command(self):
        self.list1.delete(0,END) #delete from a range
        for row in database.search(self.title_e1.get(), self.author_e2.get(), self.year_e3.get(), self.isbn_e4.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.title_e1.get(), self.author_e2.get(), self.year_e3.get(), self.isbn_e4.get())
        self.list1.delete(0,END) #delete from a range
        self.list1.insert(END,(self.title_e1.get(),self.author_e2.get(), self.year_e3.get(), self.isbn_e4.get()))
        self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0],self.title_e1.get(), self.author_e2.get(), self.year_e3.get(), self.isbn_e4.get())
        self.view_command()

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def clear_title(self):
        self.e1.delete(0,END)

    def clear_all(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)

    def clear_author(self):
        self.e2.delete(0,END)

    def clear_year(self):
        self.e3.delete(0,END)

    def clear_isbn(self):
        self.e4.delete(0,END)

window=Tk()
ux(window)
window.mainloop()
