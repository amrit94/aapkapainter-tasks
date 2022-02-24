"""
Write a code that prints out the first occurrence of a duplicate in a given array of integers
    Sample Input: [1,2,3,2,1]
    Output: 2
"""

def get_first_occurrence(nlist):
    mlist = []
    for i in nlist:
        if i not in mlist:
            mlist.append(i)
        else:
            return i

input_list = [1,2,1 ,3,2,1]
print(get_first_occurrence(input_list))

