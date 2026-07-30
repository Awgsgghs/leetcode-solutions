class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        mp={}
        for i in range(len(tasks)):
            mp[tasks[i]]=mp.get(tasks[i],0)+1
        for i in mp.keys():
            heapq.heappush(heap,-mp[i])
        time=0
        while heapq:
            remain=[]
            cycle=n+1
            while cycle and len(heap)!=0:
                maxfreq=heapq.heappop(heap)
                if maxfreq<-1:
                    remain.append(maxfreq+1)
                time+=1
                cycle-=1
            for num in remain:
                heapq.heappush(heap,num)
            if len(heap)==0:
                break
            time+=cycle
        return time