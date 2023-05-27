from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import time
import datetime
from tkinter import messagebox

root = Tk()
root.geometry()
root.title("Warung Makan Bu R")
root.configure(background='black')

mylist = []


# --------------------Fungsi------------------------------------------
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = " "
    text_Input.set(" ")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = " "


def iExit():
    qExit = messagebox.askyesno("Keluar Aplikasi", "Anda Yakin Akan Keluar Aplikasi?")
    if qExit:
        root.destroy()
        return


def Reset():
    Tax.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    SubTotal.set("0")
    txtGorengan.delete(0)
    txtKopi.delete(0)
    txtKerupuk.delete(0)
    txtPaket6.delete(0)
    txtPaket5.delete(0)
    txtPaket3.delete(0)
    txtPaket2.delete(0)
    txtPaket1.delete(0)
    txtPaket4.delete(0)
    txtEsJeruk.delete(0)
    txtTehManis.delete(0)
    txtKopi.delete(0)

    Total.set("0")
    text_Input.set("0")
    Ticketclass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destinations.set("")
    To_Destinations.set("")
    Fee_Price.set("")

    mylist = []
    txtReceipt.delete(1.0, 'end')


def total():
    global mylist
    mylist = []
    if var4.get() == 1:
        q = int(txtPaket1.get())
        Cost = 8000 * q
        print(Cost)
        mylist.append(['Paket Nasi Murah', q, 8000, Cost])
    if var5.get() == 1:
        q = int(txtPaket2.get())
        Cost = 7000 * q
        mylist.append(['Paket Nasi Liwet', q, 7000, Cost])
    if var6.get() == 1:
        q = int(txtPaket3.get())
        Cost = 5000 * q
        mylist.append(['Paket Nasi Kuning', q, 5000, Cost])
    if var7.get() == 1:
        q = int(txtPaket4.get())
        Cost = 15000 * q
        mylist.append(['Paket Nasi Padang', q, 15000, Cost])
    if var8.get() == 1:
        q = int(txtPaket5.get())
        Cost = 10000 * q
        mylist.append(['Paket Nasi Ayam', q, 10000, Cost])
    if var9.get() == 1:
        q = int(txtPaket6.get())
        Cost = 12000 * q
        mylist.append(['Paket Nasi Ikan', q, 12000, Cost])

    if var1.get() == 1:
        q = int(txtTehManis.get())
        Cost = 3000 * q
        mylist.append(['Teh Manis', q, 3000, Cost])

    if var2.get() == 1:
        q = int(txtEsJeruk.get())
        Cost = 4000 * q
        mylist.append(['Es Jeruk', q, 4000, Cost])

    if var3.get() == 1:
        q = int(txtKopi.get())
        Cost = 5000 * q
        mylist.append(['Kopi', q, 5000, Cost])

    if var13.get() == 1:
        q = int(txtSambal.get())
        Cost = 2000 * q
        mylist.append(['Sambal Matah', q, 2000, Cost])

    if var14.get() == 1:
        q = int(txtKerupuk.get())
        Cost = 1000 * q
        mylist.append(['Kerupuk', q, 1000, Cost])

    if var15.get() == 1:
        q = int(txtGorengan.get())
        Cost = 1500 * q
        mylist.append(['Gorengan', q, 1500, Cost])
        print(mylist)

    print(mylist)
    txtb123 = ''
    txtReceipt.insert('insert', 'Item\tquantity\tcost\ttotal\n')
    for i in mylist:
        txtb123 += str(i[0]) + "\t   " + str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + "\n"
    txtReceipt.insert('insert', txtb123)
    txtReceipt.insert('insert', '\t\t\t%d\n' % (sum([i[3] for i in mylist])))


import win32printing


def GenrateRec():
    printing.PrintReceipt(random.randint(1, 10000000000), mylist, sum([i[3] for i in mylist]))


# ------------------------------------Variables---------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
Tax = StringVar()
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
SubTotal = StringVar()
Total = StringVar()
text_Input = StringVar()
operator = ""
Tax = IntVar()
# -----------------------------Frame work---------------------------------------------------------------
Tops = Frame(root, width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, relief='raise')
f2.pack(side=RIGHT)

frameTopRight = Frame(f2, width=440, height=650, bd=12, relief='raise')
frameTopRight.pack(side=TOP)
frameBottomRight = Frame(f2, width=440, height=50, bd=16, relief='raise')
frameBottomRight.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=8, relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=330, bd=6, relief='raise')
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft2.pack(side=RIGHT)
"""topLeft3=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topLeft3.pack(side=RIGHT)"""

bottomleft1 = Frame(f2a, width=450, height=450, bd=14, relief='raise')
bottomleft1.pack(side=LEFT)
bottomleft2 = Frame(f2a, width=450, height=450, bd=14, relief='raise')
bottomleft2.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
lbltitle = Label(Tops, font=('arial', 40, 'bold'), text="  Warung Makan Bu R  ", bd=10, width=41, justify='left')
lbltitle.grid(row=0, column=0)

# ------------------------------------Kalkulator-----------------------------------------------
text_Input = StringVar()
txtDisplay = Entry(bottomleft2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=10, bg="powder blue", width=40,
                   justify="right")
txtDisplay.grid(columnspan=4)

btn7 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="7", bg="powder blue",
              width=4, command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="8", bg="powder blue",
              width=4, command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="9", bg="powder blue",
              width=4, command=lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="+", bg="powder blue",
                  command=lambda: btnClick("+"), width=4).grid(row=2, column=3)
# -----------------------------------------------------------------------------------------------------------------------
btn4 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="4", bg="powder blue",
              width=4, command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="5", bg="powder blue",
              width=4, command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="6", bg="powder blue",
              width=4, command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="-",
                     bg="powder blue", command=lambda: btnClick("-"), width=4).grid(row=3, column=3)

# -----------------------------------------------------------------------------------------------------------------------------

btn1 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="1", bg="powder blue",
              width=4, command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="2", bg="powder blue",
              width=4, command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="3", bg="powder blue",
              width=4, command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="*", bg="powder blue",
                  command=lambda: btnClick("*"), width=4).grid(row=4, column=3)
# -----------------------------------------------------------------------------------------------------------------------------------------------------
btn0 = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="0", bg="powder blue",
              width=4, command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="C", bg="powder blue",
                  width=4, command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="=",
                   bg="powder blue", width=4, command=btnEqualsInput).grid(row=5, column=2)

Division = Button(bottomleft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="/", bg="powder blue",
                  command=lambda: btnClick("/"), width=4).grid(row=5, column=3)
# -----------------------------------------------------------------------------------------------------------------

lblReceipt = Label(frameTopRight, font=('arial', 16, 'bold'), text="Receipt", bd=10, width=41, height=3,
                   justify='center')
lblReceipt.grid(row=0, column=0)

txtReceipt = Text(frameBottomRight, width=50, height=20, bg='white', bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0, columnspan=4)

btnTotal = Button(frameBottomRight, text='Total', padx=2, pady=2, bd=2, fg='black', font=('arial', 20, 'bold'),
                  width=6, height=1, command=total).grid(row=7, column=0)

btnClear = Button(frameBottomRight, text='Clear', padx=2, pady=2, bd=2, fg='black', font=('arial', 20, 'bold'),
                  width=6, height=1, command=Reset).grid(row=7, column=1)

btnReceipt = Button(frameBottomRight, text='Receipt', padx=2, pady=2, bd=2, fg='black', font=('arial', 20, 'bold'),
                    width=6, height=1, command=GenrateRec).grid(row=7, column=2)

btnExit = Button(frameBottomRight, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 20, 'bold'),
                 width=6, height=1, command=iExit).grid(row=7, column=3)

# ---------------------------------------------------------
lblType = Label(topLeft1, font=('arial', 22, 'bold'), text="Minuman", bd=8)
lblType.grid(row=0, column=0, sticky=W)

esTeh = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text="Teh Manis      2000", variable=var1, onvalue=1,
                    offvalue=0)
esTeh.grid(row=1, column=0, sticky=W)
txtTehManis = Spinbox(topLeft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtTehManis.grid(row=1, column=1)

esJeruk = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text="Es Jeruk    3000", variable=var2, onvalue=1,
                      offvalue=0)
esJeruk.grid(row=2, column=0, sticky=W)
txtEsJeruk = Spinbox(topLeft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtEsJeruk.grid(row=2, column=1)

kopi = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text="Kopi    5000", variable=var3, onvalue=1,
                   offvalue=0)
kopi.grid(row=3, column=0, sticky=W)
txtKopi = Spinbox(topLeft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtKopi.grid(row=3, column=1)
# ------------------------------Menu---------------------------------------------------------------------------
lblType = Label(bottomleft1, font=('arial', 22, 'bold'), text="Makanan", bd=8)
lblType.grid(row=0, column=0, sticky=N)

lblPaket1 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Murah        8000", variable=var4,
                        onvalue=1,
                        offvalue=0)
lblPaket1.grid(row=3, column=0)
txtPaket1 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket1.grid(row=3, column=1)

lblPaket2 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Liwet        7000", variable=var5,
                        onvalue=1,
                        offvalue=0)
lblPaket2.grid(row=4, column=0)
txtPaket2 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket2.grid(row=4, column=1)

lblPaket3 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Kuning      5000", variable=var6,
                        onvalue=1,
                        offvalue=0)
lblPaket3.grid(row=5, column=0)
txtPaket3 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket3.grid(row=5, column=1)

lblPaket4 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Padang      15000", variable=var7,
                        onvalue=1,
                        offvalue=0)
lblPaket4.grid(row=6, column=0)
txtPaket4 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket4.grid(row=6, column=1)

lblPaket5 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Ayam   10000", variable=var8,
                        onvalue=1,
                        offvalue=0)
lblPaket5.grid(row=7, column=0)
txtPaket5 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket5.grid(row=7, column=1)

lblPaket6 = Checkbutton(bottomleft1, font=('arial', 20, 'bold'), text="Paket Nasi Ikan     12000", variable=var9,
                        onvalue=1,
                        offvalue=0)
lblPaket6.grid(row=8, column=0)
txtPaket6 = Spinbox(bottomleft1, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtPaket6.grid(row=8, column=1)

# --------------------------------------------------------------------------------------------------

"""lblSelect=Label(topLeft3,font=('arial',22,'bold'),text="Customize your Cup",bd=8)
lblSelect.grid(row=0,column=0,sticky=W,columnspan=10)
lblDestinations=Label(topLeft3,font=('arial',22,'bold'),text="Categories",bd=8)
lblDestinations.grid(row=1,column=0,sticky=W)

cboDestination=ttk.Combobox(topLeft3,textvariable=var12,state='readonly',fon=('arial',20),width=8)
cboDestination['value']=(' ', 'Avengers',
    'Dc legends',         
     'Classic',
    'Barcelona ',
    'Real Madrid'
     )
     

cboDestination.current(0)
cboDestination.grid(row=1,column=1)

chkSmall=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Small",variable=var10,onvalue=1,offvalue=0)
chkSmall.grid(row=3,column=0,sticky=W)
chkLarge=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Large",variable=var11,onvalue=1,offvalue=0)
chkLarge.grid(row=4,column=0,sticky=W)"""

# --------------------------------------------------------------------------------------------------------
lblPastry = Label(topLeft2, font=('arial', 22, 'bold'), text="Tambahan ", bd=8)
lblPastry.grid(row=0, column=0, sticky=W)

lblSambal = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text="Sambal Matah  2000", variable=var13,
                        onvalue=1, offvalue=0)
lblSambal.grid(row=1, column=0, sticky=W)
txtSambal = Spinbox(topLeft2, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtSambal.grid(row=1, column=1)

lblKerupuk = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text="Kerupuk   1000", variable=var14,
                         onvalue=1, offvalue=0)
lblKerupuk.grid(row=2, column=0, sticky=W)
txtKerupuk = Spinbox(topLeft2, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtKerupuk.grid(row=2, column=1)

lblGorengan = Checkbutton(topLeft2, font=('arial', 22, 'bold'), text="Gorengan 1500", variable=var15, onvalue=1,
                          offvalue=0)
lblGorengan.grid(row=3, column=0, sticky=W)
txtGorengan = Spinbox(topLeft2, from_=0, to=10, font=('arial', 16, 'bold'), bd=8, width=6, justify='left')
txtGorengan.grid(row=3, column=1)

# ---------------------------------------------------------------------------------------------------


root.mainloop()
