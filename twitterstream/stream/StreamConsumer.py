from tweepy.streaming import StreamListener
import os
import errno
import json

class StreamConsumer(StreamListener):
    def __init__(self, numberOfTweetsRequested = 10, tweetsLocation = 'tweets.json'):
        self.tweetsRequested = numberOfTweetsRequested
        self.tweetsConsumed = 0
        self.tweetsLocation = tweetsLocation
        self.setupTweetLocation()
        self.tweets = []
    def on_data(self, data):
        self.tweetsConsumed = self.tweetsConsumed + 1
        if(self.tweetsConsumed <= self.tweetsRequested):
            self.tweets.append(data)
            print("Twits collected: %d" % (len(self.tweets)))
            return True
        else:
            json.dump(self.tweets, self.tweetsFile)
            self.tweetsFile.close()
            return False

    def on_error(self, status):
        print(status)

    def setupTweetLocation(self):
        dirName = os.path.dirname(self.tweetsLocation)
        if dirName and not os.path.exists(dirName):
            try:
                os.makedirs(dirName)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        self.tweetsFile = open(self.tweetsLocation,"w+")
        return self.tweetsLocation

    def getTwitsLocation(self):
        return self.tweetsLocation
