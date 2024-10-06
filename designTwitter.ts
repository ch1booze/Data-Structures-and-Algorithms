// LeetCode 355: Design Twitter

interface Tweet {
  userId: number;
  tweetId: number;
}

class Twittter {
  private userFollowers = new Map<number, Set<number>>();
  private tweets: Tweet[] = [];

  postTweet(userId: number, tweetId: number): void {
    this.tweets.push({ userId, tweetId });
  }

  getNewsFeed(userId: number): number[] {
    let newsFeed: number[] = [];
    const followers = this.userFollowers.get(userId) || new Set<number>();

    for (let i = this.tweets.length - 1; i >= 0; i--) {
      const tweet = this.tweets[i];
      if (followers.has(tweet.userId) || userId === tweet.userId) {
        newsFeed.push(tweet.tweetId);
      }
    }

    return newsFeed.slice(0, 10);
  }

  follow(followerId: number, followeeId: number): void {
    if (!this.userFollowers.has(followeeId)) {
      this.userFollowers.set(followeeId, new Set<number>());
    }
    this.userFollowers.get(followeeId)!.add(followerId);
  }

  unfollow(followerId: number, followeeId: number): void {
    const followers = this.userFollowers.get(followeeId);
    if (followers) {
      followers.delete(followerId);
    }
  }
}
