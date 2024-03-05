from math import sqrt

a = int(input("Please enter A: "))
b = int(input("Please enter B: "))
c = int(input("Please enter C: "))

p = (a + b + c)

k = p/2

ans = sqrt(k * (k - a) * (k - b) * (k - c))

print("The answer is: ",ans)


