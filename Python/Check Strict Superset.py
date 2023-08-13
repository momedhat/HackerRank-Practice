"""
(Check Strict Superset) is a problem on HackerRank that asks you to determine if a given set is a strict superset of multiple other sets. 
A set A is considered a strict superset of another set B if every element in set B is also in set A, and set A has at least one element that is not in set B.
"""

### Solution ###

setA = set(map(int, input().split()))
x= int(input())
counter = 0

for i in range(x):
    subSet = set(map(int, input().split()))
    if subSet.issubset(setA):
        counter += 1

print(True) if counter==x else print(False)
    