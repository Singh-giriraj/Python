print("hello welcom to networkcuk coffee shop\n")
name=input("what is your name?\n")
menu="black coffee, milk coffee, or latte"
price=8
print("hello "+name+" what would you like to have today form our menu?\n"+menu)
order_item=input()
print("and how many of "+order_item+" would you like to order?\n")
order_num=input()
total=int(order_num)*price
print("thanks "+name+"  your grand total is: $"+str(total)+"\nyour order will be ready in a moment")
