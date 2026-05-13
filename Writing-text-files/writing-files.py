import os

name=input("Enter the your name :")
to_write="Hello " + name + "\n"
with open(name+".txt", "w") as file:
    file.writelines(to_write)



count_until=int(input("Chose a number"))
to_write=""
for i in range(count_until):
    to_write+=str(i+1)+"\n"


with open('nums.txt', 'w') as file:
    file.writelines(to_write)