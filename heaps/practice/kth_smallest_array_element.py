# You are given a list of numbers called nums and a number k.
# Your task is to write a function find_kth_smallest(nums, k) to find the kth smallest number in the list.
# The list can contain duplicate numbers and k is guaranteed to be within the range of the length of the list.
# This function will take the following parameters:
#   nums: A list of integers.
#   k: An integer.
#
# Example:
#   nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
#   k = 4
#   The 4th smallest num is 3


from heaps.implementation import MaxHeap


def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        # Logic: keep inserting num into heap.
        # Every time heap length > k, remove the max num to ensure that the heap length never exceeds k
        # This ensures that the heap will ALWAYS have the smallest k numbers
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
    # heap[0] will return the max num in the heap
    # Since we removed all larger nums and kept the heap length equal to k,
    # we ensure the max num is the kth smallest num in the original heap
    return max_heap.heap[0]


nums = [6, 5, 4, 3, 2, 1]
k = 3
print(find_kth_smallest(nums, k))
