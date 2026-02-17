#asign food to dog and cat
animal_name = "cat";
age = 2;

if animal_name == "dog":
    if age<2:
        food_type = "Puppy";
    else:
        food_type = "Senior";
elif animal_name == 'cat':
    if age < 5:
        food_type = "Baby";
    else:
        food_type = "Senior";

print(f"The food type for {animal_name} is {food_type} {animal_name} food.");