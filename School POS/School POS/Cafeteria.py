from sqlite3.dbapi2 import Connection
import serial
from database import *
from functions import *

#Making neccesary variables
#comment out if you want to test without arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=3)

Meet = student('Meet', 'Patel', "75 567 534 412", "-2.50")
Bob = student("Bob", "dan", "234 456 34 321", "10.25")

#This is where all student objects will be stored
students = [Meet,Bob]


    

data = data_base()
conn = sqlite3.connect('student_objects.db')
c = conn.cursor()

for people in students:
    data.insert_stduent(people)    

print(data.get_student_with_RFID(Meet.rfid))

conn.close()