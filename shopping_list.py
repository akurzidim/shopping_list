# coding: utf-8

new_list = []

add_item = raw_input("Do you want to add s.t. to your shopping list?. Answer with \"yes\" or \"no\": ")

while add_item == "yes":
    item = raw_input("What do you want to add to your shopping list? ")
    new_list.append(item)
    add_item = raw_input("Do you want to add more items? Answer with \"yes\" or \"no\": ")

if add_item == "no":
    print("Thank you. Here is your shopping list: %s") % new_list
else:
    print("Wrong input. Please say \"yes\" or \"no\"")
