# HW 3: Bakery

muffins = 10
cupcakes = 10
question = input('do you want a muffin or a cupcake? ')

while question != '0':
    if question == 'muffin':
        if muffins > 0:
            muffins -= 1
            print(f'You have bought a muffin. The store has {muffins} muffins left.')
        else:
            print('Sorry, Muffins are out of stock')
        
    elif question == 'cupcake':
        if cupcakes > 0:
            cupcakes -= 1
            print(f'You have bought a cupcake. The store has {cupcakes} cupcakes left.')
        else:
            print ('Sorry, Cupcakes are out fo stock')
    else:
        print('Invalid! write either: "muffin", "cupcake", or "0"')
    question = input('do you want a muffin or a cupcake? ')

print (f'Muffins: {muffins} Cupcakes: {cupcakes}')
