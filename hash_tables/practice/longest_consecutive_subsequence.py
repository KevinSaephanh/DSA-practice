# Given an unsorted array of integers, write a function that finds the length of the longest_consecutive_sequence
# (i.e., sequence of integers in which each element is one greater than the previous element).
#
# Example:
#   Input: nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
#   Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 1
    for num in nums:
        # If num - 1 is not in the set, we'll assume it's the lowest num of a sequence
        if num - 1 not in num_set:
            curr_num = num
            curr_seq = 1

            # Begin counting the incrementing sequence (if exists)
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_seq += 1
            # Once counting is done, determine nwew longest consecutive sequence
            longest = max(longest, curr_seq)
    return longest


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
