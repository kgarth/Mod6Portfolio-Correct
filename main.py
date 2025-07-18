from shoppingcart import ShoppingCart

def print_menu(ShoppingCart):
    user_input = ''

    # Displays menu and handles user inputs
    while user_input != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' description')
        print('o - Output shopping cart')
        print('q - Quit')

        # Loops until proper input received
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

        # Branch for option 'a'
        if user_input == 'a':
            temp_item = {} # create temporary dictionary to pass into method
            
            while True: # Loop until proper input received
                try:
                    temp_name = input('Enter item\'s name: ')

                    if len(temp_name) == 0:
                        raise Exception
                    temp_item['Name'] = temp_name
                    break
                except Exception:
                    print('Enter something.')

            while True: # Loop until proper input received
                try:
                    temp_quantity = int(input('How many: ').strip())

                    if temp_quantity <= 0:
                        raise ValueError
                    temp_item['Quantity'] = temp_quantity
                    break
                except ValueError:
                    print('Enter a number greater than zero.')

            while True: # Loop until proper input received
                try:
                    temp_cost = int(input('How much does it cost: ').strip())

                    if temp_cost <= 0:
                        raise ValueError
                    temp_item['Cost'] = temp_cost
                    break
                except ValueError:
                    print('Enter a number greater than zero')

            while True: # Loop until proper input received
                try:
                    temp_description = input('Enter description: ')

                    if len(temp_description) == 0:
                        raise Exception
                    temp_item['Description'] = temp_description
                    break
                except Exception:
                    print('Enter something.')

            ShoppingCart.add_item(temp_item) # pass temporary dictionary into method

        # Branch option for 'r'
        elif user_input == 'r':
            temp_input = input('Enter name of item to remove: ')

            # Passes temp_input into class method
            ShoppingCart.remove_item(temp_input)

        # Branch option for 'c'
        elif user_input == 'c':
            temp_item = {} # create temporary dictionary to pass into method
            
            while True: # Loop until proper input received
                try:
                    temp_name = input('Enter name of item you wish to modify: ')

                    if len(temp_name) == 0:
                        raise Exception
                    temp_item['Name'] = temp_name
                    break
                except Exception:
                    print('Enter something.')

            while True: # Loop until proper input received
                try:
                    temp_quantity = int(input('Enter item quantity: ').strip())

                    if temp_quantity <= 0:
                        raise ValueError
                    temp_item['Quantity'] = temp_quantity
                    break
                except ValueError:
                    print('Please enter a number greater than zero.')

            while True: # Loop until proper input received
                try:
                    temp_cost = int(input('Enter cost of the item: ').strip())

                    if temp_cost <= 0:
                        raise ValueError
                    temp_item['Cost'] = temp_cost
                    break
                except ValueError:
                    print('Please enter a number greater than zero.')

            while True: # Loop until proper input received
                try:
                    temp_description = input('Please enter a description: ')

                    if len(temp_description) == 0:
                        raise Exception
                    temp_item['Description'] = temp_description
                    break
                except Exception:
                    print('Enter something.')

            ShoppingCart.modify_item(temp_item) # Pass temp dictionary into class method

        # Branch option for 'i'
        elif user_input == 'i':
            ShoppingCart.print_descriptions() # Call class method

        # Branch option for 'o'
        elif user_input == 'o':
            ShoppingCart.print_total() # Call class method

        elif user_input == 'q':
            print('Quiting...')
            break

def main():
    cart = ShoppingCart() # Create default object

    # Collect name and date
    user_name = input('Enter customer\'s name: ')
    date = input('Enter today\'s date: ')

    # Set cart attributes
    cart.set_name(user_name)
    cart.set_date(date)

    print_menu(cart) # Call method

if __name__ == '__main__':main()