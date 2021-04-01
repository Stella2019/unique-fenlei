#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.有效的字母异位词.py
@time: 2019/7/23 20:33
"""
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.29%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    210.6K
# Total Submissions: 331K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
"""
leetcode242: 有效的字母异位词
思路：哈希表，维护一个26个字母出现次数的数组，然后统计s字符串中字母的出现频率，
        用t减少计数器中出现字母的计算器，最后判断计数器是否回到0.(注意counter可以使用哈希)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if counter[i] != 0:
                return False
        return True

