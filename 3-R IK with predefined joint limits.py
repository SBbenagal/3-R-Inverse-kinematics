# The code is compiled by Shashi Benagal :) :)
# ONLY FOR 3-R ROBOT
# DONT KEEP Y VALUE IN  it will not proceed further
#please cross verify values in CAD softwares like CATIA SE if it gives wrong answer dont blame me guys :) it may be cuz of ur fault...
#this is copyrighted highly material :) use it for educational purpose only
#If it heps in building your project dont forget to donate.

from Tkinter import *
import tkMessageBox
import time
import serial
import math
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
#+++++++++++++Variables
#ser = serial.Serial('com25', 9600)
#++++++++++++++++Functions+++++++++++++++++++++++
def move():
    X=x.get()
    Y=y.get()
    Z=z.get()
    deg=180/3.141
    r2= X-A
    d=Z
    ase=Fraction(d,p)
    base=float(ase)
    #ka = math.atan(Y/X)
    #base = int(round(ka*deg))
    #k=Fraction(r2,Y)
    k2=float(r2)
    p2=math.atan(k2/Y)
    r3= math.sqrt((Y**2)+(r2**2))
    pa=((C**2)-(B**2)-(r3**2))
    pb=(-2*B*r3)
    c=(float(pa)/pb)
    p1= math.acos(c)
    shoulder = int((p2-p1)*deg)   
    p3=math.acos(float((r3**2)-(B**2)-(C**2))/(-2*B*C))*deg
    elbow =int(round((180-p3)))

    #this function sends the command of jointangles to the arduino to move the servos to thedesired positions
    command = str(base) + ',' + str(shoulder) + ',' + str(elbow) +  'd'
    print (command)
    plt.clf()
    pp=552*math.cos(shoulder)
    pq=552*math.sin(shoulder)
    #qp=102+(350*math.cos(shoulder+elbow))+(450*math.cos(shoulder))
    #qq=(350*math.sin(shoulder+elbow))+(450*math.sin(shoulder))
    go=[0,0,pp,X]
    gu=[0,102,pq,Y]
    
    plt.scatter(X,Y,marker=10)
    plt.scatter(0,0,marker="o")
    plt.plot(go,gu,markevery=0)
    print (pp)
    print (pq)
    
    print (shoulder)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.axis([-850,850,-850,850])
    plt.text(X,Y,'({},{})'.format(X,Y))
    
    #for i_go,i_gu in zip(go,gu):
     #   plt.text(i_go,i_gu,'({},{})'.format(i_go,i_gu))
    plt.show()
    #ser.write(command)
    #if not in the commandline can printverification to a notification window
    #tkMessageBox.showinfo( "Hello Python","message sent")
    #++++++++++++++++++++The GUI++++++++++++++++++++++
root = Tk()
#++++++++++++++++++++Drive Motors++++++++++++++++++
motorControl = Frame(root)
motorControl.pack()
forwardFrame = Frame(motorControl)
forwardFrame.pack()
backFrame = Frame(motorControl)

backFrame.pack (side = BOTTOM)
speedControl = Frame(root)
speedControl.pack()
A= 102; #base link length
B= 450; #shoulder link length
C= 350;
p=5;#elbow link lengt
#+++++++++++++++++ARM+++++++++++++++++++++++++
# The scroll bars
armControl = Frame(root)
armControl.pack( )
armLabel = Label(armControl, text = "ArmComponets", bg = "red", padx = 100)
armLabel.pack()
#++++++++++++++++++++++++BASE+++++++++++++++++++++++++++
baseLabel = Label(armControl, text = "X axis", bg ="green", padx = 100)
baseLabel.pack()
x = Scale(armControl, from_= -250, to = 800,length = 300, orient = HORIZONTAL)
x.pack()
#++++++++++++++++++++++++Shoulder+++++++++++++++++++++++++
shoulderLabel = Label(armControl, text ="Y axis", bg = "green", padx = 100)
shoulderLabel.pack()
y = Scale(armControl, from_= -700, to = 700,length = 300, orient = HORIZONTAL)
y.pack()
#++++++++++++++++++++++ELBOW++++++++++++++++++++++++++++
elbowLabel = Label(armControl, text = "Z axis", bg= "green", padx = 100)
elbowLabel.pack()
z = Scale(armControl, from_= 0, to = 500,length = 300, orient = HORIZONTAL)
z.pack()
command = move
#++++++++++++++++++++++ELBOW++++++++++++++++++++++++++++
#Send
armGoBut = Button(armControl, text ="Move arm",height = 2, width = 5,command = move )
armGoBut.pack()
root.mainloop()

