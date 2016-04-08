#!/usr/bin/env python

import not_real

def main():
    running = True
    while running:
        customer_info = dict()

        print "Get a customer's scoring"
        print "Leave blank if unknown"

        raw_income = raw_input("Enter the customer's anual income in USD: ")
        if raw_income != '':
            customer_info['income'] = raw_income 

        raw_zipcode = raw_input("And their zipcode: ")
        if raw_zipcode != '':
            customer_info['zipcode'] = raw_zipcode

        raw_age = raw_input("Finaly their age: ")
        if raw_age != '':
            customer_info['age'] = raw_age

        customer_scoring = not_real.get_customer_scoring(customer_info)
        
        print(customer_scoring)

        go_again = raw_input('Continue? (Y/N) ').lower()

        if 'y' in go_again:
            running = True
        else:
            running = False

        


main()
