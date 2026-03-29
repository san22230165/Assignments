#Mini Assignment given on 15thMarch2025
#Batch: 119
#Write a python program to print Alphabets from A to Z

#Explanation: To achieve this we use chr() its an in build function in every programming language
#This takes an integer argument and converts to its equivalent character

print(f"Welcome to my program. \n")
start=97
end=97+25 #as we have 26 alphabets in english
for i in range(start,end):
    print(chr(i).upper())