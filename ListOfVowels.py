srt = str(input("Enter string :"))
lst = []
for i in srt:
    if i == 'a' or i == 'e' or i == 'i' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        lst.append(i)
print("Vowels=", lst)
