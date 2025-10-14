stock = [
{
    "name": "Apple",
    "price": 1,
    "type": "Fruit",
    "description": "Xiyang's amazing apple."
},
{
    "name": "Orange",
    "price": 1,
    "type": "Fruit",
    "description": "Xiyang's amazing orange."
},
{
    "name": "Coca-Cola",
    "price": 1.5,
    "type": "Drink",
    "description": "Xiyang's amazing coca-cola."
},
{
    "name": "Sprite",
    "price": 1.5,
    "type": "Drink",
    "description": "Xiyang's amazing sprite."
},
{
    "name": "Takis",
    "price": 2.5,
    "type": "Snack",
    "description": "Xiyang's amazing takis."
},
{
    "name": "Potato Chips",
    "price": 2.5,
    "type": "Snack",
    "description": "Xiyang's amazing potato chips."
}
]
print("Welcome to Xiyang's amazing store! Stock:")
for index, item in enumerate(stock):
    print(index, ":", item["name"])
cart = []
buy = input("What would you like to buy?")
cart.append(buy)
cont = input("Do you want to continue? Type 'Yes' or 'No'")
while cont != "No":
    print(f"Your cart: {cart}")
    buy = input("What would you like to buy?")
    cont = input("Do you want to continue? Type 'Yes' or 'No'")
    if cont == 'Yes':
        buy = input("What would you like to buy?")
        cart.append(buy)
        print(f"Your cart: {cart}")
if cont == "No":
    print(f"Your cart: {cart}")
for i in range(len(cart)):
    x = 0
    if cart[x] == item["name"]:
        x += 1
        print(item["name"]["price"])