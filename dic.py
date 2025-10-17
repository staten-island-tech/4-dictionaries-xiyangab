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
total = []
cont = True
while cont != False:
    buy = input("what would you like to buy?")
    cart.append(buy)
    print(f"you bought: {cart}")
    a = input("do you want to continue? 'yes' or 'no'")
    if a == 'no':
        cont = False

x = 0
y = 0
for i in range(len(cart)):
    #fix this; this is assuming the order matches
    if cart[x] == stock[y]['name']:
        print(stock[x]['price'])
        x += 1
    elif cart[x] != stock[y]['name']:
        while cart[x] != stock[y]['name']:
            y += 1
        #make loop that checks for if cart and stock is same
# x = 0
# for i in range(len(cart)):
#     print(cart[x])
#     x += 1
