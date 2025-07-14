from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        start_times = [job[0] for job in jobs]
        n = len(jobs)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            next_index = bisect.bisect_left(start_times, jobs[i][1])

            skip = dp[i + 1]
            take = jobs[i][2] + dp[next_index]

            dp[i] = max(skip, take)

        return dp[0]
