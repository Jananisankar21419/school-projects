#program to find biggest number
#title

print(" -------- biggest among 3 numbers------- ")
val1 = int(input("enter the first num= "))
val2 = int(input(" enter the second num = "))
val3 = int(input(" enter the third num= " ))
#condition

if (val1 > val2) and (val1 > val3): biggest= val1
elif (val2 > val1) and (val2 > val3 ):biggest =val2
else:
    biggest = val3
print(" the biggest number is =",biggest)
print(" ========program ends here======")
#ending
