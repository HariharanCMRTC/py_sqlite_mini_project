import sqlite3

class readData:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def readStudentData(self,sid):
        self.cur.execute('''
            SELECT * FROM STUDENTS WHERE sid = ?
        ''',(sid,))
        self.conn.commit()
        s_details = self.cur.fetchone()
        print(f"Student: {s_details}")
        # print(f"----------------------------Student Data with sid={sid} deleted successfully--------------------------")

    def readCourseData(self,cid):
        self.cur.execute('''
            SELECT * FROM COURSES WHERE cid = ?
        ''',(cid,))
        c_details = self.cur.fetchone()
        print(f"Course: {c_details}")
        self.conn.commit()
        # print(f"----------------------------Course Data with course ID={cid} deleted successfully--------------------------")

    def readTransactionalData(self,tid):
        self.cur.execute('''
            SELECT * FROM trans WHERE tid = ?
        ''',(tid,))
        t_details = self.cur.fetchone()
        print(f"Transaction: {t_details}")
        self.conn.commit()
        # print(f"----------------------------Transactional Data with sid={tid} deleted successfully--------------------------")
