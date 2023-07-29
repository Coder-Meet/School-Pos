from tkinter import *
from functions import *

root = Tk()

root.geometry("1920x1080")
leftframe = Frame(root)
leftframe.pack(side='left')
pos = POS()
label_menu = Label(root,text="Menu", width=100, fg="black", font=("Arial",35))

order_button = Button(root, text="Take Orders", height=5, width=50, font=("Arial",25), bg="green", command=pos.take_orders)
lunchtime_button = Button(root, text="Lunch Time", height=5, width=50, font=("Arial",25), bg="green" , command=pos.complete_orders)
getdata_button = Button(root, text="See data",height=5, width=50, font=("Arial",25), bg="green", command=pos.get_stats)

label_menu.pack(pady=10,fill="both")
order_button.pack(pady=5, fill="both")
lunchtime_button.pack(pady=5, fill = "both")
getdata_button.pack(pady=5,fill="both")


root.mainloop()