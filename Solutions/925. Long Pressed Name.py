'''
925. Long Pressed Name
Easy
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed. 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
'''

class Solution:   
   def isLongPressedName(self, name, typed):
       i = 0
       for j in range(len(typed)):
           if i < len(name) and name[i] == typed[j]:
               i += 1
           elif j == 0 or typed[j] != typed[j - 1]:
               return False
       return i == len(name)
