import sqlite3

class updateData:
    def __init__(self) :
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()
    
    def updateStudentId(self,new_sid,old_sid):
        self.cur.execute('''
            UPDATE STUDENTS SET sid = ? WHERE sid = ?
        ''', (new_sid, old_sid))
        self.conn.commit()

    def updateStudentEmail(self,new_email,sid):
        self.cur.execute('''
            UPDATE STUDENTS SET email = ? WHERE sid = ?
        ''', (new_email, sid))
        self.conn.commit()
        print(f"----------------------------{new_email} added successfully--------------------------")

    def updateStudentCity(self,new_city,sid):
        self.cur.execute('''
            UPDATE STUDENTS SET city = ? WHERE sid = ?
        ''', (new_city, sid))
        self.conn.commit()
        print(f"----------------------------{new_city} added successfully--------------------------")

    def updateStudentName(self,new_sname,sid):
        self.cur.execute('''
            UPDATE STUDENTS SET sname = ? WHERE sid = ?
        ''', (new_sname, sid))
        self.conn.commit()
        print(f"----------------------------{new_sname} added successfully--------------------------")


    def updateCourseId(self,new_cid,old_cid):
        self.cur.execute('''
            UPDATE COURSE SET cid = ? WHERE cid = ?
        ''', (new_cid, old_cid))
        self.conn.commit()

    def updateCourseName(self,new_cname,cid):
        self.cur.execute('''
            UPDATE COURSE SET cname = ? WHERE cid = ?
        ''', (new_cname, cid))
        self.conn.commit()
        print(f"----------------------------{new_cname} added successfully--------------------------")

    def updateCoursePrice(self,new_price,cid):
        self.cur.execute('''
            UPDATE COURSE SET price = ? WHERE cid = ?
        ''', (new_price, cid))
        self.conn.commit()
        print(f"----------------------------{new_price} added successfully--------------------------")
    
    def updateCourseSid(self,new_sid,cid):
        self.cur.execute('''
            UPDATE COURSE SET sid = ? WHERE cid = ?
        ''', (new_sid, cid))
        self.conn.commit()
        print(f"----------------------------{new_sid} added successfully--------------------------")
    def updateTransactionId(self,new_tid,tid):
        self.cur.execute('''UPDATE INTO trans SET
                        tid = ? WHERE tid = ?
                        ''',(new_tid,tid))
        self.conn.commit()
        print(f"----------------------------New transaction ID '{new_tid}' added successfully--------------------------")
