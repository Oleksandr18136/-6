# Read two number sets
first_set = set(map(int, input("Введіть першу послідовність чисел через пробіл: ").split()))
second_set = set(map(int, input("Введіть другу послідовність чисел через пробіл: ").split()))

# Count common items
count = len(first_set & second_set)

# Show result
print("Ви отримали кількість спільних чисел:", count)