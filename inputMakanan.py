from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Warung Makan Bu R")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1100
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `makanan` (idMakanan INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, kodeMakanan TEXT, "
        "namaMakanan TEXT, jenisMakanan TEXT, stokMakanan TEXT, hargaPokok TEXT, hargaJual TEXT)")


def Create():
    if KODEMAKANAN.get() == "" or NAMAMAKANAN.get() == "" or JENISMAKANAN.get() == "" or STOKMAKANAN.get() == "" or \
            HARGAPOKOK.get() == \
            "" or HARGAJUAL.get() == "":
        txt_result.config(text="Data Tidak Boleh Kosong!", fg="red")
    else:
        Database()
        cursor.execute(
            "INSERT INTO `makanan` (kodeMakanan, namaMakanan, jenisMakanan, stokMakanan, hargaPokok, hargaJual) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            (str(KODEMAKANAN.get()), str(NAMAMAKANAN.get()), str(JENISMAKANAN.get()), str(STOKMAKANAN.get()),
             str(HARGAPOKOK.get()), str(HARGAJUAL.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `makanan` ORDER BY `idMakanan` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        KODEMAKANAN.set("")
        NAMAMAKANAN.set("")
        JENISMAKANAN.set("")
        STOKMAKANAN.set("")
        HARGAPOKOK.set("")
        HARGAJUAL.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Data Berhasil Disimpan!", fg="green")


def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `makanan` ORDER BY `namaMakanan` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Lihat Data!", fg="black")


def Update():
    Database()
    if NAMAMAKANAN.get() == "":
        txt_result.config(text="Pilih Nama Makanan!", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute(
            "UPDATE `makanan` SET `kodeMakanan` = ?, `namaMakanan` = ?, `jenisMakanan` =?,  `stokMakanan` = ?,  "
            "`hargaPokok` = ?, ""`hargaJual` = ? WHERE `idMakanan` = ?",
            (str(KODEMAKANAN.get()), str(NAMAMAKANAN.get()), str(JENISMAKANAN.get()), str(STOKMAKANAN.get()),
             str(HARGAPOKOK.get()),
             str(HARGAJUAL.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `makanan` ORDER BY `namaMakanan` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cursor.close()
        conn.close()
        KODEMAKANAN.set("")
        NAMAMAKANAN.set("")
        JENISMAKANAN.set("")
        STOKMAKANAN.set("")
        HARGAPOKOK.set("")
        HARGAJUAL.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Data berhasil diubah!", fg="black")


def OnSelected(event):
    global mem_id;
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    KODEMAKANAN.set("")
    NAMAMAKANAN.set("")
    JENISMAKANAN.set("")
    STOKMAKANAN.set("")
    HARGAPOKOK.set("")
    HARGAJUAL.set("")
    KODEMAKANAN.set(selecteditem[1])
    NAMAMAKANAN.set(selecteditem[2])
    STOKMAKANAN.set(selecteditem[4])
    HARGAPOKOK.set(selecteditem[5])
    HARGAJUAL.set(selecteditem[6])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)


def Delete():
    if not tree.selection():
        txt_result.config(text="Pilih data yang akan dihapus!", fg="red")
    else:
        result = tkMessageBox.askquestion('Warung Makan Bu R',
                                          'Datanya beneran mau dihapus?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `makanan` WHERE `idMakanan` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Data berhasil dihapus!", fg="black")


def Exit():
    result = tkMessageBox.askquestion('Warung Makan Bu R', 'Yakin mau keluar?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


KODEMAKANAN = StringVar()
NAMAMAKANAN = StringVar()
JENISMAKANAN = StringVar()
STOKMAKANAN = StringVar()
HARGAPOKOK = StringVar()
HARGAJUAL = StringVar()

Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
Radiobutton(RadioGroup, text="Makanan", variable=JENISMAKANAN, value="Makanan", font=('arial', 16)).pack(side=LEFT)
Radiobutton(RadioGroup, text="Minuman", variable=JENISMAKANAN, value="Minuman", font=('arial', 16)).pack(side=LEFT)

txt_title = Label(Top, width=900, font=('arial', 24), text="WARUNG MAKAN BU R - INPUT DATA MAKANAN")
txt_title.pack()
txt_KODEMAKANAN = Label(Forms, text="Kode Makanan:", font=('arial', 16), bd=15)
txt_KODEMAKANAN.grid(row=0, sticky="e")
txt_NAMAMAKANAN = Label(Forms, text="Nama Makanan:", font=('arial', 16), bd=15)
txt_NAMAMAKANAN.grid(row=1, sticky="e")
txt_JENISMAKANAN = Label(Forms, text="Jenis Makanan:", font=('arial', 16), bd=15)
txt_JENISMAKANAN.grid(row=2, sticky="e")
txt_STOKMAKANAN = Label(Forms, text="Stok Makanan:", font=('arial', 16), bd=15)
txt_STOKMAKANAN.grid(row=3, sticky="e")
txt_HARGAPOKOK = Label(Forms, text="Harga Pokok:", font=('arial', 16), bd=15)
txt_HARGAPOKOK.grid(row=4, sticky="e")
txt_HARGAJUAL = Label(Forms, text="Harga Jual:", font=('arial', 16), bd=15)
txt_HARGAJUAL.grid(row=5, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

KODEMAKANAN = Entry(Forms, textvariable=KODEMAKANAN, width=30)
KODEMAKANAN.grid(row=0, column=1)
NAMAMAKANAN = Entry(Forms, textvariable=NAMAMAKANAN, width=30)
NAMAMAKANAN.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
STOKMAKANAN = Entry(Forms, textvariable=STOKMAKANAN, width=30)
STOKMAKANAN.grid(row=3, column=1)
HARGAPOKOK = Entry(Forms, textvariable=HARGAPOKOK, width=30)
HARGAPOKOK.grid(row=4, column=1)
HARGAJUAL = Entry(Forms, textvariable=HARGAJUAL, show="*", width=30)
HARGAJUAL.grid(row=5, column=1)

btn_create = Button(Buttons, width=10, text="Simpan Data", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Lihat Data", command=Read)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Ubah Data", command=Update, state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Hapus Data", command=Delete)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Keluar", command=Exit)
btn_exit.pack(side=LEFT)

scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("IDMAKANAN", "KODEMAKANAN", "NAMAMAKANAN", "JENISMAKANAN", "STOKMAKANAN",
                                    "HARGAPOKOK", "HARGAJUAL"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('IDMAKANAN', text="ID Makanan", anchor=W)
tree.heading('KODEMAKANAN', text="Kode", anchor=W)
tree.heading('NAMAMAKANAN', text="Nama Makanan", anchor=W)
tree.heading('JENISMAKANAN', text="Jenis", anchor=W)
tree.heading('STOKMAKANAN', text="Stok", anchor=W)
tree.heading('HARGAPOKOK', text="Harga Pokok", anchor=W)
tree.heading('HARGAJUAL', text="Harga Jual", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

if __name__ == '__main__':
    root.mainloop()
