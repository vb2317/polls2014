import argparse
import json
import nltk
from nltk.tokenize import word_tokenize

parser = argparse.ArgumentParser()
parser.add_argument('--filename',help='Enter the files name that contains tweets')
args = parser.parse_args()
filename = args.filename

print 'filename: %s'%filename


aap_tweets = []
cong_tweets = []
bjp_tweets = []
with open(filename) as f:
    for line in f:
        #print line
        line = line.rstrip()
        if not line:
            continue
        try:
            line_json = json.loads(line.rstrip())
        except ValueError:
            print line
            break
        tweet = [word.encode('utf-8').lower() for word in word_tokenize(line_json['text'])]

        #print 'tweet: %s'%tweet

        if 'aap' in tweet:
            aap_tweets.extend(tweet)
        if 'congress' in tweet:
            cong_tweets.extend(tweet)
        if 'bjp' in tweet:
            bjp_tweets.extend(tweet)

nltk.FreqDist(aap_tweets).tabulate()
nltk.FreqDist(cong_tweets).tabulate()
nltk.FreqDist(bjp_tweets).tabulate()

