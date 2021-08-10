

def write_file(products):
    to_send = ''
    for product in products:
        p = f'''Product:  {product['name'].strip()}\n''' + f'''Price:  {product['org_price'].strip()}''' + (
            f'''\nCurrent price:  {product['curr_price']}''' if product['curr_price'] else '')

        to_send = to_send + p + '\n' + '###################################' + '\n'

    return to_send
