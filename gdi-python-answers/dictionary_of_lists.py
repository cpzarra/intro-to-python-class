mary_shopping_list = ['apples', 'bananas', 'chicken', 'ice cream']
fran_shopping_list = ['ice cream', 'beef', 'peppers', 'apples']
bob_shopping_list = ['chicken', 'peppers']

family_shopping_list = {
    'mary': mary_shopping_list,
    'fran': fran_shopping_list,
    'baby': bob_shopping_list,
}

for name, shop_list in family_shopping_list.items():
	print name, 'needs to buy: ', shop_list 

for key, value in family_shopping_list.items():
	if 'beef' in value:
		print key, 'wants beef'

# Changing this later can be accomplished with
family_shopping_list['fran'].append('strawberries')