items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]
inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory:", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
chosen_items = input("Which item do you want to buy? ")
if chosen_items not in inventory or inventory[chosen_items] == 0:
    print(chosen_items, "is out of stock! Stopping the checker.")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked Up Prices:", marked_up_prices)

item_index = items.index(chosen_items)
chosen_price = marked_up_prices[item_index]
print("Price of", chosen_items, "after markup:", chosen_price)
item_index = items.index(chosen_items)
chosen_price = marked_up_prices[item_index]
print("Price of", chosen_items, "after markup:", chosen_price)

inventory[chosen_items] = inventory[chosen_items] - 1
print(chosen_items, "purchased! Remaining stock:", inventory[chosen_items])

print("")
print('===== SCHOOL STORE INVENTORY CHECKER =====')
print("Item Bought:", chosen_items)
print("Price Paid:", chosen_price)
print("Updated Inventory:", inventory)
print("====================================================")