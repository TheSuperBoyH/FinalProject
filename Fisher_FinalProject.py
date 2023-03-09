from tkinter import *
import math

notesOpen = False #global variable to keep user from opening multiple note windows
  
# creates a new window for user to take notes in
def NoteBox2():

    # create a notes window
    notes = Tk()

    global notesOpen #reference global variable
    #declare textboxes for notes
    noteA = "" 
    noteB = ""
    noteC = ""
    noteX = ""
    noteY = ""
    noteZ = ""
    
    # closes the note window if the user clicks exit on the menu
    def notes_end():
        global notesOpen #reference global variable
        notesOpen = False
        notes.destroy()

    # closes the note window if the user clicks exit button 
    def disable_event():
        global notesOpen #reference global variable
        notesOpen = False
        notes.destroy()

    #clears the all the text boxes in the note window
    def notesclear():
        note_boxA.delete(0, END)
        note_boxB.delete(0, END)
        note_boxC.delete(0, END)
        note_boxX.delete(0, END)
        note_boxY.delete(0, END)
        note_boxZ.delete(0, END)

    # set the background colour of notes window
    notes.configure(background="blue")
 
    # set the title of notes window
    notes.title("Note Box")
 
    # set the configuration of notes window
    notes.geometry("270x175")
    notes.resizable(width=False, height=False)
 
    # we need this to change the behavior of the exit button in the note window
    notes.protocol("WM_DELETE_WINDOW", disable_event)
 
    # create the text box for for note A
    labelNoteA = Label(notes, text = "A",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteA.grid(row=1, column=0)
    note_boxA = Entry(notes, textvariable=noteA, font=('Arial',14,'bold'))
    note_boxA.grid(row=1, column=2, columnspan=4, ipadx=70)
    
    # create the text box for for note B
    labelNoteB = Label(notes, text = "B",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteB.grid(row=2, column=0)    
    note_boxB = Entry(notes, textvariable=noteB, font=('Arial',14,'bold'))
    note_boxB.grid(row=2, column=2, columnspan=4, ipadx=70)

    # create the text box for for note C
    labelNoteC = Label(notes, text = "C",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteC.grid(row=3, column=0)    
    note_boxC = Entry(notes, textvariable=noteC, font=('Arial',14,'bold'))
    note_boxC.grid(row=3, column=2, columnspan=4, ipadx=70)

    # create the text box for for note X
    labelNoteX = Label(notes, text = "X",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteX.grid(row=4, column=0)    
    note_boxX = Entry(notes, textvariable=noteX, font=('Arial',14,'bold'))
    note_boxX.grid(row=4, column=2, columnspan=4, ipadx=70)

    # create the text box for for note Y
    labelNoteY = Label(notes, text = "Y",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteY.grid(row=5, column=0)    
    note_boxY = Entry(notes, textvariable=noteY, font=('Arial',14,'bold'))
    note_boxY.grid(row=5, column=2, columnspan=4, ipadx=70)

    # create the text box for for note Z
    labelNoteZ = Label(notes, text = "Z",font=('Arial',14,'bold'),fg='black',justify=CENTER)
    labelNoteZ.grid(row=6, column=0)    
    note_boxZ = Entry(notes, textvariable=noteZ, font=('Arial',14,'bold'))
    note_boxZ.grid(row=6, column=2, columnspan=4, ipadx=70)

    # create a menu for notes windows with clear and exit commands
    notemenubar = Menu(notes)
    notemenubar.add_command(label = "Clear", command = notesclear)
    notemenubar.add_command(label = "Exit", command = notes_end)
    notes.config(menu=notemenubar)
     

#This function checks to see if a note window is open before creating one
def NoteBox():
    global notesOpen #reference global variable
    if (notesOpen == False):
        notesOpen = True
        NoteBox2()
    else:
        return

#this code creates the main calculator window. 
root = Tk()
root.title("Walter's Pyhton Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568")
calc = Frame(root)
calc.grid()
 
#This function performs the main calculations for the program
class Calculator():
    def __init__(self):
        self.total=0 #stores the first value in the equation.
        self.currentValue=''#holds the value that currently in the textbox 
        self.inputValue=True  #lets program know whether to append current value or start a new one
        self.checkValue=False  #lets the program know whether and operation button has been pressed or not
        self.operator='' #lets the program know what type of equation it is.
        self.result=False #lets program know operation is completed
 
    #handles user input and stores digits into one value  
    def User_Input(self, num):
        self.result=False #user is just typing in next digit don't anything yet
        firstValue=outputBox.get() #old string of digits
        secondValue=str(num) #new digits
        if self.inputValue:  #user is typing in a value
            self.currentValue = secondValue
            self.inputValue=False #let user keep typing until operator or equal button is pressed
        else:
            if secondValue == '.':  #handle the user typing in a decimal
                if secondValue in firstValue:
                    return
            self.currentValue = firstValue+secondValue #add old and new string
        self.display(self.currentValue)
 
    def solve_expression(self):
        self.result=True  #perform operation
        self.currentValue=float(self.currentValue) #change to floating number
        if self.checkValue==True: #Don't do anything if an operator has not been pressed, however
            self.simple_math()
        else:
            self.total=float(outputBox.get()) #change the value of total so the user can add to last equation
 
    #sets the display to one value instead of a string of digits
    def display(self, value):
        outputBox.delete(0, END)
        outputBox.insert(0, value)
 
    #decides what type of calcuation to perform depending which button was press.
    def simple_math(self):
        if self.operator == "add":
            self.total += self.currentValue
        if self.operator == "sub":
            self.total -= self.currentValue
        if self.operator == "multi":
            self.total *= self.currentValue
        if self.operator == "divide":
            self.total /= self.currentValue
        self.inputValue=True #let user type in new value instead of pending the current one
        self.checkValue=False  #lets the program know the operation has been performed and remove the operator.
        self.display(self.total)
 
    #handles logic if user presses an operation key
    def operation(self, operator):
        self.currentValue = float(self.currentValue) #change string into float
        if self.checkValue:  #Don't do anything if an operator has not been pressed
            self.simple_math()
        elif not self.result:  #if no operation has perform store the current value 
            self.total=self.currentValue
            self.inputValue=True #let user type in new value instead of pending the current one
        self.checkValue=True  #let the program know an operator has been pressed
        self.operator=operator  #self the value of the operator
        self.result=False  #lets the program know the operation has not been performed
 
    #set the number in the display box to 0
    def Clear_User_Input(self):
        self.result = False  #clears any current operation
        self.currentValue = "0"
        self.display(0)
        self.inputValue=True
 
    #set any number in memory and and display to 0
    def Clear_All_User_Input(self):
        self.Clear_User_Input()
        self.total=0
 
    #uses bult in math function to display pi
    def pi(self):
        self.result =  False #we want the user be able to form another operation so saying its not done.
        self.currentValue = math.pi
        self.display(self.currentValue)

    #changes the sign of the current value
    def mathPM(self):
        self.result = False
        self.currentValue = -(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the square root of the current value
    def square_root(self):
        self.result = False
        self.currentValue = math.sqrt(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the cosine of the current value
    def cos(self):
        self.result = False
        self.currentValue = math.cos(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the hyperbolic cosine of the current value
    def cosh(self):
        self.result = False
        self.currentValue = math.cosh(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the tangent of the current value
    def tan(self):
        self.result = False
        self.currentValue = math.tan(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the hyperbolic tangent of the current value
    def tanh(self):
        self.result = False
        self.currentValue = math.tanh(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the sine of the current value
    def sin(self):
        self.result = False
        self.currentValue = math.sin(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the hyperbolic sine of the current value
    def sinh(self):
        self.result = False
        self.currentValue = math.sinh(math.radians(float(outputBox.get())))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the logarithmic value of the current value
    def log(self):
        self.result = False
        self.currentValue = math.log(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the exponential value of the current value
    def exp(self):
        self.result = False
        self.currentValue = math.exp(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the inverse hyperbolic cosine of the current value
    def acosh(self):
        self.result = False
        self.currentValue = math.acosh(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the inverse hyperbolic sine of the current value
    def asinh(self):
        self.result = False
        self.currentValue = math.asinh(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the gamma value of the current value
    def lgamma(self):
        self.result = False
        self.currentValue = math.lgamma(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the degree of the current value
    def degrees(self):
        self.result = False
        self.currentValue = math.degrees(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the logarithmic base(2) value of the current value
    def log2(self):
        self.result = False
        self.currentValue = math.log2(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the logarithmic base(10) value of the current value
    def log10(self):
        self.result = False
        self.currentValue = math.log10(float(outputBox.get()))
        self.display(self.currentValue)
 
    #uses bult in math function to calculate the logarithmic function(x+1) of the current value
    def log1p(self):
        self.result = False
        self.currentValue = math.log1p(float(outputBox.get()))
        self.display(self.currentValue)
 
add_calculation = Calculator()  #make a class that uses the calculator function and subfunctions
 
# create the textbox that will display the user inputs and calcuation results
outputBox = Entry(calc, font=('Arial',20,'bold'),bg='white',fg='black',bd=30,width=28,justify=RIGHT)
outputBox.grid(row=0,column=0, columnspan=4, pady=1)
outputBox.insert(0,"0")
 
#Use a for loop to create numbers buttons on calculator
keypad = "789456123" #need numbers to appear in this order for the calculator
i=0
button = []
for j in range(2,5): #define what rows
    for k in range(3): #define what columns
        button.append(Button(calc, width=6, height=2, bg='blue',fg='white', font=('Arial',20,'bold'),bd=4,text=keypad[i]))
        button[i].grid(row=j, column= k, pady = 1)
        button[i]["command"]=lambda x=keypad[i]:add_calculation.User_Input(x)
        i+=1

#create a clear button for the calculator       
buttonClear = Button(calc, text=chr(67),width=6, height=2,bg='powder blue',font=('Arial',20,'bold'), bd=4,command=add_calculation.Clear_User_Input)
buttonClear.grid(row=1, column= 0, pady = 1)
 
#create a clear all button for the calculator
buttonClearAll = Button(calc, text=chr(67)+chr(69),width=6, height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=add_calculation.Clear_All_User_Input)
buttonClearAll.grid(row=1, column= 1, pady = 1)
 
#create a square root button for the calculator
buttonsquareroot = Button(calc, text="\u221A",width=6, height=2,bg='powder blue', font=('Arial',20,'bold'),bd=4,command=add_calculation.square_root)
buttonsquareroot.grid(row=1, column= 2, pady = 1)
 
#create an addition button for the calculator
buttonAddition = Button(calc, text="+",width=6, height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.operation("add"))
buttonAddition.grid(row=1, column= 3, pady = 1)
 
#create a subtraction button for the calculator
buttonSubstract = Button(calc, text="-",width=6,height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.operation("sub"))
buttonSubstract.grid(row=2, column= 3, pady = 1)
 
#create a multiplication button for the calculator
buttonMultiply = Button(calc, text="*",width=6,height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.operation("multi"))
buttonMultiply.grid(row=3, column= 3, pady = 1)
 
#create a division button for the calculator
buttonDivide = Button(calc, text="/",width=6,height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.operation("divide"))
buttonDivide.grid(row=4, column= 3, pady = 1)

#create a zero button for the calculator 
buttonZero = Button(calc, text="0",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.User_Input(0))
buttonZero.grid(row=5, column= 0, pady = 1)
 
#create a decimal button for the calculator 
buttonPeriod = Button(calc, text=".",width=6,height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=lambda:add_calculation.User_Input("."))
buttonPeriod.grid(row=5, column= 1, pady = 1)

#create a sign button for the calculator 
buttonPlusMinus = Button(calc, text=chr(177),width=6,height=2,bg='powder blue', font=('Arial',20,'bold'),bd=4,command=add_calculation.mathPM)
buttonPlusMinus.grid(row=5, column= 2, pady = 1)
 
#create an equals button for the calculator 
buttonEquals = Button(calc, text="=",width=6,height=2,bg='powder blue',font=('Arial',20,'bold'),bd=4,command=add_calculation.solve_expression)
buttonEquals.grid(row=5, column= 3, pady = 1)


#Add more buttons to ScientificVersion of calculator
labelDisplay = Label(calc, text = "Math Functions",font=('Arial',30,'bold'),fg='black',justify=CENTER)
labelDisplay.grid(row=0, column= 4,columnspan=4)


# row 1
#create a PI button for the calculator 
buttonPi = Button(calc, text="PI",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.pi)
buttonPi.grid(row=1, column= 4, pady = 1)

#create a cosine button for the calculator  
buttonCos = Button(calc, text="COS",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.cos)
buttonCos.grid(row=1, column= 5, pady = 1)

#create a tangent button for the calculator  
buttontan = Button(calc, text="TAN",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.tan)
buttontan.grid(row=1, column= 6, pady = 1)

#create a sine button for the calculator  
buttonsin = Button(calc, text="SIN",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.sin)
buttonsin.grid(row=1, column= 7, pady = 1)
 
# row 2
#create a degree button for the calculator 
buttondeg = Button(calc, text="DEG",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.degrees)
buttondeg.grid(row=2, column= 4, pady = 1)

#create a hyberbolic cosine button for the calculator  
buttoncosh = Button(calc, text="COSH",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.cosh)
buttoncosh.grid(row=2, column= 5, pady = 1)

#create a hyberbolic tangent button for the calculator  
buttontanh = Button(calc, text="TANH",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.tanh)
buttontanh.grid(row=2, column= 6, pady = 1)

#create a hyberbolic sine button for the calculator  
buttonsinh = Button(calc, text="SINH",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.sinh)
buttonsinh.grid(row=2, column= 7, pady = 1)
 
# row 3
#create a logarithmic button for the calculator
buttonlog = Button(calc, text="LOG",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.log)
buttonlog.grid(row=3, column= 4, pady = 1)

#create a logarithmic base(2) button for the calculator 
buttonlog2 = Button(calc, text="LOG2",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.log2)
buttonlog2.grid(row=3, column= 5, pady = 1)

#create a logarithmic base(10) button for the calculator
buttonlog10 = Button(calc, text="LOG10",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.log10)
buttonlog10.grid(row=3, column= 6, pady = 1)
 
#create a logarithmic function(x+1) button for the calculator
buttonlogpy = Button(calc, text="LOG1P",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.log1p)
buttonlogpy.grid(row=3, column= 7, pady = 1)
 
# row 4
#create a gamma button for the calculator 
buttongamma = Button(calc, text="GAMMA",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.lgamma)
buttongamma.grid(row=4, column= 4, pady = 1)

#create a exponential button for the calculator 
buttonExp = Button(calc, text="EXP",width=6, height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.exp)
buttonExp.grid(row=4, column= 5, pady = 1)

#create an inverse hyberbolic cosine button for the calculator 
buttonacosh = Button(calc, text="ACOSH",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.acosh)
buttonacosh.grid(row=4, column= 6, pady = 1)

#create an inverse hyberbolic sine button for the calculator  
buttonasinh = Button(calc, text="ASINH",width=6,height=2,bg='blue',fg='white',font=('Arial',20,'bold'),bd=4,command=add_calculation.asinh)
buttonasinh.grid(row=4, column= 7, pady = 1)
 
#resize the calculator window to show scientific functions
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568")
 
#resize the calculator window hide show scientific functions 
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")
 
#exits the calculator if you click exit on the menu
def ExitCalc():
    root.destroy()

#creates a menu for the calculator window
menubar = Menu(calc)
menubar.add_command(label = "Standard", command = Standard)
menubar.add_command(label = "Scientific", command = Scientific)
menubar.add_command(label = "Note Box", command = NoteBox)
menubar.add_command(label = "Exit", command = ExitCalc)
root.config(menu=menubar)
 
#start the program and keep it running
root.mainloop()
