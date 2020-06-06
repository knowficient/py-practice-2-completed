# hint:
#   using print("* ", end="") to print an asterisk
#   and set cursor at last position without moving to next line
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

num = 5                     # set loop to 5
for x in range(num):        # set first loop 0..4
    for y in range(x):      # set second loop from 0 to x (move along row)
        print("* ", end="") # print * but do not move to next line
    print("")               # print next line after each row

for x in range(num,0,-1):   # set first loop 5..0
    for y in range(x):      # set second loop from 0 to X
        print("* ", end="") # print * but do not move to next line
    print("")               # print next line after each row









