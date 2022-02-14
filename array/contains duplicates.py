# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:25:42 2022

@author: APARNA
"""


def main():
    nums = [1,2,3,8]
    hm = {}
    for i in nums:
        if i in hm:
            return True
        else:
            hm[i] = 1
    return False

if __name__ == '__main__':
    print(main())