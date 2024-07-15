import sqlite3

class deleteData:
    def __init__(self) :
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def deleteStudentData(self,sid):
        self.cur.execute('''
            DELETE FROM STUDENTS WHERE sid = ?
        ''',(sid,))
        self.conn.commit()
        print(f"----------------------------Student Data with sid={sid} deleted successfully--------------------------")

    def deleteCourseData(self,cid):
        self.cur.execute('''
            DELETE FROM COURSES WHERE cid = ?
        ''',(cid,))
        self.conn.commit()
        print(f"----------------------------Course Data with course ID={cid} deleted successfully--------------------------")

    def deleteTransactionalData(self,tid):
        self.cur.execute('''
            DELETE FROM trans WHERE tid = ?
        ''',(tid,))
        self.conn.commit()
        print(f"----------------------------Transactional Data with sid={tid} deleted successfully--------------------------")
