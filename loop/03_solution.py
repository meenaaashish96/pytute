#print multiplication table of 10 and skip itration 5;
num = 10;
skip = 5;

for i in range(1,10+1):
    if i == 5:
        continue
        print(num,'X',i," = ",i*num)


