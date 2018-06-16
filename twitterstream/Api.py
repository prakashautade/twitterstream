from twitterstream.auth.AuthProvider import AuthProvider
from twitterstream.stream.StreamConsumer import StreamConsumer
from tweepy import Stream

class Api():
    def setTwitterAuthParams(self, key='', secrete='', token='', token_secrete=''):
        self.key = key
        self.secrete = secrete
        self.token = token
        self.token_secrete = token_secrete

    def setStreamParams(self, twitsRequested = 10, streamLocation = 'stream.json'):
        self.twitsRequested = twitsRequested
        self.streamLocation = streamLocation

    def consumeTwitterStream(self, track = []):
        authProvider = AuthProvider()
        twitterAuth = authProvider.getAuth(self.key, self.secrete, self.token, self.token_secrete)
        streamConsumer = StreamConsumer(self.twitsRequested, self.streamLocation)
        twitterStream = Stream(twitterAuth, streamConsumer)
        twitterStream.filter(track=track)
