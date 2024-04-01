# https://leetcode.com/problems/find-the-duplicate-number/description/
# medium


# Idea: the boring approach would be scanning the array and using a set to store numbers that have been seen. 


# Interesting idea: binary search. Using binary search on an unsorted array. Why can we do this? Because we use different search condition, instead of searching some element, we count numbers that are less than the target.

class Solution:
    def findDuplicate(self, nums):
        # Initialize the search range
        left = 0
        right = len(nums) - 1
        
        # Use binary search to find the duplicate
        while left < right:
            # Find the midpoint of the current search range
            mid = left + (right - left) // 2
            
            # Count how many numbers are less than or equal to 'mid'
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # If the count is more than 'mid', then the duplicate is in the left half
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        # 'left' is the duplicate number
        return left
    
# Another interesting idea: Floyd's Tortoise and Hare (Cycle Detection). The idea is to treat the array as a linked list, where the value of the current element is the index of the next element. The duplicate number is the start of the cycle in the linked list.
    
def findDuplicate(nums):
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            return slow
