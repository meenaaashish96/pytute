#prime number : A whole Number divisible by 1 and itself only.

number = 7

if number>1:
    for i in range(2,29):
        if (number%i) == 0:
            print("Number is not prime")
            break
        else:
            print("Number is prime")
            break

