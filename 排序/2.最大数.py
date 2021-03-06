#!/usr/bin/python
# coding:utf-8
#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (37.50%)
# Likes:    483
# Dislikes: 0
# Total Accepted:    54.3K
# Total Submissions: 142.8K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
# 示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出："1"
#
#
# 示例 4：
#
#
# 输入：nums = [10]
# 输出："10"
#
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.最大数.py
@time: 2019/8/10 16:54
"""
"""
leetcode179: 最大数
思路：使用排序思想，注意交换条件
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 排序思想，对于每一对数字ab，交换ab的条件就是ab <= ba.
        # 利用归并排序的思想，时间复杂度为o(nlogn)
        self.mergesort(nums)
        if nums[0] == 0:
            return "0"
        else:
            return "".join([str(e) for e in nums])

    def mergesort(self, nums):
        if len(nums) > 1:
            mid = (0 + len(nums)) // 2

            left = nums[:mid]
            right = nums[mid:]

            self.mergesort(left)
            self.mergesort(right)

            # 合并左右两个部分
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if int(str(left[i]) + str(right[j])) <= int(str(right[j]) + str(left[i])):
                    nums[k] = right[j]
                    k += 1
                    j += 1
                else:
                    nums[k] = left[i]
                    k += 1
                    i += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

solution = Solution()
nums = [3, 30, 34, 5, 9]
res = solution.largestNumber(nums)
print(res)
