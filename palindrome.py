n = int(input("Enter number "))
s = 0
temp = n
for i in range(0, len(str(n))):
    rec = n % 10
    s = s * 10 + rec
    n = n // 10
if temp == s:
    print("It is a palindrome number")
else:
    print("Not a palindrome  number")
