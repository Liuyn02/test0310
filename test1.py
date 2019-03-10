#!/bin/env python
#-*- coding:utf-8 -*-
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''



class Solution:
    def reverse(self, x):
        nums = []
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        x = str(x)
        for i in x:
            nums.append(i)
        re = ''
        nums.reverse()
        for j in nums:
            re += j
            if int(re)>2**32-1 or int(re)<-2**31:
                return 0
        if flag == 1:
            return -int(re)
        else:
            return int(re)


if __name__ == '__main__':

    instance = Solution()
    re = instance.reverse(1563847412345)
    print(re)