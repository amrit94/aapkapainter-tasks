"""
Write a code that checks if two given strings are anagrams
    Sample Input: Mary Army
    Output: Yes
"""
def check_anagrams(str1, str2):
    if len(str1) == len(str2) and sorted(str1.lower()) == sorted(str2.lower()):
        return "Yes"
    return "No"

input_str = "Mary Army"
s1, s2 = input_str.split()
print(check_anagrams(s1, s2))
