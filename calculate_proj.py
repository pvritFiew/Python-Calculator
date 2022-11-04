
from tkinter import *
import math

display = Tk()
display.title("Naa_Fiew Calculator")

content = ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calc = float(eval(content))
    after_r = txt_input.get()
    txt_input.set(calc)
    content= str(calc)
    hist_txt = after_r + " = " + str(content) + "\n"
    history.insert(END, hist_txt)
    with open ("history.txt",'a') as file:
        file.write(hist_txt)
    file.close()
    
def allclear():#delete all content
    global content
    content = ""
    txt_input.set("")
    num_dis.insert(0,"0")

def delete():#delete last one
    global content
    content = content[:-1]
    txt_input.set(content)

def pownum():
    global content
    pow_value = math.pow(float(eval(content)),2)
    his_txt = str(content)+"\u00b2 = "+str(pow_value)+'\n'
    txt_input.set(pow_value)
    content = str(pow_value)
    history.insert(END,his_txt)
    

def sqrtnum():
    global content
    sqrt_value = math.sqrt(float(eval(content)))
    his_txt = "\u221a"+str(content)+" = "+str(sqrt_value)+'\n'
    txt_input.set(sqrt_value)
    content = str(sqrt_value)
    history.insert(END,his_txt)

def trigo(func):
    global content
    value = 0
    his_txt = ''
    if func == 'sin':
        value = math.sin(float(eval(content)))
        his_txt = "sin("+str(content)+") = "+str(value)+'\n'
    elif func == 'cos':
        value = math.cos(float(eval(content)))
        his_txt = "cos("+str(content)+") = "+str(value)+'\n'
    elif func == 'tan':
        value = math.tan(float(eval(content)))
        his_txt = "tan("+str(content)+") = "+str(value)+'\n'
    txt_input.set(value)
    content = str(value)
    history.insert(END,his_txt)

def all_h():
    history.delete("1.0", "end")
    with open ("history.txt",'r') as file:
        history_cal = file.read()
        history.insert(END,history_cal)
    file.close()

def delete_h():
    with open ("history.txt",'w') as file:
        file.write("")
    file.close()
    history.delete("1.0", "end")

win = Frame(display,width=450,height=450,bg="#15202b").place(x=0,y=0)
num_dis = Entry(font=('arial',24),bg="#AAB8C2",fg="black",textvariable=txt_input,justify="right")
num_dis.grid(columnspan=5)

btn_sin = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="sin",width=5,height=1,command=lambda:trigo('sin')).grid(row=1,column=0)
btn_l = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="(",width=5,height=1,command=lambda:btn("(")).grid(row=1,column=1)
btn_r = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text=")",width=5,height=1,command=lambda:btn(")")).grid(row=1,column=2)
btn_del = Button(master=win,fg='white',bg='#657786',bd=0,font=('arial',20),text="Del",width=5,height=1,command=delete).grid(row=1,column=3)
btn_c = Button(master=win,fg='white',bg='orange',bd=0,font=('arial',20),text="C",width=5,height=1,command=allclear).grid(row=1,column=4)

btn_cos = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="cos",width=5,height=1,command=lambda:trigo('cos')).grid(row=2,column=0)
btn1 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="1",width=5,height=1,command=lambda:btn(1)).grid(row=2,column=1)
btn2 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="2",width=5,height=1,command=lambda:btn(2)).grid(row=2,column=2)
btn3 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="3",width=5,height=1,command=lambda:btn(3)).grid(row=2,column=3)
btn_plus = Button(master=win,fg='white',bg='#AAB8C2',bd=0,font=('arial',20),text="+",width=5,height=1,command=lambda:btn("+")).grid(row=2,column=4)

btn_tan = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="tan",width=5,height=1,command=lambda:trigo('tan')).grid(row=3,column=0)
btn4 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="4",width=5,height=1,command=lambda:btn(4)).grid(row=3,column=1)
btn5 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="5",width=5,height=1,command=lambda:btn(5)).grid(row=3,column=2)
btn6 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="6",width=5,height=1,command=lambda:btn(6)).grid(row=3,column=3)
btn_minus = Button(master=win,fg='white',bg='#AAB8C2',bd=0,font=('arial',20),text="-",width=5,height=1,command=lambda:btn("-")).grid(row=3,column=4)

btn_pow = Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="x\u00b2",width=5,height=1,command=pownum).grid(row=4,column=0)
btn7 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="7",width=5,height=1,command=lambda:btn(7)).grid(row=4,column=1)
btn8 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="8",width=5,height=1,command=lambda:btn(8)).grid(row=4,column=2)
btn9 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="9",width=5,height=1,command=lambda:btn(9)).grid(row=4,column=3)
btn_multiply = Button(master=win,fg='white',bg='#AAB8C2',bd=0,font=('arial',20),text="x",width=5,height=1,command=lambda:btn("*")).grid(row=4,column=4)

btn_sqr= Button(master=win,fg='white',bg='#314356',bd=0,font=('arial',20),text="\u221ax",width=5,height=1,command=sqrtnum).grid(row=5,column=0)
btn_dot = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text=".",width=5,height=1,command=lambda:btn(".")).grid(row=5,column=1)
btn0 = Button(master=win,fg='white',bg='#15202b',bd=0,font=('arial',20),text="0",width=5,height=1,command=lambda:btn("0")).grid(row=5,column=2)
btn_Enter = Button(master=win,fg='white',bg='#32E851',bd=0,font=('arial',20),text="enter",command=equal,width=5,height=1).grid(row=5,column=3)
btn_division = Button(master=win,fg='white',bg='#AAB8C2',bd=0,font=('arial',20),text="÷",width=5,height=1,command=lambda:btn("/")).grid(row=5,column=4)

label_his = Label(display,text="History", font=20,width=40,fg='white',bg='#4275A8').place(x=0,y=300)
history = Text(display,wrap=None,width=45,height=6,bg='#E0EFF9',font=12)
history.place(x=0,y=325)

btn_rh = Button(master=win,fg='black',bg='#AAB8C2',bd=0,font=('arial',8),text="All History >>",width=15,command=all_h).place(x=340,y=430)
btn_ch = Button(master=win,fg='black',bg='#AAB8C2',bd=0,font=('arial',8),text="<< clear History",width=15,command=delete_h).place(x=0,y=430)
display.geometry("430x450")
display.minsize(430,450)
display.maxsize(430,450)
display.mainloop()
