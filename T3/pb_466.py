#Write a python program to create and read the city.txt file in one go and print the contents on the output screen.
f=open("city.txt","w+")
f.write("This is pb question 466")
f.seek(0)
z=f.read()
f.close()
print(z)