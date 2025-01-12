# Given an array of strings containing only English letters, group the anagrams in an array together
#
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"] ==> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


from collections import defaultdict


def group_anagrams(words):
    my_dict = defaultdict(list)
    for word in words:
        my_dict[str(sorted(word))].append(word)
    return list(my_dict.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
