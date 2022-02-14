# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:08:58 2022

@author: APARNA
"""


   
    
def main():
    prices = [7,6,4,3,1]
    left, right = 0,1
    max_profit = 0
    while right< len(prices):
        if prices[left]< prices[right]:
            max_profit = max(max_profit,prices[right]-prices[left])
        else:
            left = right
        right+=1
    return max_profit
        
if __name__ == '__main__':
    print(main())