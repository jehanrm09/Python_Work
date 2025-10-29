import math
#taking hour from user and converting it into min and sec
'''hour = int(input("Enter hours:"))
if hour>0:
    min = hour*60
    sec = hour*3600
    print(f"HOURS={hour}  MIN={min}  SEC={sec}")'''

#FINDING INTEGER EXPONENT
base = int(input("Enter base:"))
ans = int(input("Enter ans:"))
x=int(math.log(ans,base))
print(x)
