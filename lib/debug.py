#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    
    coffee1 = Coffee("Coffee1")
    coffee2 = Coffee("Coffee2")
    coffee3 = Coffee("Coffee3")
    coffee4 = Coffee("Coffee4")
    coffee5 = Coffee("Coffee5")
    coffee6 = Coffee("Coffee6")
    coffee7 = Coffee("Coffee7")
    coffee8 = Coffee("Coffee8")
    coffee9 = Coffee("Coffee9")
    coffee10 = Coffee("Coffee10")


    customer1 = Customer("Customer1")
    customer2 = Customer("Customer2")
    customer3 = Customer("Customer3")
    customer4 = Customer("Customer4")
    customer5 = Customer("Customer5")
    customer6 = Customer("Customer6")
    customer7 = Customer("Customer7")
    customer8 = Customer("Customer8")
    customer9 = Customer("Customer9")
    customer10 = Customer("Customer10")

    order1 = Order(customer1, coffee1, 5.00)
    order2 = Order(customer2, coffee2, 5.50)
    order3 = Order(customer3, coffee3, 6.00)
    order4 = Order(customer4, coffee4, 6.50)
    order5 = Order(customer5, coffee5, 7.00)
    order6 = Order(customer6, coffee6, 7.50)
    order7 = Order(customer7, coffee7, 8.00)
    order8 = Order(customer8, coffee8, 8.50)
    order9 = Order(customer9, coffee9, 9.00)
    order10 = Order(customer10, coffee10, 9.50)
    order11 = Order(customer1, coffee2, 5.75)
    order12 = Order(customer2, coffee3, 6.25)
    order13 = Order(customer3, coffee4, 6.75)
    order14 = Order(customer4, coffee5, 7.25)
    order15 = Order(customer5, coffee6, 7.75)
    order16 = Order(customer6, coffee7, 8.25)
    order17 = Order(customer7, coffee8, 8.75)
    order18 = Order(customer8, coffee9, 9.25)
    order19 = Order(customer9, coffee10, 9.75)
    order20 = Order(customer10, coffee1, 5.50)
    
    

    ipdb.set_trace()
