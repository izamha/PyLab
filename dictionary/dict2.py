# A generic dictionary to contain multiple product of dictionaries
products = {
    'RB00111': {'name': 'Rayban Sunglasses', 'price': 112.2, 'models': ['black', 'tortoise']},
    'DWC0317': {'name': 'Drone with Camera', 'price': 75.29, 'models': ['white', 'black']},
    'MTS0540': {'name': 'T-Shirt', 'price': 12, 'models': ['small', 'medium', 'large']},
    'EVD2989': {'name': 'Echo Dot', 'price': 29.5, 'models': []}
}

print(f"{'ID':<6} {'Name':<17} {'Price':>8} {'models'}")
print('-' * 60)

# Loop thru each dictionary in the products dictionary
for oneproduct in products.keys():
    # Get the id of one product
    ID = oneproduct
    # Get the name of one product
    name = products[oneproduct]['name']
    # Get the unit price of one product and format with $
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    # Create an empty string variable named models
    models = ''

    # Loop thru the models list and tack onto models
    # One item from the list followed by a comma and space
    for m in products[oneproduct]['models']:
        models += m + ', '
    # if the models variable is more than two characters in length
    # Peel off the last two characters (Last comma and space)
    if len(models) > 2:
        models = models[:-2]
    else:
        models = '<none>'
    # print all the variables with a neat f-string
    print(f"{ID:<6} {name:<17} {unit_price:>8} {models}")
