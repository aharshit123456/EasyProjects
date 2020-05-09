import tkinter
from tkinter import *

val = 0
addval = 0
subval = 0
mulval = 0
divval = 0


class Calculator:
    def __init__(self):
        root = tkinter.Tk()
        root.geometry("250x400+300+300")
        root.resizable(0, 0)
        root.title("Calculator")
        data = StringVar()
        opps = []

        # functions of btn clicked
        def btn_1_click():
            global val
            val = str(val) + "1"
            data.set(val)

        def btn_2_click():
            global val
            val = str(val) + "2"
            data.set(val)

        def btn_3_click():
            global val
            val = str(val) + "3"
            data.set(val)

        def btn_4_click():
            global val
            val = str(val) + "4"
            data.set(val)

        def btn_5_click():
            global val
            val = str(val) + "5"
            data.set(val)

        def btn_6_click():
            global val
            val = str(val) + "6"
            data.set(val)

        def btn_7_click():
            global val
            val = str(val) + "7"
            data.set(val)

        def btn_8_click():
            global val
            val = str(val) + "8"
            data.set(val)

        def btn_9_click():
            global val
            val = str(val) + "9"
            data.set(val)

        def btn_0_click():
            global val
            val = str(val) + "0"
            data.set(val)

        def btn_C_click():
            global val, addval,subval,mulval, divval
            val = 0
            addval = 0
            subval = 0
            mulval = 0
            divval = 0
            opps.clear()
            data.set(val)

        def add():
            global val, addval
            addval = val
            val = 0
            opps.append("add")
            data.set(val)

        def sub():
            global val, subval
            subval = val
            val = 0
            opps.append("sub")
            data.set(val)

        def mul():
            global val, mulval
            mulval = val
            val = 0
            opps.append("mul")
            data.set(val)

        def div():
            global val, divval
            divval = val
            val = 0
            opps.append("div")
            data.set(val)

        def result():
            global val, addval,subval,mulval, divval
            res = int(val)
            print(type(addval))
            for i in opps:
                if i == "add":
                    res += int(addval)
                elif i == "sub":
                    res -= int(subval)
                elif i == "mul":
                    res += int(mulval)
                elif i == "div":
                    res -= int(divval)
            data.set(res)
        # Label above rows declared and packed
        lb1 = Label(
            root,
            text="Label",
            anchor=SE,
            font=("Verdana", 18),
            bg="#000",
            fg="#FFF",
            border="5",
            textvariable=data
        )
        lb1.pack(expand=True, fill="both")
        # rows declaration
        btnrow1 = Frame(root, bg="#000000")
        btnrow1.pack(expand=True, fill="both")

        btnrow2 = Frame(root, bg="#00A")
        btnrow2.pack(expand=True, fill="both")

        btnrow3 = Frame(root, bg="#F0F")
        btnrow3.pack(expand=True, fill="both")

        btnrow4 = Frame(root, bg="#FFA")
        btnrow4.pack(expand=True, fill="both")
        btnfont = ("Verdana", 20)  # font
        # row 1 btn declaration
        btn1 = Button(
            btnrow1,
            text="1",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_1_click,
        )
        btn1.pack(side=LEFT, expand=True, fill="both")

        btn2 = Button(
            btnrow1,
            text="2",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_2_click,
        )
        btn2.pack(side=LEFT, expand=True, fill="both")

        btn3 = Button(
            btnrow1,
            text="3",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_3_click,
        )
        btn3.pack(side=LEFT, expand=True, fill="both")

        btnplus = Button(
            btnrow1,
            text="+",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=add,
        )
        btnplus.pack(side=LEFT, expand=True, fill="both")
        # row 2 btn declaration
        btn4 = Button(
            btnrow2,
            text="4",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_4_click,
        )
        btn4.pack(side=LEFT, expand=True, fill="both")

        btn5 = Button(
            btnrow2,
            text="5",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_5_click,
        )
        btn5.pack(side=LEFT, expand=True, fill="both")

        btn6 = Button(
            btnrow2,
            text="6",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_6_click,
        )
        btn6.pack(side=LEFT, expand=True, fill="both")

        btnminus = Button(
            btnrow2,
            text="-",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=sub,
        )
        btnminus.pack(side=LEFT, expand=True, fill="both")
        # row 3 btn declaration
        btn7 = Button(
            btnrow3,
            text="7",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_7_click,
        )
        btn7.pack(side=LEFT, expand=True, fill="both")

        btn8 = Button(
            btnrow3,
            text="8",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_8_click,
        )
        btn8.pack(side=LEFT, expand=True, fill="both")

        btn9 = Button(
            btnrow3,
            text="9",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_9_click,
        )
        btn9.pack(side=LEFT, expand=True, fill="both")

        btnmul = Button(
            btnrow3,
            text="*",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=mul,
        )
        btnmul.pack(side=LEFT, expand=True, fill="both")
        # row 4 btn declaration
        btnC = Button(
            btnrow4,
            text="C",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_C_click,
        )
        btnC.pack(side=LEFT, expand=True, fill="both")

        btn0 = Button(
            btnrow4,
            text="0",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=btn_0_click,
        )
        btn0.pack(side=LEFT, expand=True, fill="both")

        btneq = Button(
            btnrow4,
            text="=",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=result,
        )
        btneq.pack(side=LEFT, expand=True, fill="both")

        btndiv = Button(
            btnrow4,
            text="/",
            font=btnfont,
            relief=GROOVE,
            border=0,
            activebackground="#FFF",
            command=div,
        )
        btndiv.pack(side=LEFT, expand=True, fill="both")
        root.mainloop()


Calculator()
