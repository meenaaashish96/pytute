#find first not repeated char
string = "aashish"
for char in string:
    if string.count(char) == 1:
        print("First not repeated char is:", char)
        break;
    # prechar = char
    # charcount = 0;
    # for newchar in string:
    #     if newchar == prechar:
    #         charcount +=1;
    # if(charcount == 1):
    #     print("First not repeated char is: ",prechar)
    
