# Given an array of integers nums and a target integer target,
# find the indices of two numbers in the array that add up to the target using a hash table (dictionary).
#
# Example:
#   Input: nums = [5, 1, 7, 2, 9, 3], target = 10
#   Output: [1, 4]


def two_sum(nums, target):
    num_dict = dict()
    for i, num in enumerate(nums):
        if target - num in num_dict:
            # Return indices of the 2 nums that add up to the target
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
