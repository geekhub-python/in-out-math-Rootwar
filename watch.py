#!/usr/bin/env python3

current_minutes = int(input('Enter minutes: '))

hours = current_minutes % (60 * 24) // 60
minutes = current_minutes % 60

print('Time: ', hours, minutes)



