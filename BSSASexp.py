from tkinter import *
from PIL import ImageTk, Image
import sqlite3

dbase = sqlite3.connect('attendance_data.db')
curs = dbase.cursor()

dbase.execute("""CREATE TABLE IF NOT EXISTS employees_attendance (
            name text,
            department text,
            attendance text,
            date text
            )""")




##root = Tk()
##root.title('ByronsSuperSweetAttendanceSuite')
##root.geometry("400x500")


dbase.commit()
dbase.close()
    




















def edit():
    global editort
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()
    
    editort = Tk()
    editort.title('EditOrt')
    editort.geometry("400x135")

    record_id = delete_box.get()
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()
    curs.execute("SELECT * FROM employees_attendance WHERE oid = " + record_id)
    records = curs.fetchall()
     
    global edort_name
    global edort_department
    global edort_attendance
    global edort_date

    edort_name = Entry(editort, width=30)
    edort_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    edort_department = Entry(editort, width=30)
    edort_department.grid(row=1, column=1)
    edort_attendance = Entry(editort, width=30)
    edort_attendance.grid(row=2, column=1)
    edort_date = Entry(editort, width=30)
    edort_date.grid(row=3, column=1)
    





    name_label = Label(editort, text="Name")
    name_label.grid(row=0, column=0, pady=(10, 0) )
    department_label = Label(editort, text="Department")
    department_label.grid(row=1, column=0)
    attendance_label = Label(editort, text="Attendance")
    attendance_label.grid(row=2, column=0)
    date_label = Label(editort, text="Date(yyyy-mm-dd)")
    date_label.grid(row=3, column=0)

    for record in records:
        edort_name.insert(0, record[0])
        edort_department.insert(0, record[1])
        edort_attendance.insert(0, record[2])
        edort_date.insert(0, record[3])


    edit_btn = Button(editort, text="Save Changes", command=update)
    edit_btn.grid(row=7, column=0, columnspan=2, pady=3, padx=(6, 33), ipadx=137)
global editort
def update():
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()
    record_id = delete_box.get()
    
    curs.execute("""UPDATE employees_attendance SET
            name = :name,
            department = :department,
            attendance = :attendance,
            date = :date

            WHERE oid = :oid""",
            {
            'name': edort_name.get(),
            'department': edort_department.get(),
            'attendance': edort_attendance.get(),
            'date': edort_date.get(),
            'oid': record_id
            })
    dbase.commit()
    dbase.close()
 
    editort.destroy()






def delete():
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()

    curs.execute("DELETE from employees_attendance WHERE oid= " + delete_box.get())

    dbase.commit()
    
    dbase.close()



   

def submit():
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()
    
    
   

     # insert into table
    curs.execute("INSERT INTO employees_attendance VALUES (:name, :department, :attendance, :date)",
            {'name': name.get(),
            'department': department.get(),
            'attendance': attendance.get(),
            'date': date.get()})


    dbase.commit()
    dbase.close()

    name.delete(0, END)
    department.delete(0, END)
    attendance.delete(0, END)
    date.delete(0, END)



def query():
    dbase = sqlite3.connect('attendance_data.db')
    curs = dbase.cursor()
    curs.execute("SELECT *,oid FROM employees_attendance")
    records = curs.fetchall()
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + "\t" + "\t" + str(record[4]) + "\n"

    query_window = Tk()
    query_window.title('Database Entries')
    query_window.geometry("400x500")

    query_label = Label(query_window, text=print_records)
    query_label.grid(row=0, column=0, columnspan=2)
    

    dbase.commit()
##    dbase.close()

root = Tk()
root.title('ByronsSuperSweetAttendanceSuite')
root.geometry("400x500")

dbase = sqlite3.connect('attendance_data.db')
curs = dbase.cursor()

name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))
department = Entry(root, width=30)
department.grid(row=1, column=1)
attendance = Entry(root, width=30)
attendance.grid(row=2, column=1)
date = Entry(root, width=30)
date.grid(row=3, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=6, column=1, pady=3)






name_label = Label(root, text="Name")
name_label.grid(row=0, column=0, pady=(10, 0) )
department_label = Label(root, text="Department")
department_label.grid(row=1, column=0)
attendance_label = Label(root, text="Attendance")
attendance_label.grid(row=2, column=0)
date_label = Label(root, text="Date(yyyy-mm-dd)")
date_label.grid(row=3, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=6, column=0, pady=3)



dbase = sqlite3.connect('attendance_data.db')
curs = dbase.cursor()












sbmt_btn = Button(root, text="Add Entry To Database", command=submit)
sbmt_btn.grid(row=4, column=0, columnspan=2, pady=3, padx=8, ipadx=105)

query_btn = Button(root, text="Show Entries", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=3, padx=10, ipadx=137)


delete_btn = Button(root, text="Delete Entry", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=3, padx=10, ipadx=137)

edit_btn = Button(root, text="Edit Entry", command=edit)
edit_btn.grid(row=7, column=0, columnspan=2, pady=3, padx=10, ipadx=144)



dbase.commit()
dbase.close()

mainloop()
