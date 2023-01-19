n = int(input("Enter the limit "))
lst = []
s = 0
print("Enter the elements in the list")
for i in range(n):
    n = int(input())
    lst.append(n)
    s = s + lst[i]
print(lst)
print("sum of elements=", s)
