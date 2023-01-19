n1 = int(input("Enter start year "))
n2 = int(input("Enter last year "))
print("Leap years:")
for i in range(n1, n2):
    if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
        print(i)
