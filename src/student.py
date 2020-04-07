from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

root = Tk()
root.title("Python & PostgreSQL")

def save_new_student(name, address, age):
    conn = psycopg2.connect(
            dbname="basepg", 
            user="usuariopg", 
            password="clavepg",
            host="127.0.0.1",
            port="5432"
    )
    cursor = conn.cursor()
    query = '''insert into students (name, address, age) values (%s, %s, %s)'''
    cursor.execute(query, (name, address, age))
    print("Data: ", name, address, age, "Saved!")
    conn.commit()
    conn.close()
    #Refresh new students
    display_students()

def display_students():
    conn = psycopg2.connect(
            dbname="basepg", 
            user="usuariopg", 
            password="clavepg",
            host="127.0.0.1",
            port="5432"
    )
    cursor = conn.cursor()
    query = '''select * from students;'''
    cursor.execute(query)
    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def search_student(student_id):
    conn = psycopg2.connect(
            dbname="basepg", 
            user="usuariopg", 
            password="clavepg",
            host="127.0.0.1",
            port="5432"
    )
    cursor = conn.cursor()
    query = '''select * from students where id=%s'''
    cursor.execute(query, (student_id))
    row = cursor.fetchone()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

# Canvas
canvas = Canvas(root, height=300, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a Student')
label.grid(row=0, column=1)

#Name Input
label = Label(frame, text='Name:')
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

#Address Input
label = Label(frame, text='Address:')
label.grid(row=2, column=0)
entry_address = Entry(frame)
entry_address.grid(row=2, column=1)

#Age Input
label = Label(frame, text='Age:')
label.grid(row=3, column=0)
entry_age = Entry(frame)
entry_age.grid(row=3, column=1)

#Save Button
button = Button(frame, text="Add", command=lambda:save_new_student(
        entry_name.get(),
        entry_address.get(),
        entry_age.get() 
    ))
button.grid(row=4, column=1, sticky=W+E)

#Search
label = Label(frame, text="Search Data")
label.grid(row=5, column=1)
label = Label(frame, text="Search By ID")
label.grid(row=6, column=0)
entry_id = Entry(frame)
entry_id.grid(row=6, column=1)
button = Button(frame, text="Search", command=lambda:search_student(entry_id.get()))
button.grid(row=6, column=2)

display_students()

root.mainloop()
