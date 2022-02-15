print("welcome to Robot coffee shop!!\n")
item_1 = ["latte", 7]
item_2 = ["ice tea", 5]
item_3 = ["cold coffee", 12]
item_4 = ["black coffee", 10]
menu = """1:- latte
2:- ice tea
3:- cold coffee
4:- black coffee"""

name = input("What is your name?\n")
order = input("hello "+name+", what woud you drink?\t*enter item name*\n"+menu+"\n\n")

if order == item_1[0]:
    quantity = input("how many "+order+" would you like to order?\n")
    total = item_1[1] * int(quantity)
elif order == item_2[0]:
    quantity = input("how many "+order+" would you like to order?\n")
    total = item_2[1] * int(quantity)
elif order == item_3[0]:
    quantity = input("how many "+order+" would you like to order?\n")
    total = item_3[1] * int(quantity)
elif order == item_4[0]:
    quantity = input("how many "+order+" would you like to order?\n")
    total = item_4[1] * int(quantity)
else:
    print("please check your spelling!! and run again")
    exit()

print("your billing ammount is: "+str(total)+"$ \nyour "+order+" will be ready in a moment!")