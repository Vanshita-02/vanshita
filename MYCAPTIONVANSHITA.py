from math import pi
r = float(input("Input the radius of the circle is :"))
print("The area of the circle with radius " + str(r) +"is: " +str(pi*r**2))

filename =input("input the filename :")
f_extns = filename.split(".")
print("the extension of the file is:"+ (f_extns[-1]))
