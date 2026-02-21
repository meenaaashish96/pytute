#create a function that accept multiple arguments and return sum of them

def all_arg_sum(*args):
    return sum(args)

print(all_arg_sum(3,3,2,1,3,4))