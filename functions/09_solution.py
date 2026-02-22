#create a yield function to print even number of given range
def print_even(rng):
    for i in range(2,rng+1,2):
    #     if i%2 == 0:
        # print(i);
        yield i


for num in print_even(77):
    print(num)