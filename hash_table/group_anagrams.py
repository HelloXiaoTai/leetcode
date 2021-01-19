# -*- coding: utf-8 -*-
'''
来源：https://leetcode-cn.com/problems/group-anagrams
题目描述：
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
'''
import collections


class SolutionOne(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table=dict() #排序后的字符串为key,value为字母异位词列表
        for index,s in enumerate(strs):
            s=''.join(sorted(s))
            if s in hash_table.keys():
                hash_table[s].append(strs[index])
            else:
                hash_table[s]=[strs[index]]

        return list(hash_table.values())

#官方答案
#来源：https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/
#collections.defaultdict(list):将键-值对序列转换为列表字典
class SolutionTwo:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())


if __name__ == '__main__':
    result=SolutionOne().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)