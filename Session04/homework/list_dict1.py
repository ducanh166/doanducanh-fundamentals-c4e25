inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#C
inventory['pocket'] = ['seashell','strange berry','lint']
print(inventory)
#D
inventory['backpack'].remove("dagger")
print(inventory['backpack'])
#u
inventory['gold'] = 50
print(inventory['gold'])