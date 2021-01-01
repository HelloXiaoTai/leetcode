# -*- coding: utf-8 -*-
'''
题目：两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

#1、暴力枚举,两层循环
class SolutionOne(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_1 in range(len(nums)):
            for index_2 in range(index_1+1,len(nums)):
                if nums[index_1]+nums[index_2]==target:
                    return [index_1,index_2]
        return []


#2、巧用字典提高速度
#refer:https://leetcode-cn.com/problems/two-sum/solution/tu-jie-ha-xi-biao-by-ml-zimingmeng/%EF%BC%89%EF%BC%8C%E6%8A%8A%E5%8E%9F%E5%85%88%E7%9A%84%E6%95%B0%E7%BB%84%E8%BD%AC%E5%8C%96%E6%88%90%E5%AD%97%E5%85%B8%EF%BC%8C%E9%80%9A%E8%BF%87%E5%AD%97%E5%85%B8%E5%8E%BB%E6%9F%A5%E8%AF%A2%E9%80%9F%E5%BA%A6%E5%B0%B1%E4%BC%9A%E5%BF%AB%E5%BE%88%E5%A4%9A%E3%80%82%E4%B8%8B%E9%9D%A2%E7%9A%84%E4%BB%A3%E7%A0%81%E6%88%91%E5%8F%98%E6%9B%B4%E4%BA%86%E9%A1%BA%E5%BA%8F%EF%BC%8C%E5%A5%BD%E7%90%86%E8%A7%A3%E5%A4%9A%E4%BA%86%EF%BC%8C%E9%80%9F%E5%BA%A6%E4%B9%9F%E5%BF%AB%E4%BA%86%E4%B8%80%E4%BA%9B%E3%80%82/
#哈希表:根据关键码值(Key value)而直接进行访问的数据结构
class SolutionTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num],index]
            else:
                hashmap[num] = index
