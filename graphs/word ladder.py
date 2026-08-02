class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                nw=word[:i]+"*"+word[i+1:]
                nei[nw].append(word)
        queue=deque([beginWord])
        visited=set([beginWord])
        res=1
        while queue:
            for _ in range(len(queue)):
                word=queue.popleft()
                if word==endWord:
                    return res
                for i in range(len(word)):
                    nw=word[:i]+"*"+word[i+1:]
                    for neighbor in nei[nw]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            res+=1
        return 0
