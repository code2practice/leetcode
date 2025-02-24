'''
1328. Break a Palindrome
Medium
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.
Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
 
Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 
Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
'''

'''
We need to replace one symbol and to get the smallest string as possible. First, we try to change elements on the smaller positions: imagine we have string xyzyx - where x, y, z can be any symbols. If x is not equal to "a", then if we replace this symbol with "a" we will break palindrome and it will be as small as possible. However if x = "a", it is not optimal to replace it to say "b", we can only make our string bigger. So, we move to the next element y and so on. Notice that we can not change z in this case, because we will not break palindrome property.
What happens, if we reached the last element and were not able to apply strategy above? Then we have string like this aaaaaa..aaaaaa or aaaaaa...z...aaaaaa, where z can be any symbol. In this case to get the smalles string as possible we need to replace last symbol to "b". Also there is case when n = 1, and we can not break palindrome property so we return "".
Complexity
It is O(n) for time and for space.
'''

class Solution:
    def breakPalindrome(self, pal):
        n = len(pal)
        for i in range(n // 2):
            if pal[i] != "a":
                return pal[:i] + "a" + pal[i + 1 :]
        return pal[:-1] + "b" if n > 1 else ""
