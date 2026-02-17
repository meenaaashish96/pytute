#check password strength
password = "safh63@";
password_length = len(password);
if password_length < 6:
    strength = "WEAK"
elif password_length <= 10:
    strength = "MEDIUM"
else: 
    strength =  "STRONG"

print("Your password is :", strength)