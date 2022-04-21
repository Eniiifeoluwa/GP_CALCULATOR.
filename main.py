from math import *
import datetime
def exam(calculator):
    print(calculator)
exam("Welcome, You are about checking your result on the " + str(datetime.datetime.now()) + " P.M \n Kindly solve this mathematical question to show that you are qualified for being a science University" )
Question1=  9
Question2 =   64
School1 = input("What is the ceiling of 8.5: ")
School2 = input("What is the cube of 4: ")
if School1 == str(Question1) and School2 == str(Question2) :
    print(' Wow! You passed the examination.')
else:
    print('Please, you failed. read very well next time. Thank you!')
className = input( "Enter your General studies' exam score: ")
studentPercentage = input( "Input your overall percentage: ")
score = className
percentage = 60
average = 50
if (className >= str(average)) and (studentPercentage > str(average)) :
    print('You passed the examination, You are qualified to write your final exam.')
else:
    print("We are sorry,You failed! Try again later.")

name = input("Enter your name: ")
age = input("Enter your age: ")
level = input("Enter your level: ")

GPA1 = input(" Enter your first semester GPA: ")
GPA2= input("Enter your second semester GPA: ")
VGPA= (float(GPA1) + float(GPA2))
CGPA = (VGPA / 2)
print ("Hello, " + name + ("! You are ") + age + " years old ,You are in " +level +" level" +  "\n Your CGPA is " + str(CGPA) + ",Thank you.")

