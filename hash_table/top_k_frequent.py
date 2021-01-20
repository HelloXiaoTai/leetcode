# -*- coding: utf-8 -*-
'''
来源：https://leetcode-cn.com/problems/top-k-frequent-elements
题目描述：
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
'''
import collections
import heapq


class SolutionOne(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result=list()
        for i in collections.Counter(nums).most_common(k):
            result.append(i[0])
        return result

#使用堆（https://docs.python.org/zh-cn/3.8/library/heapq.html）
#来源：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/zui-xiao-dui-by-elevenxx/
class SolutionTwo:
    def topKFrequent(self, nums, k: int) :
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i)) #频率，元素
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans


if __name__ == '__main__':
    result=SolutionOne().topKFrequent([1,2,3,4,5,6,1,3],2)
    print(result)