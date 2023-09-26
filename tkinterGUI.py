from tkinter import *
def buttonClick(self):
    print("you have click me")

root=Tk()
f= Frame(root,height=200,width=300)
f.propagate(0)
f.pack()
b=Button(f, text="my button",width=15,height=2,bg="blue",fg="gold",activebackground="gray",activeforeground="green")
l=Label(f, text="Name",width=15,height=2,fg="white",bg="black") 
b.pack()
b.bind("<Button-1>",buttonClick)


root.title("Calculator")

#root.wm_iconbitmap('calculator.jpg')
#c=canvas(root, bg="blue",height=500,width=600,cursor='pencil')
mainloop()
