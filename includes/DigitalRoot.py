# -*- coding: utf-8 -*-

class DigitalRoot:
    def __init__(self,digits):
        self.digits = digits
        
    def splitNum(self):
        splitDigits = [int(i) for i in str(self.digits)]
        return(splitDigits)

    ## to add split
    def addSplit(self):
        splitDigits = [int(i) for i in str(self.digits)]
        s = 0
        for i in splitDigits:
            s = s + i
        return(s)
  
    # to find digital root
    def digitalRoot(self):
        digits = self.digits
        #return(digits)
        while digits >= 9:
            splitDigits = [int(i) for i in str(digits)]
            s = 0
            for j in splitDigits:
                s = s + j
            digits = s
        return(digits)
    
    # find digital root with modulo
    """ def digitalRoot2(self):
        digits = self.digits
        if (digits < 10):
            return(digits)
        else:
            sum = 0
            while (digits > 0):
                sum = sum + (digits % 10)
                digits = digits/10
                
        return(sum)
 """