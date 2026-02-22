#create a function that support kwargs
def accept_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

accept_kwargs(name="aashsih",age="29",gender="male")