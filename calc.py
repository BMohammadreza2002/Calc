from tkinter import *
import tkinter.messagebox

# ============================================== settings =========================================
root = Tk()
root.title("Mohammadreza calculator")
root.geometry("300x350")
root.resizable(width=False, height=False)
color = "gray"
root.configure(bg=color)

# ============================================== variables =========================================
num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ============================================== frames =========================================
top_first = Frame(root, width=300, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=300, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=300, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=300, height=50, bg=color)
top_forth.pack(side=TOP)

top_fifth = Frame(root, width=300, height=50, bg=color)
top_fifth.pack(side=TOP)

top_sixth = Frame(root, width=300, height=50, bg=color)
top_sixth.pack(side=TOP)

top_seventh = Frame(root, width=300, height=50, bg=color)
top_seventh.pack(side=TOP)


# ============================================== Functions =========================================
def errorMsg(ms):
    if (ms == "error"):
        tkinter.messagebox.showerror("error", "something went wrong")
    elif ms == "division zero error":
        tkinter.messagebox.showerror("error", "can not devide by 0")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def div():
    if num2.get() == "0":
        errorMsg("division zero error")
    elif num2.get() != "0":
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg("error")


def one():
    label_first_num.set(1)


# ============================================== buttons =========================================
btn_seven = Button(top_forth, text="7", width=1, height=1, highlightbackground=color)
btn_seven.pack(side=LEFT, padx=10, pady=10)

btn_eight = Button(top_forth, text="8", width=1, height=1, highlightbackground=color)
btn_eight.pack(side=LEFT, padx=10, pady=10)

btn_nine = Button(top_forth, text="9", width=1, height=1, highlightbackground=color)
btn_nine.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_forth, text="/", width=1, height=1, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

btn_four = Button(top_fifth, text="4", width=1, height=1, highlightbackground=color)
btn_four.pack(side=LEFT, padx=10, pady=10)

btn_five = Button(top_fifth, text="5", width=1, height=1, highlightbackground=color)
btn_five.pack(side=LEFT, padx=10, pady=10)

btn_six = Button(top_fifth, text="6", width=1, height=1, highlightbackground=color)
btn_six.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_fifth, text="*", width=1, height=1, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_one = Button(top_sixth, text="1", width=1, height=1, highlightbackground=color, command=lambda: one())
btn_one.pack(side=LEFT, padx=10, pady=10)

btn_two = Button(top_sixth, text="2", width=1, height=1, highlightbackground=color)
btn_two.pack(side=LEFT, padx=10, pady=10)

btn_three = Button(top_sixth, text="3", width=1, height=1, highlightbackground=color)
btn_three.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_sixth, text="-", width=1, height=1, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_zero = Button(top_seventh, text="0", width=1, height=1, highlightbackground=color)
btn_zero.pack(side=LEFT, padx=48, pady=10)

btn_plus = Button(top_seventh, text="+", width=1, height=1, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

# ========================================= Entries and labels ===================================
label_first_num = Label(top_first, text="number 1:", bg=color)
label_first_num.pack(side=LEFT, padx=10, pady=10)

label_num = Entry(top_first, highlightbackground=color, textvariable=num1)
label_num.pack(side=LEFT)

label_second_num = Label(top_second, text="number 2:", bg=color)
label_second_num.pack(side=LEFT, padx=10, pady=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_third, text="result:", bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_third, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()
