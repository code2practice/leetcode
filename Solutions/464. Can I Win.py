'''
464. Can I Win
Medium
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.
 
Example 1:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:
Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:
Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
 
Constraints:
1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
'''

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        seen = {}
        @cache
        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True
            # we haven't won yet.. it's the next player's turn.
            for index in range(len(choices)):
                if not can_win(choices[:index] + choices[index + 1:], remainder - choices[index]):
                    return True
            # uh-oh if we got here then next player won all permutations, we can't force their hand
            # actually, they were able to force our hand :(
            return False
        # let's do some quick checks before we journey through the tree of permutations
        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False
        # if the sum matches desiredTotal exactly then you win if there's an odd number of turns
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2 == 1
        # slow: time to go through the tree of permutations
        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(tuple(choices), desiredTotal)
