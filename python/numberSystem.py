n=int(input("enter number"))
def num(n):
     a={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",
   12:"twelve",13:"thirteen",14:"forteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
  20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty"}
     if n<=20:
        return a[n]
     elif n<100:
        if n%10==0:
            return a[n]
        else:
            return a[(n//10)*10]+" "+a[n%10]
     elif n<1000:
        if n%100 == 0:
            return a[n//100]+" hundred "
        else:
            return a[n//100]+" hundred"+ " " + num(n%100)
print(num(n))