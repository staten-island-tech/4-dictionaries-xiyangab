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
    "name": "Banana",
    "price": 1,
    "type": "Fruit",
    "description": "Xiyang's amazing banana."
},
{
    "name": "Grapes",
    "price": 2,
    "type": "Fruit",
    "description": "Xiyang's amazing grapes."
},
{
    "name": "Strawberry",
    "price": 2,
    "type": "Fruit",
    "description": "Xiyang's amazing strawberry."
},
{
    "name": "Pineapple",
    "price": 3,
    "type": "Fruit",
    "description": "Xiyang's amazing pineapple."
},
{
    "name": "Mango",
    "price": 3,
    "type": "Fruit",
    "description": "Xiyang's amazing mango."
},
{
    "name": "Watermelon",
    "price": 4,
    "type": "Fruit",
    "description": "Xiyang's amazing watermelon."
},
{
    "name": "Coca-Cola",
    "price": 2,
    "type": "Drink",
    "description": "Xiyang's amazing coca-cola."
},
{
    "name": "Sprite",
    "price": 2,
    "type": "Drink",
    "description": "Xiyang's amazing sprite."
},
{
    "name": "Pepsi",
    "price": 2,
    "type": "Drink",
    "description": "Xiyang's amazing pepsi."
},
{
    "name": "Fanta",
    "price": 2,
    "type": "Drink",
    "description": "Xiyang's amazing fanta."
},
{
    "name": "Iced Tea",
    "price": 3,
    "type": "Drink",
    "description": "Xiyang's amazing iced tea."
},
{
    "name": "Lemonade",
    "price": 3,
    "type": "Drink",
    "description": "Xiyang's amazing lemonade."
},
{
    "name": "Bottled Water",
    "price": 1,
    "type": "Drink",
    "description": "Xiyang's amazing bottled water."
},
{
    "name": "Takis",
    "price": 3,
    "type": "Snack",
    "description": "Xiyang's amazing takis."
},
{
    "name": "Potato Chips",
    "price": 3,
    "type": "Snack",
    "description": "Xiyang's amazing potato chips."
},
{
    "name": "Popcorn",
    "price": 2,
    "type": "Snack",
    "description": "Xiyang's amazing popcorn."
},
{
    "name": "Pretzels",
    "price": 2,
    "type": "Snack",
    "description": "Xiyang's amazing pretzels."
},
{
    "name": "Chocolate Bar",
    "price": 2,
    "type": "Snack",
    "description": "Xiyang's amazing chocolate bar."
},
{
    "name": "Granola Bar",
    "price": 2,
    "type": "Snack",
    "description": "Xiyang's amazing granola bar."
},
{
    "name": "Beef Jerky",
    "price": 4,
    "type": "Snack",
    "description": "Xiyang's amazing beef jerky."
},
{
    "name": "Carrot",
    "price": 1,
    "type": "Vegetable",
    "description": "Xiyang's amazing carrot."
},
{
    "name": "Broccoli",
    "price": 2,
    "type": "Vegetable",
    "description": "Xiyang's amazing broccoli."
},
{
    "name": "Tomato",
    "price": 1,
    "type": "Vegetable",
    "description": "Xiyang's amazing tomato."
},
{
    "name": "Cucumber",
    "price": 1,
    "type": "Vegetable",
    "description": "Xiyang's amazing cucumber."
},
{
    "name": "Lettuce",
    "price": 1,
    "type": "Vegetable",
    "description": "Xiyang's amazing lettuce."
},
{
    "name": "Ice Cream",
    "price": 4,
    "type": "Dessert",
    "description": "Xiyang's amazing ice cream."
},
{
    "name": "Cupcake",
    "price": 3,
    "type": "Dessert",
    "description": "Xiyang's amazing cupcake."
},
{
    "name": "Cookie",
    "price": 2,
    "type": "Dessert",
    "description": "Xiyang's amazing cookie."
},
{
    "name": "Brownie",
    "price": 3,
    "type": "Dessert",
    "description": "Xiyang's amazing brownie."
},
{
    "name": "Donut",
    "price": 2,
    "type": "Dessert",
    "description": "Xiyang's amazing donut."
}
]

print("welcome to xiyangs amazing store!")
print("stock:")
for index, item in enumerate(stock):
    print(index, ":", item["name"])
cart = []
cont = True
while cont != False:
    buy = int(input("what would you like to buy?"))
    if buy in range(len(stock)):
        cart.append(stock[buy])
    a = input("do you want to continue? 'yes' or 'no'")
    if a == 'no':
            cont = False
total = []
for i in cart:
     total.append(i['price'])
print(f"you total is: ${sum(total)}")
print(f"you bought {len(cart)} items")