score = int(input("Enter your score:"))

if(score < 60):
    grade = "F";
elif(score>=60 and score<70):
    grade = "D";
elif(score>=70 and score<80):
    grade = "C";
elif(score>=80 and score<90):
    grade = "B";
elif(score>100):
    raise "Wrong grading !";
else:
    grade = "A";

print("Your grade is:", grade);