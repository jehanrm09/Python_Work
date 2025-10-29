n = int(input("Enter total days:"))
year = n//360
month = (n %360)//30
days = (n %360)%30
print(f"YEAR :{year} \nMONTHS : {month} \nDAYS : {days}")