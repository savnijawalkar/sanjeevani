# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:20:12 2022

@author: Dell
"""

a=int(input("the number 1 is : "))
b=int(input("the number 2 is : "))

def countOne(n) :
    count=0
    while(n) :
        count +=1
        n &= (n-1)
        return count()
    
    def countflips(a,b):
        return countOne(a^b)
    print(countflips(a,b))