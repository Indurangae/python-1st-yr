#Author - Induranga Ekanayake
#Student ID - w1954091 (20220908)
# Date - 10.12.2022


marks = []    #open list

a = 0
b = 0
c = 0
d = 0

while True:
    try:
        while True :
            try:
                print()
                credit_pass = int(input("Please enter your credits at pass : "))
                if credit_pass % 20 != 0 or credit_pass > 120 or credit_pass < 0:      #conditions for pass credit
                    print("Out of range")
                    continue
                else:
                    break
            except:
                print("Integer required")
                continue
        while True :
            try:
                credit_defer = int(input("Please enter your credits at defer : "))
                if credit_defer % 20 != 0 or credit_defer > 120 or credit_defer < 0:   #conditions for defer credit
                    print("Out of range")
                    continue
                else:
                    break
            except:
                print("Integer required")
                continue
        while True :
            try:
                credit_fail = int(input("Please enter your credits at fail : "))
                if credit_fail % 20 != 0 or credit_fail > 120 or credit_fail < 0:      #conditions for fail credit
                    print("Out of range")
                    continue
                else:
                    break
            except:
                print("Integer required")
                continue
        total=credit_pass+credit_defer+credit_fail
        if total != 120:
            print(" Total incorrect")
            continue
        if credit_pass == 120:
            print("Progress")
            a += 1
            marks.append("Progress - ")
            marks.append(credit_pass)
            marks.append(credit_defer)         # add to the list
            marks.append(credit_fail)
        elif credit_pass == 100:
            print("Progress (module trailer)")
            b += 1
            marks.append("Progress (module trailer) - ")
            marks.append(credit_pass)
            marks.append(credit_defer)      # add to the list
            marks.append(credit_fail)
        elif credit_fail > 70:
            print("Exclude")
            c += 1
            marks.append("Exclude - ")
            marks.append(credit_pass)
            marks.append(credit_defer)      # add to the list
            marks.append(credit_fail)
        else:
            print("Do not progress – module retriever")
            d += 1
            marks.append("Do not progress – module retriever - ")
            marks.append(credit_pass)
            marks.append(credit_defer)    # add to the list
            marks.append(credit_fail)

                
        enter1 = (input("""
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """))
        while enter1 != "q" and enter1 != "y":
            print("Invalid input")
            enter1 = (input("""
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """))
        if enter1 == "y":
            continue
        if enter1 == "q":
            print("You have exit the program")
            break
            
    except:
        print("Integer required")
        continue
  

#histogram
    
print()
print("-" * 60 )
print("Histogram")
print("progress",a," :", a * "*")
print("Trailer",b,"  :", b * "*")
print("Retriever",d,":", d * "*")
print("Excluded",c," :", c * "*")
print()
print(a+b+c+d, "Outcomes in total.")
print("-" * 60 )
print()

#List and file

file=open('Student_File.txt','w')

x = int(len(marks) / 4)
for I in range (x):
    print(marks[4*I],marks[4*I+1],",",marks[4*I+2],",",marks[4*I+3])
    file.write(str(marks[4*I])+" "+str(marks[4*I+1])+","+str(marks[4*I+2])+","+str(marks[4*I+3]))
    file.write('\n')

file.close()






    
    




    
