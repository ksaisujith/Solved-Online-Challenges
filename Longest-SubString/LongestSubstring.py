__author__ = " Sai Sujith K"

'''
Given a string, program prints the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
'''


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lengths = [0]
    for index in range(len(s)):
        string = s[index]
        for nextindex in range (index+1,len(s)):
            if s[nextindex] not in string:
                string = string + s[nextindex]
            else:
                break
        lengths.append(len(string))
    return max(lengths)


print(lengthOfLongestSubstring("jlygy"))