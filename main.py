from insert import insertData
from update import updateData
from delete import deleteData
from read import readData

insert_obj = insertData()
update_obj = updateData()
delete_obj = deleteData()
show = readData()

def main_menu():
    print("--------------STUDENT MANAGEMENT SYSTEM-------------")
    print("TO INSERT PRESS 1\nUPDATE PRESS 2\nTO DELETE PRESS 3\nREAD PRESS 4")
    print("TO EXIT PRESS 5")

def insert_data():
    print("1. STUDENT\n2. COURSE\n3. TRANSACTIONS")
    n = int(input("Enter your option: "))
    if n == 1:
        sid = int(input("Enter your ID: "))
        sname = input("Enter your name: ")
        email = input("Enter your email address: ")
        city = input("Enter your city: ")
        insert_obj.insertStudent(sid,sname,email,city)

    elif n == 2:
        cid = int(input("Enter your course ID: "))
        cname = input("Enter your course name: ")
        price = int(input("Enter the price of the course: "))
        sid = int(input("Enter your student ID: "))
        insert_obj.insertCourse(cid,cname,price,sid)

    elif n == 3:
        tid = int(input("Enter your Transaction ID: "))
        sid = input("Enter your student ID: ")
        cid = int(input("Enter your course ID: "))
        mode = input("Enter method of transaction: ")
        insert_obj.insertTrans(tid,sid,cid,mode)

def update_data():
    print("1. STUDENT\n2. COURSE\n3. TRANSACTIONS")
    n = int(input("Enter your option: "))
    if n == 1:
        print("1. UPDATE sid\n2. UPDATE sname\n3. UPDATE email\n4. UPDATE city")
        update_option = int(input("Enter your choice: "))
        if update_option == 1:
            sid = int(input("Enter your old ID: "))
            # sname = input("Enter your name: ")
            new_sid = int(input("Enter your new ID: "))
            update_obj.updateStudentId(new_sid,sid)
        elif update_option == 2:
            sid = int(input("Enter your ID: "))
            new_sname = input("Enter your new name: ")
            update_obj.updateStudentName(new_sname,sid)
        elif update_option == 3:
            sid = int(input("Enter your ID: "))
            new_email = input("Enter your new email: ")
            update_obj.updateStudentEmail(new_email,sid)
        elif update_option == 4:
            sid = int(input("Enter your ID: "))
            new_city = input("Enter your new city: ")
            update_obj.updateStudentCity(new_city,sid)

    elif n == 2:
        print("1. UPDATE cid\n2. UPDATE cname\n3. UPDATE price\n4. UPDATE sid")
        update_option = int(input("Enter your choice: "))
        if update_option == 1:
            cid = int(input("Enter your old course ID: "))
            # sname = input("Enter your name: ")
            new_cid = int(input("Enter your new course ID: "))
            update_obj.updateCourseId(new_cid,cid)
        elif update_option == 2:
            cid = int(input("Enter your ID: "))
            new_cname = input("Enter your new course name: ")
            update_obj.updateCourseName(new_cname,cid)
        elif update_option == 3:
            cid = int(input("Enter your ID: "))
            new_price = input("Enter your new price: ")
            update_obj.updateCoursePrice(new_price,cid)
        elif update_option == 4:
            cid = int(input("Enter your ID: "))
            new_sid = input("Enter your new sid: ")
            update_obj.updateCourseSid(new_sid,cid)

    elif n == 3:
        print("UPDATE transaction ID")
        tid = int(input("Enter your transaction ID: "))
        new_tid = int(input("Enter your new transaction ID: "))
        update_obj.updateTransId(new_tid,tid)

def delete_date():
    print("1. STUDENT \n2. COURSE\n3. TRANSACTIONS")
    n = int(input("Enter your option: "))
    if n == 1:
        sid = int(input("Enter your student ID: "))
        delete_obj.deleteStudentData(sid)

def read_data():
    print("1. STUDENT \n2. COURSE\n3. TRANSACTIONS")
    n = int(input("Enter your option: "))
    if n == 1:
        sid = int(input("Enter your student ID: "))
        show.readStudentData(sid)
    elif n == 2:
        cid = int(input("Enter your course ID: "))
        show.readCourseData(cid)
    elif n == 3:
        tid = int(input("Enter your transaction ID: "))
        show.readTransactionalData(tid)

while(True):
    main_menu()
    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        delete_date()
    elif choice == 4:
        read_data()
    elif choice == 5:
        break
    else:
        print("INVALID INPUT! CHOOSE AGAIN")
