#Weather activity sugessions
weather = "Rainy".lower();
if(weather not in ["sunny", "rainy", "snowy"]):
    print('Invalid weather information!');
    exit();
if weather == "sunny":
    message = "Go for walk";
elif weather == "rainy":
    message = "Read a book";
elif weather == "snowy":
    message = "Build a snowman";

print(message);