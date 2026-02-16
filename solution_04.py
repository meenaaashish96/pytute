#furite ripeness checker
fruite = "banana";
color = "brown";

if color != 'green' and color != 'yellow' and color != 'brown' :
    raise "Invalid Color";

if color == 'green':
    status = 'Unripe';
elif color == 'yellow':
    status = 'Ripe';
else:
    status = 'Overripe';

print(f"The fruite is {status}");