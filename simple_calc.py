from tkinter import *
frame = Tk()
frame.title("Simple Calculator")
frame.geometry("450x750")

entry = Entry(frame, width=30,font=('Times New Roman', 20), borderwidth=8, relief = RIDGE, justify = 'right')
entry.grid(row = 0, column=0, columnspan=5, pady=12)


def enter(button_press):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(END, current + button_press)


def clear():
    entry.delete(0,END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,str(result))
        
    except:
        entry.delete(0,END)
        entry.insert(END,'Error')


buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)

]            

for (text,row,col) in buttons:
    if text == '=':
        Button(frame, text=text, width=6, height=3, font=('Times New Roman',20), command=calculate).grid(row=row, column=col, padx=6,pady=6)
    else:
        Button(frame, text=text, width=6, height=3, font=('Times New Roman',20), command=lambda t=text: enter(t)).grid(row=row, column=col, padx=6, pady=6)

Button(frame, text='C', width=6, height=3, font=('Times New Roman',20), command=clear).grid(row=5, column=0, columnspan=4, padx=6, pady=6) 

frame.mainloop()

