num = int(input("Enter the number "))
n1 = 0
n2 = 1
total = 0
if num <= 0:
    print("Enter a valid number")
elif num == 1:
    print(n1)
else:
    print("fibonacci sequence ")
    while total < num:
        print(n1)
        s = n1 + n2
        n1 = n2
        n2 = s
        total += 1
