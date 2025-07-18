class ShoppingCart():
    # Set class attributes
    customer_name = ''
    current_date = ''
    cart_items = []

    # Default constructor
    def __init__(self, name = 'none', date = 'January 1, 2020'):
        self.customer_name = name
        self.current_date = date

    # Name setter
    def set_name(self, name):
        self.customer_name = name

    # Date setter
    def set_date(self, date):
        self.current_date = date

    # List of class methods
    def add_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item['Name'].lower() == ItemToPurchase['Name'].lower():
                print('Item already in cart')
        else:
            self.cart_items.append(ItemToPurchase)

    def remove_item(self, ItemToRemove):
        for pos, item in enumerate(self.cart_items):
            if item['Name'].lower() == ItemToRemove.lower():
                del self.cart_items[pos]
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        for pos, item in enumerate(self.cart_items):
            if item['Name'].lower() == ItemToPurchase['Name'].lower():
                if item['Quantity'] != ItemToPurchase['Quantity']:
                    self.cart_items[pos]['Quantity'] = ItemToPurchase['Quantity']
                if item['Cost'] != ItemToPurchase['Cost']:
                    self.cart_items[pos]['Cost'] = ItemToPurchase['Cost']
                if item['Description'].lower() != ItemToPurchase['Description'].lower():
                    self.cart_items[pos]['Description'] = ItemToPurchase['Description']
                break
        else:
            print('Item not found in cart. Nothing modified')

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += (item['Cost'] * item['Quantity'])
        return total

    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMTPY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}'.format(self.get_num_items_in_cart()))
            
            for item in self.cart_items:
                print('{} {} @ ${} = ${}'.format(item['Name'], item['Quantity'],
                                                 item['Cost'], (item['Cost'] * 
                                                                item['Quantity'])))

            print('Total: ${}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMTPY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Item Descriptions')

            for item in self.cart_items:
                print('{}: {}'.format(item['Name'], item['Description']))

