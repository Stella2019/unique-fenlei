#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.加油站问题.py
@time: 2019/8/21 10:24
"""
"""
leetcode134: 加油站问题
思路：贪心
参考：https://leetcode-cn.com/problems/gas-station/submissions/
"""

# [134] 加油站
#
# https://leetcode-cn.com/problems/gas-station/description/
#
# algorithms
# Medium (56.82%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    90.8K
# Total Submissions: 159.3K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明: 
#
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
#
#
# 示例 1:
#
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# 输出: 3
#
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
# 输入:
# gas  = [2,3,4]
# cost = [3,4,3]
#
# 输出: -1
#
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 思路：贪心，累加在每个位置的left += gas[i] - cost[i], 就是在每个位置剩余的油量,
        # 如果left一直大于0, 就可以一直走下取. 如果left小于0了, 那么就从下一个位置重新开始计数,
        # 并且将之前欠下的多少记录下来, 如果最终遍历完数组剩下的燃料足以弥补之前不够的,
        # 那么就可以到达, 并返回最后一次开始的位置.否则就返回-1。
        # 时间复杂度为O(n)
        start, left, lack = 0, 0, 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if left < 0:
                lack += left
                start = i + 1
                left = 0
        if left + lack >= 0:
            return start
        else:
            return -1


class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        res, all_sum, min_sum = -1, 0, float('inf')
        n = len(gas)
        for i in range(n):
            all_sum += gas[i] - cost[i]
            if min_sum > all_sum:
                min_sum = all_sum
                res = (i + 1) % n

        if all_sum < 0:
            return -1

        return res




class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        totalgas = 0
        totalcost = 0
        start = 0
        balance = 0
        for i in xrange(0, len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]

        for i in range(0, len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0

        if totalcost <= totalgas:
            return start
        return -1