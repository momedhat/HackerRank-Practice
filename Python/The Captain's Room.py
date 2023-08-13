"""
(The Captain's Room) is a problem on HackerRank that involves finding a unique element in a list of numbers.
 The problem scenario typically goes like this:
There are n rooms in a hotel. The rooms are numbered from 1 to n and arranged in a line.
A group of n tourists arrived, where each tourist stayed in a room. The captain of the group realized that there was a mistake 
and that one room was assigned to two different tourists. 
He wants to find the room number of the captain, which is the room that was not assigned to multiple tourists.
"""

### Solution ###

x = input()
ROOM_LIST = input().split()
ROOM_SET = set(ROOM_LIST)

for ele in list(ROOM_SET):
    ROOM_LIST.remove(ele)

CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
print(CAPTAIN_ROOM_NUM)
