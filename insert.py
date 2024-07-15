import sqlite3

class insertData:
    def __init__(self) :
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()
    
    def insertStudent(self,sid,sname,email,city):
        self.cur.execute('''INSERT INTO STUDENTS VALUES(?,?,?,?)
                        ''',(sid,sname,email,city))
        self.conn.commit()
        print("----------------------------Student Data added successfully--------------------------")

    def insertCourse(self,cid,cname,price,sid):
        self.cur.execute('''INSERT INTO COURSE VALUES(?,?,?,?)
                        ''',(cid,cname,price,sid))
        self.conn.commit()
        print("----------------------------Course Data added successfully--------------------------")
    
    def insertTrans(self,tid,sid,cid,method):
        self.cur.execute('''INSERT INTO trans VALUES(?,?,?,?)
                        ''',(tid,sid,cid,method))
        self.conn.commit()
        print("----------------------------Transaction Data added successfully--------------------------")

