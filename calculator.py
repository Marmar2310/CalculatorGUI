from tkinter import *

expression = ""

def button_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal_button():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = str(total)

def clear_button():
    global expression
    expression = ""
    equation.set("")

if __name__ == '__main__':
    window = Tk()
    window.title("Calculator")
    window.geometry('350x200')

    equation = StringVar()
    expression_field = Entry(window, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(window, text=' 1 ', fg='black', bg='orange',
                     command=lambda: button_press(1), height=1, width=7)
    button1.grid(row=4, column=0)

    button2 = Button(window, text=' 2 ', fg='black', bg='orange',
                     command=lambda: button_press(2), height=1, width=7)
    button2.grid(row=4, column=1)

    button3 = Button(window, text=' 3 ', fg='black', bg='orange',
                     command=lambda: button_press(3), height=1, width=7)
    button3.grid(row=4, column=2)

    button4 = Button(window, text=' 4 ', fg='black', bg='orange',
                     command=lambda: button_press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(window, text=' 5 ', fg='black', bg='orange',
                     command=lambda: button_press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(window, text=' 6 ', fg='black', bg='orange',
                     command=lambda: button_press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(window, text=' 7 ', fg='black', bg='orange',
                     command=lambda: button_press(7), height=1, width=7)
    button7.grid(row=2, column=0)

    button8 = Button(window, text=' 8 ', fg='black', bg='orange',
                     command=lambda: button_press(8), height=1, width=7)
    button8.grid(row=2, column=1)

    button9 = Button(window, text=' 9 ', fg='black', bg='orange',
                     command=lambda: button_press(9), height=1, width=7)
    button9.grid(row=2, column=2)

    button0 = Button(window, text=' 0 ', fg='black', bg='orange',
                     command=lambda: button_press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    plus = Button(window, text=' + ', fg='white', bg='grey',
                  command=lambda: button_press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(window, text=' - ', fg='white', bg='grey',
                   command=lambda: button_press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(window, text=' * ', fg='white', bg='grey',
                      command=lambda: button_press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(window, text=' / ', fg='white', bg='grey',
                    command=lambda: button_press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(window, text=' = ', fg='white', bg='grey',
                   command=equal_button, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(window, text='Clear', fg='white', bg='grey',
                   command=clear_button, height=1, width=7)
    clear.grid(row=6, column=0)

    decimal = Button(window, text='.', fg='white', bg='orange',
                     command=lambda: button_press('.'), height=1, width=7)
    decimal.grid(row=5, column=0)

    window.mainloop()
