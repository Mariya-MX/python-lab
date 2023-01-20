n = int(input("Enter number "))
rev = 0
for i in range(0, len(str(n))):
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("Reverse is ", rev)
