#Create two dictionaries to represent information about two pets
# the pet dictionary
Malachi = {
    'type of pet': 'Cane Corso Dog',
    'color': 'Black',
    'nickname': 'MB',
    'owners name': 'Mayes',
}
Ruger = {
    'type of pet': 'Basenji Dog',
    'color': 'Brown and White',
    'nickname': 'Rugie',
    'owners name': 'Taraneh',
}

#Part 2
england = {'Capital': 'London'}
france = {'Capital': 'Paris'}
belgium = {'Capital': 'Brussels'}

england['population'] = '53.01 million'
france['population'] = '66.9 million'
belgium['population'] = '11.35 million'

england['Interesting fact'] = 'The Queen has her own poet'
france['Interesting fact'] = 'French love cheese'
belgium['Interesting fact'] = 'Belgium produces more than 220,000 tons of chocolate per year'

england['top language'] = 'English'
france['top language'] = 'French'
belgium['top language'] = 'Dutch'

#Iterate over each dictionary, printing each key-value pair on one line
for key, value in england.items():
    print(key + ": ", value)

for key, value in france.items():
    print(key + ": ", value) 
    
for key, value in belgium.items():
    print(key + ": ", value) 
    

#Part3


pizza_order = {
    'customers_name': 'Sam',
    'Size': 'Large',
    'Crust': 'Thick',
    'Toppings': 'Sausage, Mushrooms, Olives',
}
print("Thank you for your order,", pizza_order.get('customers_name') + "!")
print("You have ordered a", pizza_order.get('Size'),pizza_order.get('Crust'), "with the following toppings: ")
print(pizza_order.get('Toppings'))