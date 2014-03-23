"""
Scoring mechanism borrowed from here:   http://sentiwordnet.isti.cnr.it/code/SentiWordNetDemoCode.java
"""
import argparse
from collections import defaultdict
import json

DEBUG=False

def _sentiwordnet_rank_score_dict(f):
    """
    creates dictionary from sentiwordnet file

    args:
    f file handle of sentiwordnet file

    returns:
    dictionary with scores 

    """

    #initialize a temporary dictionary for storing ranks and scores for each term
    rank_score_dict = defaultdict(dict)
    
    if DEBUG:
        cnt = 0
    for line in f:

        if DEBUG:
            print "read: %s"%line
            cnt += 1
            if cnt==50:
                break

        line = line.strip()

        #ignore commented lines
        if line[0] == '#':
            continue

        values = line.split('\t')

        if(len(values)!=6):
            print "No of elements are not equal to 6"
            return 

        pos_tag = values[0]

        #synset score: pos - neg
        score = float(values[2]) - float(values[3])
       
        #read all the terms 
        terms = values[4].split(' ')

        if DEBUG:
            print "terms: ",terms

        for term in terms:
            rank = int(term.split('#')[1])
            term = term.split('#')[0] + "#" + pos_tag
            rank_score_dict[term][rank] = score 
       
    return rank_score_dict

def get_sentiwordnet_dict(filename):
    """
    creates dictionary from sentiwordnet file

    args:
    filename filename with full path of sentiwordnet file

    return:
    dictionary with words and their scores
    """
    with open(filename) as f:
        rank_score_dict = _sentiwordnet_rank_score_dict(f)

    if rank_score_dict:
        weigthed_score_dict = {}

        for word, rank_score in rank_score_dict.iteritems():
            
            #calculate the weighted average.
            # weigh the terms according to their ranks
            sum_rank = 0.0
            weigthed_score = 0.0

            for rank,score in rank_score.iteritems():
                weigthed_score += score/rank
                sum_rank += 1.0/rank

            weigthed_score = weigthed_score/sum_rank
            weigthed_score_dict[word] = weigthed_score

        return weigthed_score_dict

    print "ERROR!!"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',help='Enter the files name that contains tweets')
    args = parser.parse_args()
    filename = args.filename
    print 'filename: %s'%filename
    word_scores = get_sentiwordnet_dict(filename)

    with open("senti_word_scores.json","wb") as fw:
        json.dump(word_scores,fw, indent=True)


if __name__ == "__main__":
    main()
