class Twitter:

    def __init__(self):
        self.timer = 0
        self.followers = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timer, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        if userId in self.tweets:
            n = len(self.tweets[userId])
            for i in range(n - 1, max(-1, n - 11), -1):
                heapq.heappush(news, self.tweets[userId][i])
                if len(news) > 10:
                    heapq.heappop(news)
        if userId in self.followers:
            for followee in self.followers[userId]:
                if followee in self.tweets:
                    n = len(self.tweets[followee]) - 1
                    for i in range(n, max(-1, n - 11), -1):
                        heapq.heappush(news, self.tweets[followee][i])
                        if len(news) > 10:
                            heapq.heappop(news)
        res = []
        while news:
            res.append(heapq.heappop(news)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)