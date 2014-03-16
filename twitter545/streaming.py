from slistener import SListener
import time, tweepy, sys

## authentication
username = '' ## put a valid Twitter username here
password = '' ## put a valid Twitter password here
#auth     = tweepy.BasicAuthHandler(username, password)
auth     = tweepy.OAuthHandler('Otmr3TjtVKlw4X3amh3A','vD7YueYHIxCLbDqNVgqp25nfKk0iUVfWYQcODKAw')
auth.set_access_token('79137270-7uG6Prq58a0UnYVSQgCkwy9Flcxx5myDp1eFbKxnT','Tca04qVZAiYAm6aYJY1W0LfLLlFCt5zNW7WOMNd3PbVKT')
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
