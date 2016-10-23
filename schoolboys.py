#!/usr/bin/env python3

children = int(input('Quantity children: '))
apples = int(input('Quantity apples: '))

quantity_apples = apples // children
other_apples = apples % children

print('Used apples: ', quantity_apples)
print('Other apples: ', other_apples)