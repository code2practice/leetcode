'''
256. Paint House
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.
 
Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:
Input: costs = [[7,6,2]]
Output: 2
 
Constraints:
costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
Explanation of the Solution:
Initialization: Three variables a, b, and c are initialized to 0. These variables will hold the cumulative minimum costs of painting up to the current house, ending with each of the three colors respectively.


Iteration Over Houses: The code iterates over each house’s painting costs. For each house, represented by its costs [ca, cb, cc] for painting it with colors 0, 1, and 2 respectively:
The new value of a is set to the minimum of the previous values of b and c added to ca. This represents the minimum cost of painting the current house with color 0, given that the previous house was painted with color 1 or 2.
Similarly, the new value of b is set to the minimum of the previous values of a and c added to cb, representing painting the current house with color 1.
The new value of c is set to the minimum of the previous values of a and b added to cc, representing painting the current house with color 2.
Finding the Minimum Total Cost: After iterating through all the houses, the minimum of a, b, and c gives the overall minimum cost to paint all houses following the rule that no two adjacent houses are painted with the same color.
Why It Works:
This dynamic programming approach works because, at each step (for each house), it considers the minimum cost incurred so far for each color choice, ensuring that no two adjacent houses are painted the same color by switching to a different color for the current house. By cumulatively building up the solution from the base (starting with 0 cost and adding the house costs one by one), it finds the global minimum cost to paint all houses under the given constraints.
Example:
Given costs = [[17,2,17],[16,16,5],[14,3,19]], the function will calculate as follows:
After the first house, the costs are [17, 2, 17].
For the second house, it calculates the new costs as [18 (2+16), 5 (2+3), 7 (2+5)].
For the third house, the costs are updated to [19, 10, 14].
The minimum cost to paint all houses will be min(19, 10, 14) = 10.
'''

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Initialize the minimum costs for the three colors
        cost_red = cost_blue = cost_green = 0

        # Iterate over each house and calculate the minimum cost
        # of painting each house, not repeating the color of the adjacent house
        for cost_of_red, cost_of_blue, cost_of_green in costs:
            # Update the cost of painting each house with red, blue, or green
            # by adding the current painting cost to the minimum cost of the
            # other two colors from the previous step
            new_cost_red = min(cost_blue, cost_green) + cost_of_red
            new_cost_blue = min(cost_red, cost_green) + cost_of_blue
            new_cost_green = min(cost_red, cost_blue) + cost_of_green

            # Update the current minimum costs for each color
            cost_red, cost_blue, cost_green = (
                new_cost_red,
                new_cost_blue,
                new_cost_green,
            )

        # Return the minimum cost among the three colors after
        # completing the calculation for all houses
        return min(cost_red, cost_blue, cost_green)
