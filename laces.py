#!/usr/bin/env python3

len_between_rows = int(input())
len_between_tears = int(input())
quantity_tears = int(input())
free_length = int(input())

a = len_between_rows + len_between_tears
b = (quantity_tears * a) + free_length
b = b * 2

print(b)