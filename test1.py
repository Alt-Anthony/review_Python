# 1° print

name = input("").strip()

#print("hello, ", name, sep='?',end='!')
#print(f"this is a {name}, type again to complete the {name}")
#name = name.title()

#strip() remove whitespaces
#title() 
first, last = name.split(" ")
print(f"this is a {first}, and my name is {last.capitalize()}")