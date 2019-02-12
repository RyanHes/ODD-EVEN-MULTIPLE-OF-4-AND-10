num = int(input("Give me a number:  "))
mod = num % 2
yep = num % 4
nod = num % 10
if mod > 0:
    print("THIS IS AN ODD NUMBER")
else:
    print("THIS NUMBER IS EVEN")
if yep == 0:
    print("THIS NUMBER IS A MULTIPLE OF 4")
else:
    print("THIS NUMBER IS NOT A MULTIPLE OF 4")
if nod % 10 == 0 :
    print("THIS IS A MULTIPLE OF 10")
else:
    print("THIS IS NOT A MULTIPLE OF 10")
    

