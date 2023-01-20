str1=input("Enter a string : ")
print(str1)
dict={}
a=str1.split()
print(a)
for i in a:
    if i  in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
