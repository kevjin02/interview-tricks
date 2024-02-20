"""
You are given an array of strings, count the number of times a search string occurs in the array.

in: dog cat dog cat
out: cat

Output: 2

in: dog cat cart cat cat vanderbilt dog cat cat four score and seven years ago
out: cat

Output: 5

"""

def count_occurences(inputt1: list(str), searchword: str) -> int:
    count = 0
    for word in inputt1:
        if word == searchword:
            count += 1
    return count
