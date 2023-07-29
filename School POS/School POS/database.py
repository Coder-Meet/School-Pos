import sqlite3

#Connects to data base
conn = sqlite3.connect('student_objects.db')

#Makes the cursor
c = conn.cursor()

#Uncomment to make table
#c.execute("""CREATE TABLE student_info (First text,Last text,RFID text,id integer,balance text)""")

#Makes class
class data_base():

    #Enters student in data base
    def insert_stduent(self,student_object):
        with conn:
            #Optional if statement. Could check if rfid already exist in database befor hand.
            if c.execute("SELECT 1 FROM student_info WHERE RFID = :rfid",{'rfid': student_object.rfid}).fetchone() == None:
                c.execute("INSERT INTO student_info VALUES (:first, :last, :RFID, :id, :balance)", {"first":student_object.first,"last":student_object.last, "RFID":student_object.rfid, "id":student_object.id, "balance":student_object.balance})
   
    #Removes student from data base
    def remove_student(self,student_object):
        with conn:
            c.execute("DELETE from student_info WHERE first = :first AND last = :last",
                        {'first': student_object.first, 'last': student_object.last})

    #Updates balnce for students in data base
    def update_balance(self,student_object, balance):
        with conn:
            c.execute("""UPDATE student_info SET 'balance' = :balance
                        WHERE first = :first AND last = :last""",
                        {'first': student_object.first, 'last': student_object.last, 'balance': balance})

    #gets student info given rfid tag as string
    def get_student_with_RFID(self,rfid):
        c.execute("SELECT * FROM student_info WHERE RFID = :rfid", {'rfid': rfid})
        return c.fetchone()

#conn.close()