#keep asking use for input until they not enter number in between 1 to 10
while True:
    number = int(input("Enter a number in between 1 to 10: "))
    if number in range(1,10+1):
        print("Thank you we got the expected number:", number)
        break
