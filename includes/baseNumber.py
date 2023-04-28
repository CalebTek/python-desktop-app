# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:01:34 2020

@author: LFC SOKOTO STUDIO
"""



## function base number
'''
from string import ascii_uppercase
base_26 = list(ascii_uppercase)
base_10 = list(range(1,27))
dict_10_26 = {(base_26.index(i)+1):i for i in base_26}

base_10_26 = ""
number = 1208
number, remainder = divmod(number, 26)
base_10_26 = base_10_26 + dict_10_26[remainder]
'''

'''
count = 1
number = 348

while number//5 >5:
    s = number//5
    count +=1
    number = s
print(count)
'''


def base2(number = False):
    if number == False:
        number = eval(input("Enter the number: "))
    else:
        number = number
    base_10_2 = ""
    while number >0:
        number, remainder = divmod(number,2)
        base_10_2 = base_10_2 + str(remainder)
    base_10_2 = base_10_2[: : -1]
    return(base_10_2)

def base5(number = False):
    if number == False:
        number = eval(input("Enter the number: "))
    else:
        number = number
    base_10_5 = ""
    while number >0:
        number, remainder = divmod(number,5)
        base_10_5 = base_10_5 + str(remainder)
    base_10_5 = base_10_5[: : -1]
    return(base_10_5)

def base10ToLowerBase(number = False, newBase = False):
    if number == False and newBase == False:
        number = eval(input("Enter the number: "))
        newBase = eval(input("Enter new base number: "))
    else:
        number = number
        newBase = newBase
    base_10_newBase = ""
    while number >0:
        number, remainder = divmod(number,newBase)
        base_10_newBase = base_10_newBase + str(remainder)
    base_10_newBase = base_10_newBase[: : -1]
    return(base_10_newBase)


def base16(number = False):
    from string import ascii_uppercase
    if number == False:
        number = eval(input("Enter the number: "))
    else:
        number = number
    base_16 = list(ascii_uppercase)[:16]
    base_10_16 = ""
    dict_16 = {base_16.index(i):i for i in base_16}
    while number >0:
        number, remainder = divmod(number,16)
        base_10_16 = base_10_16 + dict_16[remainder]
    base_10_16 = base_10_16[: : -1]
    return(base_10_16)


def base20(number = False):
    from string import ascii_uppercase
    if number == False:
        number = eval(input("Enter the number: "))
    else:
        number = number
    base_20 = list(ascii_uppercase)[:20]
    base_10_20 = ""
    dict_20 = {base_20.index(i):i for i in base_20}
    while number >0:
        number, remainder = divmod(number,20)
        base_10_20 = base_10_20 + dict_20[remainder]
    base_10_20 = base_10_20[: : -1]
    return(base_10_20)

def base26(number = False):
    from string import ascii_uppercase
    if number == False:
        number = eval(input("Enter the number: "))
    else:
        number = number
    base_26 = list(ascii_uppercase)
    base_10_26 = ""
    dict_26 = {base_26.index(i):i for i in base_26}
    while number >0:
        number, remainder = divmod(number,26)
        base_10_26 = base_10_26 + dict_26[remainder]
    base_10_26 = base_10_26[: : -1]
    return(base_10_26)


def base10ToUpperBase(number = False, newBase = False):
    from string import ascii_uppercase
    if number == False and newBase == False:
        number = eval(input("Enter the number: "))
        newBase = eval(input("Enter new base number: "))
    else:
        number = number
        newBase = newBase
    base_newBase = list(ascii_uppercase)[:newBase]
    base_10_newBase = ""
    dict_newBase = {base_newBase.index(i):i for i in base_newBase}
    while number >0:
        number, remainder = divmod(number,newBase)
        base_10_newBase = base_10_newBase + dict_newBase[remainder]
    base_10_newBase = base_10_newBase[: : -1]
    return(base_10_newBase)