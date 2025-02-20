'''
245. Shortest Word Distance III
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.
Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.
 
Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
 
Constraints:
1 <= wordsDict.length <= 105
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
'''

'''
A condition is added here, that is, two words may be the same.
When word1 and word2 are equal, use p1 to save the result of p2, and p2 is assigned to the current position i, so that the result can be updated.
If word1 and word2 are not equal, the same logic is still valid.
'''
class Solution:
   def shortest_word_distance(self, words_dict: List[str], word1: str, word2: str) -> int:
       # Initialize the minimum distance to the length of the word list
       min_distance = len(words_dict)
    
       # If both words are the same, we need to find the shortest distance
       # between two occurrences of the same word
       if word1 == word2:
           last_occurrence_index = -1  # Initialize the index for the last occurrence of the word
           for index, word in enumerate(words_dict):
               if word == word1:
                   if last_occurrence_index != -1:
                       # Update minimum distance if the current pair is closer
                       min_distance = min(min_distance, index - last_occurrence_index)
                   # Update the last occurrence index to the current index
                   last_occurrence_index = index
       else:
           # If the words are different, find the shortest distance between word1 and word2
           index1 = index2 = -1  # Initialize the indexes for the occurrences of the words
        
           for index, word in enumerate(words_dict):
               if word == word1:
                   index1 = index  # Update index when word1 is found
               if word == word2:
                   index2 = index  # Update index when word2 is found
            
               # If both words have been found, update the minimum distance
               if index1 != -1 and index2 != -1:
                   min_distance = min(min_distance, abs(index1 - index2))
    
       # Return the minimum distance found
       return min_distance
