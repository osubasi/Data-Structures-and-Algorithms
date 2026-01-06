# Omer Subasi

import bisect 

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [(0, 0)]
    for e, s, p in jobs:
        i = bisect.bisect_right(dp, (s, float('inf'))) - 1
        cand = dp[i][1] + p
        if cand > dp[-1][1]:
            dp.append((e, cand))
    return dp[-1][1]
