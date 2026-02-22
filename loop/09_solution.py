#remove duplicate items from list 
list = ["aa","bb","ab","ba","bb","cc","ba"];

for item in list:
    if list.count(item) > 1:
        list.remove(item);

print(list);