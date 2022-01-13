# 1. Create a shopping cart
from turtle import width


myItems = []
cartTotal = 0

def addItem(itemName, itemPrice):
    myItems.append(itemName)
    return(itemPrice)

cartTotal += addItem('DJI Mini 2 Drone', 220.87)
cartTotal += addItem('Shoes', 51.23)
cartTotal += addItem('Jeans', 39.89)
cartTotal += addItem('How To Grow A Moustache Like Ryan - Paperback Edition', 28.87)
cartTotal += addItem('RYAN TIME Official Soundtrack', 10.28)
cartTotal += addItem('Becoming An Ethical Hacker: The Basics - Hardcover Edition', 20.98)
cartTotal += addItem('Cracking the Coding Interview - Paperback Edition', 34.17)

cartSummary = dict((item,myItems.count(item))for item in myItems)

print(cartSummary)
print(cartTotal)






# 2. module in vscode func1 calculate square footage of a house
length = int(input("Enter the length:"))
width = int(input("Enter the length"))
squareFootage = length * width
print("Square Footage of House ="+str(squareFootage))

# func2 calculate circumference of a circle
radius = int(input("Enter the Radius:"))
circumference = radius * 2 * 3.14
print("Circumference of the Circle ="+str(circumference))