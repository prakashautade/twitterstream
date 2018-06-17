#### Download
```sh
$ mkdir twitterstream
$ cd twitterstream
$ git clone https://github.com/prakashautade/twitterstream.git
```
#### Install
```sh
$ pip3 install twitterstream/dist/twitterstream-0.0.1-py3-none-any.whl
```
#### Create twitter application
```sh
- Use link https://apps.twitter.com
- Record consumer key, consumer secret, token and token_secret
```
#### Use twitterstream
```sh
from twitterstream.Api import Api
streamApi = Api()
streamApi.setTwitterAuthParams(key='consumer_key', secrete='consumer_secret', token='access_token', token_secrete='access_token_secret')
streamApi.setStreamParams(twitsRequested = 2, streamLocation = '/tmp/stream.json')
streamApi.consumeTwitterStream(track=['python'])
```