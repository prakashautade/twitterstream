from tweepy import OAuthHandler

class AuthProvider:
    def getAuth(self, key, secrete, token, token_secrete):
        twitterAuth = OAuthHandler(key, secrete)
        twitterAuth.set_access_token(token, token_secrete)
        return twitterAuth
