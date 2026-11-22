# Read string
text = input("Введіть рядок символів: ")

# Count letters and digits
letters = 0
digits = 0
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# Show counts
print("Ви отримали: літер -", letters, ", цифр -", digits)