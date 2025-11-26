#Write a function count_lines() to count and display the total number of lines from the file. Consider the following lines for the file – friends.txt.
f=open("friends.txt","w+")
string="Friends are crazy, Friends are naughty !\nFriends are honest, Friends are best !\nFriends are like keygen, friends are like license key !\nWe are nothing without friends, Life is not possible without friends !"
f.write(string)
f.close()

def count_lines():
    f=open("friends.txt","r")
    z=f.readlines()
    count=len(z)
    return count

print("Total numbers of lines: ",count_lines())