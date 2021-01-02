# -*- coding: utf-8 -*-
'''
给你一个字符串 s ，请你根据下面的算法重新构造字符串：
1、从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
2、从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
3、重复步骤 2 ，直到你没法从 s 中选择字符。
4、从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
5、从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
6、重复步骤 5 ，直到你没法从 s 中选择字符。
7、重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。

示例 1：

输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
'''
import collections


class Solution:
    def sortString(self, s: str) -> str:
        li = list(s)
        sort_li = list()  # 排序后的字符串列表
        temp = list()  # 重复元素
        while li:
            # 升：找出每一轮的最小值
            while li:
                min_s = min(li)
                sort_li.append(li.pop(li.index(min_s)))
                while min_s in li:
                    # 删除重复元素
                    temp.append(li.pop(li.index(min_s)))
            li = temp
            temp = []
            # 降：找出每一轮的最大值
            while li:
                max_s = max(li)
                sort_li.append(li.pop(li.index(max_s)))
                while max_s in li:
                    # 删除重复元素
                    temp.append(li.pop(li.index(max_s)))
            li = temp
            temp = []
        sort_s = ''.join(sort_li)

        return sort_s


# 改进
'''
refer:https://leetcode-cn.com/problems/increasing-decreasing-string/solution/pythonyou-ya-ti-jie-by-smilelight/
排序：调用list的sort方法，通过设置reverse参数来控制是否降序。
字符集合提取：采用collections内置库的Counter对象来操作。
Counter:字典的子类，提供了可哈希对象的计数功能

'''


class SolutionTwo:
    def sortString(self, s: str) -> str:
        str_counter = collections.Counter(s)  # Counter({'a': 3, 'b': 3, 'c': 3})
        result = []
        flag = False
        while str_counter:
            keys = list(str_counter.keys())
            keys.sort(reverse=flag)
            flag = not flag
            result.append(''.join(keys))
            str_counter -= collections.Counter(keys)
        return ''.join(result)


if __name__ == '__main__':
    results = Solution().sortString('aaaabbbbcccc')
    print(results)
