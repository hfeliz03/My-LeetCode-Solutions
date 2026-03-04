from collections import deque
class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows.get(userId, set())
        res = []
        for tweetId, authorId in reversed(self.tweets):
            if authorId == userId or authorId in followees:
                res.append(tweetId)
            if len(res) == 10: break
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)