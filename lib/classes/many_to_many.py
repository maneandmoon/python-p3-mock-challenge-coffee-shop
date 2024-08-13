
class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_coffee):
        if not hasattr(self, 'name') and isinstance(new_coffee, str) and len(new_coffee) >= 3:
            self._name = new_coffee

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # Unique list of customers who ordered this coffee
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if not self.orders():
            return 0
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders())

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        # Unique list of coffees ordered by this customer
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee object.")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        order = Order(self, coffee, float(price))
        self.orders().append(order)
        coffee.orders().append(order)  # Append the order to the coffee's orders list
        return order

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
        # Automatically add this order to the customer and coffee's order lists
        customer.orders().append(self)
        coffee.orders().append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not hasattr(self, 'price') and isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
            self._price = new_price

        

