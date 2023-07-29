from tkinter import *
from serial.serialutil import Timeout
import serial
import tkinter.messagebox
from database import *

class student():

    def __init__(self, first, last, RFID, balance):
        self.first = first
        self.last = last
        self.rfid = RFID
        self.id = generate_id()
        self.balance = balance

counter = -1

def generate_id():
    global counter
    counter+=1
    return counter

data = data_base()


arduino = serial.Serial("COM3",9600,timeout=3)

Meet = student("Meet",'Patel',"23 115 163 123","5.25")
Sanvi = student("Sanvi",'Patel',"177 62 230 81","10.75")
Darshi = student("Darshi",'Patel',"36 128 119 26","-2.50")
data.insert_stduent(Meet)
data.insert_stduent(Sanvi)
data.insert_stduent(Darshi)

#gets id from serial port
def get_id():
    global arduino
    arduino.close()
    arduino = serial.Serial("COM3",9600,timeout=3)
    
    number = arduino.readline()
    if len(number)<2:
        return None
    return str(number)[2:][:-6]


#All the funtionality of the code will be here. If rfid scanner is not wanting to be used name search is possible

def take_orders():
    global arduino, root
    root.destroy()
    root = Tk()
    root.geometry("1920x1080")
    back_button = Button(root, text="Go Back", height=5, width=50, font=("Arial",25), bg="green", command=home_page)
    back_button.pack()
    scan_label = Label(root,text="Scan a card", width=100, fg="black", font=("Arial",35))
    scan_label.pack()
    id = get_id()
    while id==None:
        answer = tkinter.messagebox.askokcancel("Message","Please scan a card")
        if answer==True:
            id = get_id()
        else:
            root.destroy()
            home_page()
            break
    
    info = data.get_student_with_RFID(id)
    scanned_label = Label(root,text=f"{info[0]} {info[1]} has a balance of {info[-1]}", width=100, fg="black", font=("Arial",35))
    scanned_label.pack()

    root.mainloop()



    #Will be limited to S for Soup and M for meal
    #Will not subtract money from account
    #if cash is paid it will add balance to account

def complete_orders():
    print("Lunch time")
    #Might have diffrent products to be able to buy
    #subtracts money from account
    #if user owes money will also show to remind them
    #If balance of id tag is zero either take back id tag or ask to refill it

def get_stats():
    print("Getting stats")
    #tells today sales
    #can access orders placed from morning
    #can see pending balances and money to be owed
    #can remove an account from database





root = Tk()

def home_page():
    global root
    root.destroy()
    root = Tk()
    root.geometry("1920x1080")

    label_menu = Label(root,text="Menu", width=100, fg="black", font=("Arial",35))

    order_button = Button(root, text="Take Orders", height=5, width=50, font=("Arial",25), bg="green", command=take_orders)
    lunchtime_button = Button(root, text="Lunch Time", height=5, width=50, font=("Arial",25), bg="green" , command=complete_orders)
    getdata_button = Button(root, text="See data",height=5, width=50, font=("Arial",25), bg="green", command=get_stats)

    label_menu.pack(pady=10,fill="both")
    order_button.pack(pady=5, fill="both")
    lunchtime_button.pack(pady=5, fill = "both")
    getdata_button.pack(pady=5,fill="both")


home_page()

root.mainloop()

