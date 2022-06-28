from tkinter import *
import random
root=Tk()
root.title("Strong passcodes")
root.geometry("500x500")
label1=Label(root)
label1.place(relx=0.5,rely=0.2,anchor=CENTER)
input1=Entry(root)
input1.place(relx=0.5,rely=0.4,anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)

array_3d=[[[1,2,3,4,5,6,7],["dfjvlk","uakojaswibv","lollmaooiiy"],["A","B","C","O","E","F","G"],["!","@","&","$","#","*"]]]
def generatepassword():
    passcode=input1.get()
    label2["text"]="old password: "+passcode
    random_number1=random.randint(0,6)
    random_number2=random.randint(0,2)
    random_number3=random.randint(0,6)
    random_number4=random.randint(0,5)
    letter1=str(array_3d[0][0][random_number1])
    letter2=array_3d[0][1][random_number2]
    letter3=array_3d[0][2][random_number3]
    letter4=array_3d[0][3][random_number4]
    label1["text"]=letter1+letter2+letter3+letter4



    
    
    
button1=Button(root,bg="royalblue",text="Generate password",command=generatepassword)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

