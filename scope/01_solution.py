#global #function #block #closer #bagtheory
x=99
def f1():
    #print(x) #x valuable come from global scope
    #global x #to manipulat global variable or to define global variable
    x=34
    def f2():
        print(x) #output will be 34 and not affect global variable
    
    return f2()

result = f1()
 
#that is called closed in python like it will we return refrence of f2() so it will run f2 but print value of "34" just because of it will hold the in bag like memnory refrence of cloasest value.

#closer or factory function
def closer_fun(num):
    def main(x):
        print("x:", x)
        return x**num
    return main

a = closer_fun(2)  #num = 2
b = closer_fun(3)  #num = 3

print(a(3)) #x = 3
print(b(3)) #x = 3

#that is called cloaser just because of here main not excuted come as refrence in a and b and when we execute and pass value it will change the value of main x function not num
