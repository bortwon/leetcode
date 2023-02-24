# 13. Roman to Integer
# Easy

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res


# 383. Ransom Note
# Easy
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for i in magazine:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for ch in ransomNote:
            if ch not in d or d[ch] == 0:
                return False
            else:
                d[ch] -= 1
        return True


# 412. Fizz Buzz
# Easy
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res



# 876. Middle of the Linked List
# Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head



# 1. Two Sum
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i



# 9. Palindrome Number
# Easy

# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]



# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        length = min(map(lambda x: len(x), strs))
        for i in range(length):
            if len(set(map(lambda x: x[i], strs))) == 1:
                res += strs[0][i]
                continue
            break
        return res



# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.

# An input string is valid if:
#
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true

# Example 2:
#
# Input: s = "()[]{}"
# Output: true

# Example 3:
#
# Input: s = "(]"
# Output: false


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0



# 26. Remove Duplicates from Sorted Array
# Easy

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first
# k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4
# respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)



# 7. Reverse Integer
# Medium

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
#
# Input: x = 123
# Output: 321

# Example 2:
#
# Input: x = -123
# Output: -321

# Example 3:
#
# Input: x = 120
# Output: 21



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ex = (-(2 ** 31), 2 ** 31 - 1)
        if x < 0:
            x = int(str(x)[1:][::-1]) * -1
            return 0 if x < ex[0] else x
        if x > 0:
            x = int(str(x)[::-1])
            return 0 if x > ex[1] else x
        return 0



#