
print(" Enter the year>=1700","\n")

day1,month1,year1=input("Enter DD/MM/YYYY: ").split("/") 
print("to")
day2,month2,year2=input("Enter dd/MM/YYYY: ").split("/")

d1=int(day1)
d2=int(day2)      
m1=int(month1) 
m2=int(month2)
y1=int(year1)
y2=int(year2) 

if d1 and d2<=31 and (d1 and d2) > 0:
    if m1 and m2<=12 and (m1 and m2) > 0: 
        if y1 and y2>=1700 and (y1 != y2) and (y1<y2):
            print("These are leap years:-")
            for i in range(y1,y2+1):
                if i % 4 ==  0:
                    print(i,end=" ")
                    continue
                
            print("\n","These are Non Leap Year:-")
            for i in range(y1,y2+1):
                if i % 4 >0:
                    print(i,end=" ")
         
        else:
            print("Enter the correct year")
    else:
        print("Enter the corrct month")
else:
    print("Enter the corrct day")