#find factorial of a number using while loop
n = 6
factorial = 1
# for i in range(n,1,-1):
#     factorial *= i;
# print(factorial);

while n > 0:
    factorial *= n
    n -= 1

print(f"Factorial of given number is:",factorial)
