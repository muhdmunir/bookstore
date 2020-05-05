from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END) #delete from a range
    for row in backend.view():
        list1.insert(END,row) #list.insert(index, element)

def search_command():
    list1.delete(0,END) #delete from a range
    for row in backend.search(title_e1.get(), author_e2.get(), year_e3.get(), isbn_e4.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_e1.get(), author_e2.get(), year_e3.get(), isbn_e4.get())
    list1.delete(0,END) #delete from a range
    list1.insert(END,(title_e1.get(),author_e2.get(), year_e3.get(), isbn_e4.get()))
    view_command()

def update_command():
    backend.update(selected_tuple[0],title_e1.get(), author_e2.get(), year_e3.get(), isbn_e4.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

window=Tk()
window.wm_title("My Book Database")

l1 = Label(window, text="Title").grid(row=0, column=0)
l1 = Label(window, text="Author").grid(row=0, column=2)
l1 = Label(window, text="Year").grid(row=1, column=0)
l1 = Label(window, text="ISBN").grid(row=1, column=2)

title_e1=StringVar()
e1=Entry(window,textvariable=title_e1)
e1.grid(row=0, column=1) #entry widget

author_e2=StringVar()
e2=Entry(window,textvariable=author_e2)
e2.grid(row=0, column=3) #entry widget

year_e3=StringVar()
e3=Entry(window,textvariable=year_e3)
e3.grid(row=1, column=1) #entry widget

isbn_e4=StringVar()
e4=Entry(window,textvariable=isbn_e4)
e4.grid(row=1, column=3) #entry widget

list1=Listbox(window, height=12,width=45, selectmode=EXTENDED)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window) #add scroll Scrollbar
sb1.grid(row=2,column=2, rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width = 12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width = 12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add New Entry",width = 12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width = 12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width = 12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close Program",width = 12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
