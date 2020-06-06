# convert temperature to and from Celsius (C) or Fahrenheit (F)
# 2 Equations; C = (5(F-32))/9 and F = (9C + (32*5))/5
# User would input say 55C, 131F or even 55c
# Express your result to the nearest one unit (No decimal value) using round()

temp = input("Enter the temperature to convert? (eg. 55C, 131F, etc) : ")
degree = int(temp[:-1]) #get digits
method = str(temp[-1])  #get last alphabet

if method.upper() == "F":            # using upper() to convert char to upper case for F
    result = round((degree-32)*5/9)  # perform conversion and apply round to nearest one unit
    standard = "Celsius"             # set standard as Celsius to be printed later
elif method.upper() == "C":          # using upper() to convert char to upper case for C
    result = round((9*degree)/5+32)  # perform conversion and apply round to nearest one unit
    standard = "Fahrenheit"          # set standard as Celsius to be printed later
else:                                # take care of improper input like 55 or 55X
    print("Improper input")
    quit()

print("The temperature in", standard, "is", result, "degrees.")

