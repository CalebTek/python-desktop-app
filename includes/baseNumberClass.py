# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:25:13 2020

@author: LFC SOKOTO STUDIO
"""


class BaseNumber:
    def __init__(self,number, newBase):
        self.number = number
        self.newBase = newBase
    
    def base10ToLowerBase(self):
        base_10_newBase = ""
        number = self.number
        while number >0:
            number, remainder = divmod(number,self.newBase)
            base_10_newBase = base_10_newBase + str(remainder)
        base_10_newBase = base_10_newBase[: : -1]
        return(base_10_newBase)
    
    def base10ToUpperBase(self):
        number = self.number
        from string import ascii_uppercase
        base_newBase = list(ascii_uppercase)[:self.newBase]
        base_10_newBase = ""
        dict_newBase = {base_newBase.index(i):i for i in base_newBase}
        while number >0:
            number, remainder = divmod(number,self.newBase)
            base_10_newBase = base_10_newBase + dict_newBase[remainder]
        base_10_newBase = base_10_newBase[: : -1]
        return(base_10_newBase)