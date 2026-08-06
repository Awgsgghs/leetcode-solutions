class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        currtank = 0
        start_idx = 0
        for i in range(len(gas)):
            currtank += gas[i] - cost[i]
            if currtank < 0:
                start_idx = i + 1
                currtank = 0
        return start_idx
