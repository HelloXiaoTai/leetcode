# -*- coding: utf-8 -*-
'''
来源：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
438. 找到字符串中所有字母异位词
题目描述
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
'''
import collections

#解法（超出了运行时间限制）
class SolutionOne(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #p_dic:记录p中元素出现的次数
        p_dic=collections.Counter(p)
        result=list()
        for index in range(len(s)-len(p)+1):
            tmp=collections.Counter(s[index:index+len(p)])
            if tmp==p_dic:
                result.append(index)
        return result



if __name__ == '__main__':
    result=SolutionOne().findAnagrams("baa","aa")
    print(result)
