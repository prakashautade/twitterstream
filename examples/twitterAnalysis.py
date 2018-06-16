from twitterstream.Api import Api

streamApi = Api()
streamApi.setTwitterAuthParams(key='consumer_key', secrete='consumer_secret', token='access_token', token_secrete='access_token_secret')
streamApi.setStreamParams(twitsRequested = 2, streamLocation = '/tmp/stream.json')
streamApi.consumeTwitterStream(track=['python'])
