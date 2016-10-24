#!/usr/bin/env python3

len_between_rows = int(input('Enter length between rows: '))
len_between_tears = int(input('Enter length between tears: '))
free_length = int(input('Enter free length laces: '))
quantity_tears = int(input('Enter quantity tears: '))

len_between_tears = len_between_tears * (quantity_tears - 1) * 2
len_between_rows = ((len_between_rows * 2) * quantity_tears) - len_between_rows
length_laces = len_between_rows + len_between_tears + free_length * 2

print('Length tears: ', length_laces)