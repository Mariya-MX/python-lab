num = int(input("Enter the number of strings: "))
lst = []
count = 0
print("Enter strings")
for i in range(num):
    n = str(input())
    lst.append(n)
print(lst)
for i in lst:
    for j in i:
        if j == 'a':
            count += 1
print(count)
