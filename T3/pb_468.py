#Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file – friends.txt.
f=open("friend.txt","w+")
f.write("Friends are crazy, Friends are naughty !\n")
f.write("Friends are honest, Friends are  best !\n")
f.write("Friends are like keygen, friends are like license key !\n")
f.write("We are nothing without friends, Life is not possible without friends !\n")
f.close()

def display_oddLines():
    f=open("friend.txt","r")
    x=f.readlines()
    for i in range(0,len(x)):
        if i%2!=0:
            print(x[i].strip())

display_oddLines()