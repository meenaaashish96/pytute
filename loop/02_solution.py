#calculate some of even number
n = 10;
sum = 0;
for num in range(1,n+1):
    if num%2 == 0:
        sum += num;

print(f"Sum of even numbers is: ",sum)
