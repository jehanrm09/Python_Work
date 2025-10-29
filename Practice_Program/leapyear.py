n=int(input("enter year : "))
if n%400==0 or n%4==0 :
    if n%100 !=0:
        print("year is leap year")
else:
    print("year is not leap year")