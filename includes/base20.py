# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:50:08 2020

@author: LFC SOKOTO STUDIO
"""


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