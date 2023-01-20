str=input("Enter the string:")
dict={}
print(str)
for i in str:
    print(i)
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
for m,n in dict.items():
    print(m,n)