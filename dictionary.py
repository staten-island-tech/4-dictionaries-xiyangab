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
prices = []
cont = True
while cont != False:
    buy = int(input("what would you like to buy?"))
    if buy in range(len(stock)):
        prices.append(stock[buy]['price'])
    cart.append(buy)
    a = input("do you want to continue? 'yes' or 'no'")
    if a == 'no':
            cont = False
total = sum(prices)
print(f"you total is: ${total}")