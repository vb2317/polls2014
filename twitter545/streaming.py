from slistener import SListener
import time, tweepy, sys
import json

## authentication
with open('tweet-auth.json') as f:
    auth_dict = json.load(f)

auth_dict_ascii = dict()
for k,v in auth_dict.iteritems():
    auth_dict_ascii[k.encode('utf-8')] = v.encode('utf-8')
    
auth     = tweepy.OAuthHandler(auth_dict['consumer_key'],auth_dict['consumer_secret'])
auth.set_access_token(auth_dict['auth_key'],auth_dict['auth_secret'])
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
