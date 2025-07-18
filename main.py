from shoppingcart import ShoppingCart

def print_menu(ShoppingCart):
    user_input = ''

    while user_input != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' description')
        print('o - Output shopping cart')
        print('q - Quit')

        while True:
            try:
                user_input = input('Choose an option: ').strip().lower()

                if len(user_input) == 0:
                    raise Exception
                elif user_input not in ('a', 'r', 'c', 'i', 'o', 'q'):
                    raise Exception
                break
            except Exception:
                print('Please choose an option from the menu.')

        if user_input == 'a':
            temp_item = {}
            while True:
                try:
                    temp_name = input('Enter item\'s name: ')

                    if len(temp_name) == 0:
                        raise Exception
                    temp_item['Name'] = temp_name
                    break
                except Exception:
                    print('Enter something.')

            while True:
                try:
                    temp_quantity = int(input('How many: ').strip())

                    if temp_quantity <= 0:
                        raise ValueError
                    temp_item['Quantity'] = temp_quantity
                    break
                except ValueError:
                    print('Enter a number greater than zero.')

            while True:
                try:
                    temp_cost = int(input('How much does it cost: ').strip())

                    if temp_cost <= 0:
                        raise ValueError
                    temp_item['Cost'] = temp_cost
                    break
                except ValueError:
                    print('Enter a number greater than zero')

            while True:
                try:
                    temp_description = input('Enter description: ')

                    if len(temp_description) == 0:
                        raise Exception
                    temp_item['Description'] = temp_description
                    break
                except Exception:
                    print('Enter something.')

            ShoppingCart.add_item(temp_item)

        elif user_input == 'r':
            temp_input = input('Enter name of item to remove: ')

            ShoppingCart.remove_item(temp_input)

        elif user_input == 'c':
            temp_item = {}
            while True:
                try:
                    temp_name = input('Enter name of item you wish to modify: ')

                    if len(temp_name) == 0:
                        raise Exception
                    temp_item['Name'] = temp_name
                    break
                except Exception:
                    print('Enter something.')

            while True:
                try:
                    temp_quantity = int(input('Enter item quantity: ').strip())

                    if temp_quantity <= 0:
                        raise ValueError
                    temp_item['Quantity'] = temp_quantity
                    break
                except ValueError:
                    print('Please enter a number greater than zero.')

            while True:
                try:
                    temp_cost = int(input('Enter cost of the item: ').strip())

                    if temp_cost <= 0:
                        raise ValueError
                    temp_item['Cost'] = temp_cost
                    break
                except ValueError:
                    print('Please enter a number greater than zero.')

            while True:
                try:
                    temp_description = input('Please enter a description: ')

                    if len(temp_description) == 0:
                        raise Exception
                    temp_item['Description'] = temp_description
                    break
                except Exception:
                    print('Enter something.')

            ShoppingCart.modify_item(temp_item)

        elif user_input == 'i':
            ShoppingCart.print_descriptions()

        elif user_input == 'o':
            ShoppingCart.print_total()

        elif user_input == 'q':
            print('Quiting...')
            break

def main():
    cart = ShoppingCart()

    user_name = input('Enter customer\'s name: ')
    date = input('Enter today\'s date: ')

    cart.set_name(user_name)
    cart.set_date(date)

    print_menu(cart)

if __name__ == '__main__':main()