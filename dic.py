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
print("welcome to xiyangs amazing store!")
print("stock:")
for index, item in enumerate(stock):
    print(index, ":", item["name"])
cart = []
cont = True
while cont != False:
    buy = input("what would you like to buy? (type 'no' to stop buying)")
    cart.append(buy)
    print(f"""you bought: {buy}""")
    if buy == "no":
        cont = False