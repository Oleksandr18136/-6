# Countries and capitals
capitals = {
    "Ukraine": "Kyiv",
    "France": "Paris",
    "Denmark": "Copenhagen",
    "China": "Beijing",
    "Canada": "Ottawa"
}

# Sort descending by capital
result = sorted(capitals.items(), key=lambda x: x[1], reverse=True)

# Show result
print("Ви отримали відсортований список (за спаданням столиць):", result)