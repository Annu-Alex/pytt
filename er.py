y= int(input("Enter a temperature"))
scale=input("Is this is in (C)elsius or (F)ahrenheit?")
if scale=="C":
   f=(9/5*y)+32
   print(y,"Celsius is",f,"fahrenheit")
else:
    c=5/9*(y-32)
    print(y,"Fahrenheit is",c,"celsius")