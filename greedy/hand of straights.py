class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            if count[key]>0:
                need=count[key]
                for i in range(groupSize):
                    card=key+i
                    if count[card]<need:
                        return False
                    count[card]-=need
        return True
