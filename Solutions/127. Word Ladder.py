'''
127. Word Ladder
Hard
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
 
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def areWordsAdjacent(word1, word2):
            if len(word1) != len(word2):
                return False
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if count == 1:
                        return False
                    count += 1
            return True

        adj = defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if areWordsAdjacent(wordList[i], wordList[j]):
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])
        q = deque([beginWord])
        visited = set()
        count = 0
        while q:
            s = len(q)
            count += 1
            while s > 0:
                top = q.popleft()
                if top == endWord:
                    return count
                visited.add(top)
                for n in adj[top]:
                    if n not in visited:
                        q.append(n)
                s -= 1
        return 0
