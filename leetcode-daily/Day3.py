"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:
Input: s = ""
Output: 0
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        mySet = set()
        best, left = 0, 0
        for right in range(n):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            best = max(best, right - left + 1)
            mySet.add(s[right])
        return best