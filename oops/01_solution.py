class Vehicle:
    def __init__(self, start, stop): #constructor 
        self.on = start 
        self.off = stop
    
    def car(self):
        return f"Your car engine status is: {self.off}"

vehicle = Vehicle(1,2)

class Electric(Vehicle):
    def __init__(self, start, stop, battery_size):
        super().__init__(start,stop)
        self.batterysize = battery_size

class Hello:
    def greet():
        return "Hello from Hello class"

class Hi:
    def greeting():
        return "Hi from Hi class"
    

Mycar = Electric("on","off","85kHw")
#print(Mycar.car())
        

# print(vehicle.car())
#getter and setter in python with encapsulation
class Student(Hello,Hi):
    total_obj = 0
    def __init__(self,name,age):
        self.__name = name
        self.age = age
        Student.total_obj += 1
    
    def set_name(self,new_name):
        if len(new_name) > 2:
            self.__name = new_name
            return self.__name
        else:
            print("Name length is not sufficient")
    
    def get_name(self):
        return self.__name
    

stdObj = Student("Vinay", 34)
stdObj2 = Student("Aman", 36)
print(stdObj.get_name())
print(stdObj.set_name("Felix"))
print(stdObj2.greeting)
print(Student.total_obj) #checking object count to eleborate polymorphism