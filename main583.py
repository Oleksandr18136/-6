# Read two number sets
first_set = set(map(int, input("Введіть першу послідовність чисел через пробіл: ").split()))
second_set = set(map(int, input("Введіть другу послідовність чисел через пробіл: ").split()))

# Sort common numbers
common_sorted = sorted(first_set & second_set)

# Show result
print("Ви отримали спільні числа за зростанням:", *common_sorted)