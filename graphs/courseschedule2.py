class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp={}
        for nums in prerequisites:
            if nums[1] not in mp:
                mp[nums[1]]=[]
            mp[nums[1]].append(nums[0])
        visited=[0]*numCourses
        res=[]
        def dfs(i):
            if visited[i]==1:
                return False
            if visited[i]==2:
                return True
            visited[i]=1
            if i in mp:
                for neighbor in mp[i]:
                    if not dfs(neighbor):
                        return False
            visited[i]=2
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
