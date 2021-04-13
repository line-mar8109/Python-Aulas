from tkinter import *

# eu não gostei, peguei no site -> https://copyassignment.com/simple-gui-calculator-using-tkinter-in-python/

root = Tk()
root.geometry("430x470")
expression = ""


def setexpression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)


def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except IndexError:
        value.set("ENTER CORRECT EXPRESSION")
        expression = ""


def clear():
    global expression
    expression = ""
    value.set(expression)


large_font = ('Verdana', 15)
small_font = ('Verdana', 10)

value = StringVar(value="ENTER EXPRESSION")
Entry(root, textvariable=value, font=large_font).grid(row=0,
                                                      column=0, columnspan=4, ipadx=70)

Button(root, text="+", fg="#212529", bg="#caffbf", command=lambda: setexpression("+"), height=4, width=4).grid(row=1,
                                                                                                               column=0,
                                                                                                               pady=10)
Button(root, text="-", fg="#212529", bg="#dee2ff", command=lambda: setexpression("-"), height=4, width=4).grid(row=2,
                                                                                                               column=0,
                                                                                                               pady=10)
Button(root, text="X", fg="#212529", bg="#ffd6a5", command=lambda: setexpression("*"), height=4, width=4).grid(row=3,
                                                                                                               column=0,
                                                                                                               pady=10)
Button(root, text="/", fg="#212529", bg="#a0c4ff", command=lambda: setexpression("/"), height=4, width=4).grid(row=4,
                                                                                                               column=0,
                                                                                                               pady=10)
Button(root, text="1", fg="#212529", bg="#ffadad", command=lambda: setexpression("1"), height=4, width=8).grid(row=1,
                                                                                                               column=1,
                                                                                                               pady=10)
Button(root, text="2", fg="#212529", bg="#ffadad", command=lambda: setexpression("2"), height=4, width=8).grid(row=1,
                                                                                                               column=2,
                                                                                                               pady=10)
Button(root, text="3", fg="#212529", bg="#ffadad", command=lambda: setexpression("3"), height=4, width=8).grid(row=1,
                                                                                                               column=3,
                                                                                                               pady=10)
Button(root, text="4", fg="#212529", bg="#ffadad", command=lambda: setexpression("4"), height=4, width=8).grid(row=2,
                                                                                                               column=1,
                                                                                                               pady=10)
Button(root, text="5", fg="#212529", bg="#ffadad", command=lambda: setexpression("5"), height=4, width=8).grid(row=2,
                                                                                                               column=2)
Button(root, text="6", fg="#212529", bg="#ffadad", command=lambda: setexpression("6"), height=4, width=8).grid(row=2,
                                                                                                               column=3,
                                                                                                               pady=10)
Button(root, text="7", fg="#212529", bg="#ffadad", command=lambda: setexpression("7"), height=4, width=8).grid(row=3,
                                                                                                               column=1,
                                                                                                               pady=10)
Button(root, text="8", fg="#212529", bg="#ffadad", command=lambda: setexpression("8"), height=4, width=8).grid(row=3,
                                                                                                               column=2,
                                                                                                               pady=10)
Button(root, text="9", fg="#212529", bg="#ffadad", command=lambda: setexpression("9"), height=4, width=8).grid(row=3,
                                                                                                               column=3,
                                                                                                               pady=10)
Button(root, text="0", fg="#212529", bg="#ffadad", command=lambda: setexpression("0"), height=4, width=8).grid(row=4,
                                                                                                               column=2,
                                                                                                               pady=10)
Button(root, text=".", fg="#212529", bg="#ffadad", command=lambda: setexpression("."), height=4, width=8).grid(row=4,
                                                                                                               column=1,
                                                                                                               pady=10)

Button(root, text="=", fg="#212529", bg="#fdffb6", command=calculator, height=4,
       width=8).grid(row=4, column=3, pady=10)

Button(root, text="Clear", fg="#212529", bg="#fdffb6", command=clear, height=3,
       width=8).grid(row=6, column=2, pady=10)

root.mainloop()
