# Write a function named stream_max that takes as its input a list of integers (nums).
# The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.
#
# More specifically, for each index i in the input list,
# the element at the same index in the output list should be the maximum value among the elements at indices 0 through i in the input list.
# Example:
#   If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].
#   Explanation:
#       At index 0, the maximum number seen so far is 1.
#       At index 1, the maximum number seen so far is 3.
#       At index 2, the maximum number seen so far is still 3.
#       At index 3, the maximum number seen so far is 5.
#       At index 4, the maximum number seen so far is still 5.
#       So, the output list is [1, 3, 3, 5, 5].


from heaps.implementation import MaxHeap


def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []
    for n in nums:
        max_heap.insert(n)
        # Since the heap always rearranges itself after inserting, top element will always be the largest
        max_stream.append(max_heap.heap[0])
    return max_stream


nums = [1, 3, 2, 5, 4]
print(stream_max(nums))
