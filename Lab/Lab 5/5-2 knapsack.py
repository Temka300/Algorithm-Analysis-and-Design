import unittest
import os

def knapsack(W, weights, values, n):
    # Initialize a 2D array for DP, where dp[i][w] represents the max value
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:  # Can we include this item?
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:  # We cannot include the item, so just carry forward the previous value
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

# # Example items
# values = [60, 100, 120]  # Prices (value) of the items
# weights = [10, 20, 30]  # Weights of the items
# W = 50  # Maximum weight capacity
# n = len(values)  # Number of items
# # n = len(values)  # Number of items

# # Run the knapsack function
# result = knapsack(W, weights, values, n)
# print(f"Maximum value in the knapsack: {result}")


class TestInsertionSort(unittest.TestCase):

    def test(self):
        with open("Algorithm\\LAB\\5-2.txt", 'r') as f:
            line = f.readline().strip()
            W, weights, values, n, output = eval(line)
            W = int(W)
            weights = list(map(int, weights))
            values = list(map(int, values))
            n = int(n)
            output = int(output)
        self.assertEqual(knapsack(W, weights, values, n), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)