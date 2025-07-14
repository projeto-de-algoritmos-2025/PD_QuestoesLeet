from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        return dp[rows - 1][cols - 1]
        