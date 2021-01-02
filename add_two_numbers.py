# -*- coding: utf-8 -*-
'''
题目描述：给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
'''
链表知识：
链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的。
链表由一系列结点（链表中每一个元素称为结点）组成，结点可以在运行时动态生成。
每个结点包括两个部分：一个是存储数据元素的数据域，另一个是存储下一个结点地址的指针域。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#refer:https://leetcode-cn.com/problems/add-two-numbers/solution/zui-zhi-bai-de-xie-fa-by-meng-zhi-hen-n-2/
class SolutionOne:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(None)
        s = 0               # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
            p = p.next                      # p 向后遍历
            s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点


#refer:https://leetcode-cn.com/problems/add-two-numbers/solution/cjie-ti-de-wan-zheng-dai-ma-bao-gua-sheng-cheng-ce/
class SolutionTwo:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next

def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


if __name__ == "__main__":
    l1 = generateList([1, 9, 3])
    l2 = generateList([9, 0, 8, 9])
    printList(l1)
    printList(l2)
    s = SolutionTwo()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
