name = input("Welcome to Robot coffee shop!!\nWhat's your name?\n")

menu = """1:- latte
2:- ice tea
3:- cold coffee
4:- black coffee"""

price = 5

order = input("Hello " + name + ", what would you like to order today?\t*enter item name*\n"+menu+"\n\n")

quantity = input("How many "+order+" would you like to order?\n")

total = price*int(quantity)

if order > "1":
    print("\nThanks "+name+", your "+quantity+" "+order+"'s would be ready in a moment!\nYour total bill amount is: $"+str(total))
else:
    print("\nThanks "+name+", your "+order+" would be ready in a moment!\nyour total bill amount is: $"+str(total))