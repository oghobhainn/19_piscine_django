#! /usr/bin/env python3

# declaring 9 variables?

def     my_var():
    arr = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42, ), set()]
    for i in arr:
        print("{0} has a type {1}".format(i, type(i)))

if __name__=='__main__':
    my_var()
