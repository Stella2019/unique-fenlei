#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.子集.py
@time: 2019/8/7 11:08
"""
"""
leetcode78: 子集合
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯法, 依次求长度为i(1<=i<=n)的组合
        res = []
        self.dfs(0, [], nums, res)
        return res

    def dfs(self, start, sub, nums, res):
        if len(sub) <= len(nums):
            res.append(sub[:])

        for i in range(start, len(nums)):
            self.dfs(i + 1, sub + [nums[i]], nums, res)


# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (79.32%)
# Likes:    1043
# Dislikes: 0
# Total Accepted:    207.2K
# Total Submissions: 260.2K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#