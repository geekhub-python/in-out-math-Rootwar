#!/usr/bin/env python3

import math

class1 = int(input('Quantity children in class one: '))
class2 = int(input('Quantity children in class two: '))
class3 = int(input('Quantity children in class three: '))

quantity_desks = (class1 + class2 + class3) / 2

print('Need desks: ', math.ceil(quantity_desks))
