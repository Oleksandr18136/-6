# Fridge items
fridge = {
    "butter": "це молочний продукт з високим вмістом жиру",
    "milk": "це білий молочний напій",
    "bread": "це хлібобулочний виріб з борошна"
}

# Read item name
item = input("Введіть назву продукту: ")

# Show result
if item in fridge:
    print("Ви отримали:", item, "-", fridge[item])
else:
    print("Ви отримали: продукт", item, "не знайдено в холодильнику")