from slistener import SListener
import time, tweepy, sys

## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
#auth     = tweepy.BasicAuthHandler(username, password)
auth     = tweepy.OAuthHandler('consumer_key','consumer_secret')
auth.set_access_token('auth_key','auth_secret')
api      = tweepy.API(auth)

def main():
    track = [ 'congress','bjp','aap' ]
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
