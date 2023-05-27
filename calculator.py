#from tkinter import *
from customtkinter import *
root = CTk()
root.config(background= "#284F74")
root.geometry("345x470")
root.resizable(False,False)
root.title("Calculator by aviorian")

first_value = "0"
second_value = "0"
equal_amount = 0
first_value_operator = ""



def numerical_button(value:int):
    
    if len(entry_box.get()) !=0 or value !=0:
        entry_box.insert(END,str(value))
        

def clear():
    entry = entry_box.get()
    entry_1 = entry[0:-1]
    entry_box.delete(0,END)
    entry_box.insert(END,entry_1)


def clear_all():
    
    global first_value
    global second_value
    global equal_amount

    entry_box.delete(0,END)
    entry_box_secondary.delete(0,END)
    first_value = "0"
    second_value ="0"
    equal_amount=0


def operator(sign:str):

    global first_value
    global second_value
    
    if entry_box.get() != "":
        entry_box.insert(END,sign)
        
        if first_value == "0":
            first_value = entry_box.get()
            entry_box_secondary.insert(END,first_value)
        else :
            first_value_without_operator = (first_value[0:-1])
            second_value = entry_box.get()
            second_value_without_operator =(second_value[0:-1])

            if first_value[-1]=="+":
                first_value = float(first_value_without_operator) + float(second_value_without_operator)
            elif first_value[-1] == "-":
                first_value = float(first_value_without_operator) - float(second_value_without_operator)
            elif first_value[-1] == "*":
                first_value = float(first_value_without_operator) * float(second_value_without_operator)
            elif first_value[-1] == "/":
                first_value = float(first_value_without_operator) / float(second_value_without_operator)

            first_value = str(first_value) + second_value[-1]
            entry_box_secondary.insert(END,second_value)

            

    entry_box.delete(0,END)
    


def equal():

    global first_value
    global second_value
    global equal_amount
    global first_value_operator


    if entry_box.get() != "":
        
        if equal_amount<1:
        
            first_value_without_operator = (first_value[0:-1])
            first_value_operator = first_value[-1]
            second_value = entry_box.get()
            

            if first_value[-1]=="+":
                first_value = float(first_value_without_operator) + float(second_value)
            elif first_value[-1] == "-":
                first_value = float(first_value_without_operator) - float(second_value)
            elif first_value[-1] == "*":
                first_value = float(first_value_without_operator) * float(second_value)
            elif first_value[-1] == "/":
                first_value = float(first_value_without_operator) / float(second_value)

            entry_box.delete(0,END)
            entry_box_secondary.insert(END,second_value+"=")
            entry_box.insert(0,str(first_value))
            
        if equal_amount>=1:
            if first_value_operator=="+":
                first_value =float(first_value)+float(second_value)
            elif first_value_operator=="-":
                first_value =float(first_value)-float(second_value)
            elif first_value_operator=="*":
                first_value =float(first_value)*float(second_value)
            elif first_value_operator=="/":
                first_value =float(first_value)/float(second_value)
                
            entry_box.delete(0,END)
            entry_box.insert(END,first_value)
    
    equal_amount+=1

def ignore_keyboard_input(event):
    return "break"


        

entry_box_secondary = CTkEntry(root,width=255,height=15,font=(None,15), corner_radius=5,text_color="white")
entry_box = CTkEntry(root,width=255,height=50,font=(None,27), corner_radius=5,text_color="orange")
entry_box.bind("<Key>",ignore_keyboard_input)
entry_box_secondary.bind("<Key>",ignore_keyboard_input)

button_1 = CTkButton(root,text="1",fg_color="#081717",hover_color="#202e2e" ,text_color="orange", width=80,height=70,command=lambda: numerical_button(1))
button_2 = CTkButton(root,text="2",fg_color="#081717",hover_color="#202e2e" ,text_color="orange" ,width=80,height=70,command=lambda: numerical_button(2))
button_3 = CTkButton(root,text="3",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(3))
button_4 = CTkButton(root,text="4",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(4))
button_5 = CTkButton(root,text="5",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(5))
button_6 = CTkButton(root,text="6",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(6))
button_7 = CTkButton(root,text="7",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(7))
button_8 = CTkButton(root,text="8",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(8))
button_9 = CTkButton(root,text="9",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=80,height=70,command=lambda: numerical_button(9))
button_0 = CTkButton(root,text="0",fg_color="#081717",hover_color="#202e2e" ,text_color="orange",width=165,height=70,command=lambda: numerical_button(0))

button_plus=CTkButton(root,text="+",fg_color="#394545",text_color="yellow",hover_color="#635C6C", width=80,height=70,command=lambda: operator("+"))
button_division=CTkButton(root,text="/",fg_color="#394545",text_color="yellow",hover_color="#635C6C",width=80,height=70,command=lambda: operator("/"))
button_minus=CTkButton(root,text="-",fg_color="#394545",text_color="yellow",hover_color="#635C6C",width=80,height=70,command=lambda: operator("-"))
button_multiple=CTkButton(root,text="x",fg_color="#394545",text_color="yellow",hover_color="#635C6C",width=80,height=70,command=lambda: operator("*"))
button_equal=CTkButton(root,text="=",fg_color="#635C6C",text_color="yellow",hover_color="#394545",width=80,height=70,command=equal)
button_clear=CTkButton(root,text="⌫",fg_color="#394545",text_color="yellow",hover_color="#635C6C",width=80,height=70,command=clear)
button_clear_all=CTkButton(root,text="C",fg_color="#394545",text_color="yellow",hover_color="#635C6C",width=165,height=70,command=clear_all)

label = CTkLabel(root,text="Don't forget press 'C'" + "\n" + " after using '='.",text_color="orange",bg_color="#284F74")

entry_box_secondary.place(x=0,y=0)
entry_box.place(x=0,y=25)

button_7.place(x=5,y=80)
button_4.place(x=5,y=155)
button_1.place(x=5,y=230)

button_8.place(x=90,y=80)
button_5.place(x=90,y=155)
button_2.place(x=90,y=230)

button_9.place(x=175,y=80)
button_6.place(x=175,y=155)
button_3.place(x=175,y=230)

button_0.place(x=5,y=305)

button_division.place(x=260,y=80)
button_multiple.place(x=260,y=155)
button_minus.place(x=260,y=230)
button_plus.place(x=260,y=305)
button_equal.place(x=175,y=305)
button_clear.place(x=260,y=5)
button_clear_all.place(x=5,y=380)
label.place(x=220,y=430)

root.mainloop()

