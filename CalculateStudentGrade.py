# Python Program - Print Student Result Card and Graph View ***

import pandas as pd
import matplotlib.pyplot as plt

x=1
while x <10:
    i= input("Enter 'x' for exit and Y for continue = ")
    if i =='x' or i=='X':
        exit();
    else:
        stud_name = input("Enter the Student Name = ")
        stud_RegNo = input("Enter the Registration Number = ")
        stud_Class = input("Enter the Student Class = ")

        stud_Eng=      int(input("Enter the Student marks in English: ="))
        stud_Match=    int(input("Enter the Student marks in Maths: ="))
        stud_Phy=      int(input("Enter the Student Marks in Phyton: ="))
        stud_xml=      int(input("Enter the Student Marks in XML: ="))
        stud_Java=     int(input("Enter the student Marks in Java: ="))
        sum1 = stud_Eng + stud_Match + stud_Phy + stud_xml + stud_Java
        average = sum1/5;
        if(average>=91 and average<=100):
         stud_grade= "A+"
        elif(average>=81 and average<=90):
         stud_grade= "A"
        elif(average>=71 and average<=80):
          stud_grade= "B+"
        elif(average>=61 and average<=70):
          stud_grade= "B"
        elif(average>=51 and average<=60):
          stud_grade= "C+"
        elif(average>=41 and average<=50):
          stud_grade= "C"
        elif(average>=0 and average<=40):
          stud_grade= "F"
        else:
          stud_grade= print("Strange Grade..!!");
        print (" _____________________________________________")
        print (" ********************************************* ")
        print (" ********* HOME NETWORK INSTITUTE ************ ")
        print ("                 Result Card                   ")
        print ("_______________________________________________")

        print ("Name of Student =",stud_name)
        print ("Student Registration Number =",stud_RegNo)
        print ("Student Class : =",stud_Class)
        print (" *********************************************** ")
        print (" ----------------------------------------------- ")
        # Define a dictionary containing student data 
        data = {'Subject':['English', 'Math', 'Python', 'XML','Java'], 
        'Marks':[stud_Eng, stud_Match, stud_Phy, stud_xml, stud_Java]} 
        # Convert the dictionary into DataFrame  
        df = pd.DataFrame(data) 
        # select two columns 
        print(df[['Subject', 'Marks']])
        print ("Total Marks = 500 ")
        print ("Marks Obtained =",sum1)
        print ("Your Grade is = ",stud_grade)
        subj = ['English', 'Math', 'Python', 'XML','Java']
        marks= [stud_Eng, stud_Match, stud_Phy, stud_xml, stud_Java]
        plt.plot(subj,marks,color ='orange')
        plt.xlabel('Class Subjects')
        plt.ylabel('Student Marks Obtained')
        plt.title('Student Result Graph')
    plt.show()

    x=x+1
