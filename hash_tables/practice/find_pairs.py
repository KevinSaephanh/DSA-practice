# You are given two lists of integers, arr1 and arr2, and a target integer value, target.
# Find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
#
# Example:
#   arr1 = [1, 2, 3]
#   arr2 = [4, 5, 6]
#   target = 9
#
#   pairs = find_pairs(arr1, arr2, target)
#   print (pairs)
#   # Expected output: [(3, 6)]
#   # Explanation: There's only one pair that adds up to 9: 3 from arr1 and 6 from arr2.


def find_pairs(arr1, arr2, target):
    my_set = set(arr1)
    pairs = []
    for num in arr2:
        if target - num in my_set:
            pairs.append((target - num, num))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)
