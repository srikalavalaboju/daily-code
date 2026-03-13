s = "python programming"
count = 0

for char in s:
    if char in "aeiouAEIOU":
        count += 1

print("Vowels:", count)