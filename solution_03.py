#as per the score calculate grade
score = int(input("Enter your score:"))

if(score>100):
    raise "Wrong grading !";


if(score < 60):
    grade = "F";
elif(score>=60 and score<70):
    grade = "D";
elif(score>=70 and score<80):
    grade = "C";
elif(score>=80 and score<90):
    grade = "B";
else:
    grade = "A";

print("Your grade is:", grade);