mary_shopping_list = ['apples', 'bananas', 'chicken', 'ice cream']
fran_shopping_list = ['ice cream', 'beef', 'peppers', 'apples']
bob_shopping_list = ['chicken', 'peppers']

family_shopping_list = []
family_shopping_list.append(mary_shopping_list)
family_shopping_list.append(fran_shopping_list)
family_shopping_list.append(bob_shopping_list)

print family_shopping_list

for shop_list in family_shopping_list:
    for food_item in shop_list:
        print food_item