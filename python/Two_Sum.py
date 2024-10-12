# https://leetcode.com/problems/two-sum/


# Brute Force Approach: O(n^2)
# In the brute-force method, we loop through the array twice, checking each pair of numbers to see if their sum matches the target.
# This method uses two nested loops and has a time complexity of O(n^2).

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# Better idea
# Hash map
# store the numbers we’ve already seen along with their indices.
# This allows us to check in constant time whether the required complement (target minus the current number) has already been seen.

def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

print(two_sum([2, 7, 11, 15], 9))
