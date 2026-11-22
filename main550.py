# Countries and capitals
capitals = {
    "Ukraine": "Kyiv",
    "France": "Paris",
    "Denmark": "Copenhagen",
    "China": "Beijing",
    "Canada": "Ottawa"
}

# Sort ascending by capital
result = sorted(capitals.items(), key=lambda x: x[1])

# Show result
print("Ви отримали відсортований список (за зростанням столиць):", result)