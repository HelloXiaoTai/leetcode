# -*- coding: utf-8 -*-
'''
请根据每日 气温 列表，重新生成一个列表。
对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]

'''

#暴力解答（提交未通过）
class SolutionOne(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = list()
        for out_index in range(0,len(T)-1):
            for inner_index in range (out_index+1,len(T)):
                if T[out_index]<T[inner_index]:
                    result.append(inner_index-out_index)
                    break
            else:
                result.append(0)
        result.append(0)
        return result

#来源：https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
#栈
class SolutionTwo:
    def dailyTemperatures(self, T) :
        length = len(T)
        ans = [0] * length
        stack = [] #放下标
        for index,temperature in range(length):
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = index - prev_index
            stack.append(index)
        return ans



if __name__ == '__main__':
    result=SolutionOne().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(result)