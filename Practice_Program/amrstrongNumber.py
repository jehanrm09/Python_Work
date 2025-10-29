n=int(input("enter number"))
c=ans=0
temp=n

while n>0:
    c+=1
    n//=10
print(c)

n=temp
while n>0:
    r=n%10
    ans=ans+r**c
    n=n//10
print(ans)

if(ans==temp):
    print("number is armstrong number")
else:
    print("number is not armstrong number")