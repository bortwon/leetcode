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



# 27. Remove Element
# Easy

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order
# of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the
# duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave
# beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.


# Example 1:
#
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i



# 1108. Defanging an IP Address
# Easy

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for i in address:
            if i == '.':
                res += '[.]'
            else:
                res += i
        return res



# 1920. Build Array from Permutation
# Easy

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]]
# for each 0 <= i < nums.length and return it.
#
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
#
# Example 1:
#
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]

# Example 2:
#
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans



# 1929. Concatenation of Array
# Easy

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]


# First solution:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums



# 2469. Convert the Temperature
# Easy

# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the
# temperature in Celsius.
#
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
#
# Return the array ans. Answers within 10-5 of the actual answer will be accepted.
#
# Note that:
#
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00
#
# Example 1:
#
# Input: celsius = 36.50
# Output: [309.65000,97.70000]
# Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

# Example 2:
#
# Input: celsius = 122.11
# Output: [395.26000,251.79800]
# Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.


# 1
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        res.append(celsius + 273.15)
        res.append(celsius * 1.80 + 32.00)
        return res

# 2
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[]
        kelvin=celsius+273.15
        fahrenheit=celsius * 1.80 + 32.00
        temp.append(kelvin)
        temp.append(fahrenheit)
        return temp



# 2011. Final Value of Variable After Performing Operations
# Easy

# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return the final value of X after performing
# all the operations.

# Example 1:
#
# Input: operations = ["--X","X++","X++"]
# Output: 1

# Example 2:
#
# Input: operations = ["++X","++X","X++"]
# Output: 3


# 1
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = ''.join(operations)
        res = s.count('++') - s.count('--')
        return res


# 2
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in operations:
            if '+' in i:
                res += 1
            elif '-' in i:
                res -= 1
        return res



#