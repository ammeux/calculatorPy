from tkinter import *
from functools import partial
import math


class Calculator:
    def __init__(self):
        self.operation = "+"
        self.last_result = 0
        self.new_num = 0
        self.operator = ""
        self.currentSign = "+"
        self.op_history = ""
        self.label_result = Label(root)
        self.label_result.grid(row=0, column=0)
        self.count_op = int(0)
        self.erase = False

# methods used to display operations history and screen
    def display_history(self):
        self.label_result.config(text=self.op_history)

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

# methods performing calculations according to last operator
    def operations(self):
        if self.operator == "+":
            self.last_result = float(self.last_result) + float(self.new_num)
        elif self.operator == "-":
            self.last_result = float(self.last_result) - float(self.new_num)
        elif self.operator == "x":
            self.last_result = float(self.last_result) * float(self.new_num)
        elif self.operator == "/":
            self.last_result = float(self.last_result) / float(self.new_num)
        elif self.operator == "mod":
            self.last_result = float(self.last_result) % float(self.new_num)
        elif self.operator == "power":
            self.last_result = float(self.last_result) ** float(self.new_num)


# methods called according to buttons typed
    def typed_figures(self, figure):
        if self.erase:
            self.display("")
            self.erase = False
        temp = text_box.get()
        temp2 = str(figure)
        self.display(temp + temp2)

    def typed_operators(self, operator):
        self.op_history = self.op_history + " " + text_box.get() + " " + operator
        self.new_num = float(text_box.get())
        self.operations()
        self.display(self.last_result)
        self.operator = operator
        if operator == "=":
            self.op_history = ""
            self.last_result = 0
            self.operator = "+"
        self.display_history()
        self.erase = True

    def typed_functions(self, function):
        temp = text_box.get()
        if function == "factorial":
            temp = self.factorial(int(temp))
        if function == "square":
            temp = float(temp) * float(temp)
        if function == "sine":
            temp = round(math.sin(math.radians(int(temp))), 2)
        if function == "cosine":
            temp = round(math.cos(math.radians(int(temp))), 2)
        if function == "tangent":
            temp = round(math.tan(math.radians(int(temp))), 2)
        if function == "square_root":
            temp = round(math.sqrt(int(temp)), 2)
        if function == "ten_power":
            temp = self.ten_power(int(temp))
        if function == "log":
            temp = round(math.log(int(temp), 10), 2)
        if function == "exp":
            temp = round(math.exp(int(temp)), 2)
        self.display(temp)

# Clearing screen/history methods
    def clear(self):
        self.display("")

    def clearAll(self):
        self.last_result = 0
        self.operator = "+"
        self.display("")
        self.op_history = ""
        self.display_history()

# ChangeSign button
    def changeSign(self):
        temp = text_box.get()
        if self.currentSign == "+":
            self.display("-" + temp)
            self.currentSign = "-"
        else:
            self.display(temp[1:])
            self.currentSign = "+"

# Functions developed in recursive way
    def factorial(self, number):
        if number >= 1:
            return number*self.factorial(number - 1)
        else:
            return 1

    def ten_power(self, number):
        if number >= 1:
            return self.ten_power(number - 1) * 10
        else:
            return 1

root = Tk()
root.title('My Calculator')

calculator = Calculator()
calc = Frame(root)
calc.grid()


# Top buttons front
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=5, pady=5)

square = Button(calc, text="x²", bg="orange")
square["command"] = partial(calculator.typed_functions, "square")
square.grid(row=1, column=0, pady=5)

power = Button(calc, text="x"+u"\u207F", bg="orange")
power["command"] = partial(calculator.typed_operators, "power")
power.grid(row=1, column=1, pady=5)

sine = Button(calc, text="sin", bg="orange")
sine["command"] = partial(calculator.typed_functions, "sine")
sine.grid(row=1, column=2, pady=5)

cosine = Button(calc, text="cos", bg="orange")
cosine["command"] = partial(calculator.typed_functions, "cosine")
cosine.grid(row=1, column=3, pady=5)

tangent = Button(calc, text="tan", bg="orange")
tangent["command"] = partial(calculator.typed_functions, "tangent")
tangent.grid(row=1, column=4, pady=5)

square_root = Button(calc, text="√", bg="orange")
square_root["command"] = partial(calculator.typed_functions, "square_root")
square_root.grid(row=2, column=0, pady=5)

ten_power = Button(calc, text="10"+u"\u207F", bg="orange")
ten_power["command"] = partial(calculator.typed_functions, "ten_power")
ten_power.grid(row=2, column=1, pady=5)

log = Button(calc, text="log", bg="orange")
log["command"] = partial(calculator.typed_functions, "log")
log.grid(row=2, column=2, pady=5)

exp = Button(calc, text="exp", bg="orange")
exp["command"] = partial(calculator.typed_functions, "exp")
exp.grid(row=2, column=3, pady=5)

mod = Button(calc, text="mod", bg="orange")
mod["command"] = partial(calculator.typed_operators, "mod")
mod.grid(row=2, column=4, pady=5)

# Numeric pad
numbers = "789456123"
i = 0
bttn = []
for j in range(3, 6):
    for k in range(3):
        bttn.append(Button(calc, text=numbers[i]))
        bttn[i].grid(row=j, column=k, pady=5)
        bttn[i]["command"] = partial(calculator.typed_figures, numbers[i])
        i += 1

# Operations buttons
add = Button(calc, text="+", bg="steel blue")
add["command"] = partial(calculator.typed_operators, "+")
add.grid(row=3, column=3, pady=5)

minus = Button(calc, text=" -", bg="steel blue")
minus["command"] = partial(calculator.typed_operators, "-")
minus.grid(row=4, column=3, pady=5)

multiply = Button(calc, text="x", bg="steel blue")
multiply["command"] = partial(calculator.typed_operators, "x")
multiply.grid(row=5, column=3, pady=5)

divide = Button(calc, text="/", bg="steel blue")
divide["command"] = partial(calculator.typed_operators, "/")
divide.grid(row=6, column=3, pady=5)

equals = Button(calc, text="=", bg="steel blue")
equals["command"] = partial(calculator.typed_operators, "=")
equals.grid(row=6, column=2, pady=5)

button_0 = Button(calc, text="0")
button_0["command"] = partial(calculator.typed_figures, "0")
button_0.grid(row=6, column=1, pady=5)

sign = Button(calc, text="+/-", bg="steel blue")
sign["command"] = partial(calculator.changeSign)
sign.grid(row=6, column=0, pady=5)

clear = Button(calc, text="C", bg="green")
clear["command"] = partial(calculator.clear)
clear.grid(row=3, column=4, pady=5)

clearAll = Button(calc, text="AC", bg="green")
clearAll["command"] = partial(calculator.clearAll)
clearAll.grid(row=4, column=4, pady=5)

pi = Button(calc, text=u"\u03C0", bg="steel blue")
pi["command"] = partial(calculator.display, round(math.pi, 3))
pi.grid(row=5, column=4, pady=5)

factorial = Button(calc, text="!n", bg="steel blue")
factorial["command"] = partial(calculator.typed_functions, "factorial")
factorial.grid(row=6, column=4, pady=5)

root.mainloop()