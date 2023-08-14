#calculator:

'''print("\nwelcome to the python calculator:\n\n"
    "\t1.addition\n"
    "\t2.subtraction\n"
    "\t3.multiplication\n"
    "\t4.division\n"
)
n=int(input("choose any one --1,2,3 or 4--:"))
a=int(input("Enter the First Value:"))
b=int(input("Enter the Second Value:"))

if n == 1:
    c=a+b
    print("\n\tAddition answer is:",c)

elif n == 2:
    c=a-b
    print("\n\tSubtraction answer is:",c)

elif n == 3:
    c=a*b
    print("\n\tMultiplication answer is:",c)
elif n == 4:
    c=a/b
    print("\n\tDivision answer is:",c)

else:
    print("invalid value")'''





import tkinter as tk

calculation= ""
root = tk.Tk()

root.resizable(False,False)
root.configure(bg="#17161b")

input = tk.Text(root,height=2,width=18,font=('Arial',24),bg="black",fg="white")
input.grid(columnspan=5)

def add(num):
    global calculation
    calculation += str(num)
    input.delete(1.0,"end")
    input.insert(1.0,calculation)


def equal():
    global calculation
    try:
        calculation = str(eval(calculation))
        input.delete(1.0,"end")
        input.insert(1.0,calculation)
    except:
        clear()
        input.insert(1.0,"error")


def clear():
    global calculation
    calculation=""
    input.delete(1.0,"end")








button_1 = tk.Button(root, text="1", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(1))
button_2 = tk.Button(root, text="2", width=10, height=2,bg='#2a2d36',fg='white', command=lambda:add(2))
button_3 = tk.Button(root, text="3", width=10,height=2,bg='#2a2d36',fg='white',  command=lambda:add(3))
button_4 = tk.Button(root, text="4", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(4))
button_5 = tk.Button(root, text="5", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(5))
button_6 = tk.Button(root, text="6", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(6))
button_7 = tk.Button(root, text="7", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(7))
button_8 = tk.Button(root, text="8", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(8))
button_9 = tk.Button(root, text="9", width=10,height=2,bg='#2a2d36',fg='white',  command=lambda:add(9))
button_0 = tk.Button(root, text="0", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(0))

button_open= tk.Button(root, text="(", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add("("))
button_close= tk.Button(root, text=")", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add(")"))
button_percentage= tk.Button(root, text="%", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add("%"))
button_dot= tk.Button(root, text=".", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add("."))
button_add = tk.Button(root, text="+", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add("+"))
button_sub = tk.Button(root, text="-", width=10,height=2, bg='#2a2d36',fg='white', command=lambda:add("-"))
button_multi = tk.Button(root, text="x", width=10,height=2,bg='#2a2d36',fg='white', command=lambda:add("*"))
button_div = tk.Button(root, text="/", width=10, height=2,bg='#2a2d36',fg='white', command=lambda:add("/"))
button_clear = tk.Button(root, text="AC",width=10,height=2, bg='#3697f5',fg='white', command=clear)
button_equal = tk.Button(root, text="=", width=10,height=2, bg='#fe9037',fg='white', command=equal)



button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=5,column=3)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_multi.grid(row=4, column=3)
button_div.grid(row=4, column=2)

button_clear.grid(row=1,column=3)
button_open.grid(row=5,column=0)
button_close.grid(row=5,column=1)
button_percentage.grid(row=5,column=2)

root.mainloop()

