# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:10:12 2022

@author: Dell
"""

s1=int(input("the side 1 is: "))
s2=int(input("the side 2 is : "))
s3=int(input("the side 3 is : "))
if((s1+s2)>s3) :
    print("yes")
elif((s2+s3)>s1) :
    print("yes") 
elif((s1+s3)>s2) :
    print("no")
    
            
        