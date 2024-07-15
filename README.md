# Student Management System

This project is a simple Student Management System implemented in Python using SQLite as the database. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on students, courses, and transactions data. Additionally, it ensures that deleting a student profile will automatically delete related data in the transactions and courses tables using cascading delete functionality.

## Features

- **Create**: Add new students, courses, and transactions to the database.
- **Read**: Retrieve and display details of students, courses, and transactions.
- **Update**: Modify existing records in the database.
- **Delete**: Remove students from the database along with their related courses and transactions using cascading delete.

## Prerequisites

- Python 3.x
- SQLite

## Setup and Usage

1. **Clone the repository**

    ```sh
    git clone https://github.com/your-username/student-management-system.git
    cd student-management-system
    ```

2. **Run the setup script**

    This script creates the database and populates it with some example data.

    ```python
    import sqlite3
    import os

    # Function to create and populate the database for demonstration purposes
    def setup_database():
        conn = sqlite3.connect("sms.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.cursor()

        # Create tables
        cur.execute('''
        CREATE TABLE IF NOT EXISTS STUDENTS(
            sid INTEGER PRIMARY KEY,
            sname TEXT,
            email TEXT,
            city TEXT
        )
        ''')

        cur.execute('''
        CREATE TABLE IF NOT EXISTS COURSES(
            cid INTEGER PRIMARY KEY,
            cname TEXT,
            price INTEGER,
            sid INTEGER,
            FOREIGN KEY(sid) REFERENCES STUDENTS(sid) ON DELETE CASCADE
        )
        ''')

        cur.execute('''
        CREATE TABLE IF NOT EXISTS TRANSACTIONS(
            tid INTEGER PRIMARY KEY,
            sid INTEGER,
            cid INTEGER,
            mode TEXT,
            FOREIGN KEY(sid) REFERENCES STUDENTS(sid) ON DELETE CASCADE,
            FOREIGN KEY(cid) REFERENCES COURSES(cid) ON DELETE CASCADE
        )
        ''')

        # Insert example data
        cur.execute("INSERT INTO STUDENTS (sid, sname, email, city) VALUES (1, 'John Doe', 'john@example.com', 'New York')")
        cur.execute("INSERT INTO COURSES (cid, cname, price, sid) VALUES (101, 'Math', 200, 1)")
        cur.execute("INSERT INTO TRANSACTIONS (tid, sid, cid, mode) VALUES (1001, 1, 101, 'Credit Card')")
        conn.commit()
        conn.close()

    # Function to delete the database file
    def delete_database(db_path):
        # Ensure all connections are closed
        try:
            conn = sqlite3.connect(db_path)
            conn.close()
        except Exception as e:
            print(f"Error closing the connection: {e}")

        # Delete the database file
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Database file {db_path} deleted.")
        else:
            print(f"Database file {db_path} does not exist.")

    # Set up the database for demonstration purposes
    setup_database()

    # Path to your SQLite database file
    db_path = "sms.db"

    # Delete the database file
    delete_database(db_path)
    ```

3. **Run the main script**

    The main script allows you to interact with the Student Management System through a simple command-line interface.

    ```python
    from insert import insertData
    from update import updateData
    from delete import deleteData
    from read import readData

    insert_obj = insertData()
    update_obj = updateData()
    delete_obj = deleteData()
    show = readData()

    print("--------------STUDENT MANAGEMENT SYSTEM-------------")
    print("TO INSERT PRESS 1, UPDATE PRESS 2\nTO DELETE PRESS 3, READ PRESS 4")
    print("TO EXIT PRESS 5")

    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
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

    elif choice == 2:
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
            print("1. UPDATE cid\n2. UPDATE cname\n3. UPDATE price")
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

        elif n == 3:
            print("UPDATE transaction ID")
            tid = int(input("Enter your transaction ID: "))
            new_tid = int(input("Enter your new transaction ID: "))
            update_obj.updateTransId(new_tid,tid)

    elif choice == 3:
        print("1. STUDENT \n2. COURSE\n3. TRANSACTIONS")
        n = int(input("Enter your option: "))
        if n == 1:
            sid = int(input("Enter your student ID: "))
            delete_obj.deleteStudentData(sid)

    elif choice == 4:
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

    ```

## How to Delete the Database File

If you need to delete the entire database file, ensure that all connections are closed before attempting to remove the file.

```python
import os
import sqlite3

# Function to delete the database file
def delete_database(db_path):
    # Ensure all connections are closed
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
    except Exception as e:
        print(f"Error closing the connection: {e}")

    # Delete the database file
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Database file {db_path} deleted.")
    else:
        print(f"Database file {db_path} does not exist.")

# Path to your SQLite database file
db_path = "sms.db"

# Delete the database file
delete_database(db_path)
