# -*- coding: utf-8 -*-
'''
https://leetcode-cn.com/problems/single-number/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：算法应该具有线性时间复杂度,不使用额外空间来实现。
示例 1:
输入: [2,2,1]
输出: 1
'''

import collections
from functools import reduce

#解法一：哈希表（使用了额外空间）
class SolutionOne(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_counter = collections.Counter(nums)
        for key,value in num_counter.items():
            if value==1:
                return key

#解法二（时间复杂度n的平方）
class SolutionTwo(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num)==1:
                return num


'''
官方答案：异或（https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/）
任何数和 0 做异或运算，结果仍然是原来的数，即a⊕0=a。
任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
'''
#reduce() 函数会对参数序列中元素进行累积。
# 先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
class SolutionThree(object):
    def singleNumber(self, nums) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    result=SolutionThree().singleNumber([1,0,1])
    print(result)