import backend
from tkinter import *
import time


# blue = #100d46
# light = #afade2
# button color = light blue

# ----------------------------------------------function-----------------------------------------------


def search_command():
    console.delete(0, END)
    rang = backend.search(findE.get().strip().lower())
    if len(rang) == 0:
        console.insert(END, 'No such item is in store')
    for row in rang:
        st = ("There's {} item named {} each priced at ${}".format(row[3], row[1], row[2]))
        console.insert(END, st)


def sell_command():
    quant = sellQ.get()
    name = sellE.get().strip().lower()
    global prev, pres
    console.delete(0, END)
    if not quant.isnumeric():
        console.insert(END, 'Please enter a valid number of item')
        return 0
    if len(name) == 0:
        console.insert(END, 'Please enter a valid name')
        return 0
    # ----before search----
    row = backend.search(name)
    prev = 0
    if len(row) == 0:
        console.insert(END, 'No such item is in store')
    else:
        prev = row[0][3]
        if prev < int(quant):
            console.insert(END, "Not enough item in Stock..")
            st = ("There were {} item named {} each priced at ${}".format(row[0][3], row[0][1], row[0][2]))
            console.insert(END, st)
            return 0
        st = ("There were {} item named {} each priced at ${}".format(row[0][3], row[0][1], row[0][2]))
        console.insert(END, st)
    # ----checkout----
    backend.sellItem(name, quant)
    # ----after search----
    row = backend.search(name)
    pres = 0
    if len(row) == 0:
        console.insert(END, 'No such item is in store')
    else:
        pres = row[0][3]
        st = ("Now There's {} item named {} each priced at ${}".format(row[0][3], row[0][1], row[0][2]))
        console.insert(END, st)
    diff = prev - pres
    st2 = ("Item sold = {}".format(diff))
    console.insert(END, st2)


def add_command():
    console.delete(0, END)
    item_name = nameE.get().strip().lower()
    if len(item_name) == 0:
        console.insert(END, 'Item Name cannot name cannot be empty')
        return 0
    if not priceE.get().isnumeric():
        console.insert(END, 'Please enter a valid price of item')
        return 0
    item_price = int(priceE.get())
    if not addQ.get().isnumeric():
        console.insert(END, 'Please enter a valid number of item')
        return 0
    item_q = int(addQ.get())
    row = backend.search(item_name)

    if len(row) != 0:
        console.insert(END, 'Item already exists')
        console.insert(END, 'Hence adding all the items and updating the price')
        backend.update(item_name, item_price, item_q)
        for row in backend.view():
            st = ("{}) ITEMNAME= |{}| ITEMPRICE= ${} ITEMQUANTITY= {}".format(row[0], row[1], row[2], row[3]))
            console.insert(END, st)
        return 0

    backend.insert(item_name, item_price, item_q)
    console.insert(END, "Storage updated")
    row = backend.search(item_name)
    if len(row) == 0:
        console.insert(END, 'No such item is in store')
    else:
        st = ("There were {} item named {} each priced at ${}".format(row[0][3], row[0][1], row[0][2]))
        console.insert(END, st)


def view_command():
    console.delete(0, END)
    for row in backend.view():
        st = ("{}) ITEMNAME= |{}| ITEMPRICE= ${} ITEMQUANTITY= {}".format(row[0], row[1], row[2], row[3]))
        console.insert(END, st)


# --------------------------------------------------------------------------------------------------

localtime = time.asctime(time.localtime(time.time()))
font10 = '{Courier New} 10 normal'
font11 = '{U.S. 101} 30 bold'
font12 = '{Courier New} 12 bold'
font13 = '{Segoe UI} 15 bold'
font14 = '{Segoe UI} 15 normal'
font15 = '{Segoe UI} 10 normal'
font16 = '{Segoe UI} 13 bold'

root = Tk()
root.title('Pharmacy Store Management Application')
root.geometry('1028x660')
root.configure(bg='#100d46')
# -----title-----
title = Label(master=root, text='Pharmacy Store Management System', font=font11, bg='#100d46', fg='#afade2')
title.place(relx=0.10, rely=0.02, height=50, width=807)

timeLabel = Label(master=root, text=localtime, font=font16, bg='#100d46', fg='light blue')
timeLabel.place(relx=0.20, rely=0.12, height=20, width=607)

title = Label(master=root, text='by Pritam, Prantik, Rittika and Nilanjan', font=font16, bg='#100d46', fg='white')
title.place(relx=0.10, rely=0.16, height=50, width=807)

# -----find-----

findL = Label(master=root, text='FIND ITEMS', font=font13, bg='#100d46', fg='#afade2')
findL.place(relx=0.05, rely=0.3)

findText = StringVar()
findE = Entry(master=root, textvariable=findText)
findE.place(relx=0.2, rely=0.32, width=400)

b1 = Button(master=root, text="Search", bg="light blue", fg='#100d46', font=font12, command=search_command)
b1.place(relx=0.7, rely=0.32, width=150, height=22)
# -----sell-----
sellL = Label(master=root, text='SELL ITEMS', font=font13, bg='#100d46', fg='#afade2')
sellL.place(relx=0.05, rely=0.4)

SellText = StringVar()
sellE = Entry(master=root, textvariable=SellText)
sellE.place(relx=0.2, rely=0.42, width=300)

sellN = Label(master=root, text='Num', font=font14, bg='#100d46', fg='#afade2')
sellN.place(relx=0.52, rely=0.40)

SellQ = StringVar()
sellQ = Entry(master=root, textvariable=SellQ)
sellQ.place(relx=0.60, rely=0.42, width=40)

b2 = Button(master=root, text="Checkout", bg="light blue", fg='#100d46', font=font12, command=sell_command)
b2.place(relx=0.7, rely=0.42, width=150, height=22)
# -----add-----
addL = Label(master=root, text='ADD ITEMS', font=font13, bg='#100d46', fg='#afade2')
addL.place(relx=0.05, rely=0.5)

addName = Label(master=root, text='Item Name', font=font14, bg='#100d46', fg='#afade2')
addName.place(relx=0.2, rely=0.5)

nameText = StringVar()
nameE = Entry(master=root, textvariable=nameText)
nameE.place(relx=0.33, rely=0.52, width=300)

addPrice = Label(master=root, text='Item Price', font=font14, bg='#100d46', fg='#afade2')
addPrice.place(relx=0.66, rely=0.5)

priceText = StringVar()
priceE = Entry(master=root, textvariable=priceText)
priceE.place(relx=0.78, rely=0.52, width=65)

addNum = Label(master=root, text='Num of Item', font=font14, bg='#100d46', fg='#afade2')
addNum.place(relx=0.2, rely=0.58)

addQ = StringVar()
addQ = Entry(master=root, textvariable=addQ)
addQ.place(relx=0.4, rely=0.6, width=40)

b3 = Button(master=root, text="INCLUDE ITEMS", bg="light blue", fg='#100d46', font=font12, command=add_command)
b3.place(relx=0.65, rely=0.60, width=200, height=30)

# -----console-----

console = Listbox(root, height=6, width=35, font=font12)
console.place(relx=0.2, rely=0.7, width=660, height=100)

sb = Scrollbar(master=root)
sb.place(relx=0.84, rely=0.7, height=100)

console.configure(yscrollcommand=sb.set)
sb.configure(command=console.yview)

b3 = Button(master=root, text="VIEW ALL ITEMS", bg="light blue", fg='#100d46', font=font12, command=view_command)
b3.place(relx=0.65, rely=0.88, width=200, height=30)

root.mainloop()
