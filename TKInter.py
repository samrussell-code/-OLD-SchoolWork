from tkinter import *;import os
### Python Documentation Example ###
class HelloWorld(Frame):
    def __init__(self, mainWidget=None):
        super().__init__(mainWidget) #constructs the frame widget
        self.mainWidget = mainWidget
        mainWidget.title("Window Title Text");mainWidget.configure(bg="aqua")
        self.pack(fill=BOTH,expand=True) #adds the widget
        self.CreateContent()
    
    def CreateContent(self):
        ### All the stuff inside the widget
        self.SayHi = Button(self, text="Hello World", fg="white",bg="blue",width=75,height=10,command=self.sayHi) #creates a type of Button called buttonName, to be included in the widget (self)
        self.SayHi.pack(side="top",fill=BOTH,expand=True) #adds the button into the widget at the top, filling the space

        self.CloseWidget = Button(self, text="CLOSE WIDGET", fg="white",bg="green",width=75,height=10,cursor="target",command=self.mainWidget.destroy)#creates a type of Button called quit, to be included in the widget (self), have text called quit, have colour of red, and the built in destroy command
        self.CloseWidget.pack(side="top",fill=BOTH,expand=True) #adds the button into the widget at the bottom, filling the space

        self.CloseProgram = Button(self, text="CLOSE PROGRAM", fg="white",bg="dark green",width=75,height=10,cursor="pirate",command=self.closeProgram)
        self.CloseProgram.place(bordermode=OUTSIDE,relx=0.0,rely=0.0,relheight=1.0,relwidth=0.25) #adds the button into the widget at the bottom, filling the space

    def sayHi(widgetName):
        print("hi there, everyone!")

    def closeProgram(widgetName):
         os._exit(0)


userInput=""
HelloWorld(mainWidget=Tk()).mainloop(); #instantiates a widget defined earlier
while userInput!="1":
    userInput=input("Enter 0 For Widget\nEnter 1 For Exit\n")
    if userInput=="0":
        HelloWorld(mainWidget=Tk()).mainloop(); #instantiates a widget defined earlier
    elif userInput=="1":
        os._exit(1)