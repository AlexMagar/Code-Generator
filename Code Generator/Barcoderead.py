
"""
https://www.youtube.com/watch?v=i1sXTNpJuyc

"""

from barcode import EAN13
import random 

number [7]= int
number[] = '121212122121223, 121214522121223, 121212122561223, 121278122121223, 121902122121223'
for x in range(number):
    my_code = EAN13(number[x])

fn = my_code.save('btr')
