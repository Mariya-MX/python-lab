n = int(input("Enter the size of list "))
lst = []
print("Enter the elements : ")
for i in range(n):
    n1 = float(input())
    lst.append(n1)
print("Positive numbers ")
for i in lst:
    if i >= 0:
        print(i)
