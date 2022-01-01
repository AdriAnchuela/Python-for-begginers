#Shopping list

shopping = []

def shop():
    product = ''
    while product != 'end':
        product = str(input('Introduce an item: '))
        shopping.append(product)
    shopping.remove('end')
    print(shopping)

shop()