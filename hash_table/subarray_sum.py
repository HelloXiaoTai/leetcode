# -*- coding: utf-8 -*-
'''
来源：
题目描述
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''


# 解法一：暴力遍历（超出时间限制）
class SolutionOne(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp == k:
                    count += 1
        return count


# 解法二（官方答案）：前缀和 + 哈希表优化
# 来源：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
# dic.get(pre, 0)--字典的get()方法：返回指定键的值，不存在时返回默认指定值
class SolutionTwo(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre = 0
        dic = {0: 1}
        count = 0
        for i in nums:
            pre += i
            if pre - k in dic:
                count += dic[pre - k]
            dic[pre] = dic.get(pre, 0) + 1
        return count


if __name__ == '__main__':
    result = SolutionOne().subarraySum([1, -1, 0], 0)
    print(result)
