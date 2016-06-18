"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""


class FindLCM(object):
    
    def __init__(self,num):
        self.num = num
        self.factors = []
        self.factorize()
        self.print_LCM()
        
    def factorize(self):
        for num in range(2,self.num+1):
            self._factorize(num)
    
    def _factorize(self,num):
        temp_factors = self.factors[:]
        div = 2
        while True:
            if num%div == 0:
                if div in temp_factors:
                    temp_factors.remove(div)
                else:
                    self.factors.append(div)
                if div == num:
                    return
                num = num/div
            else:
                div += 1
                
    def print_LCM(self):
        LCM = 1
        for num in self.factors:
            LCM *= num
        print(LCM)