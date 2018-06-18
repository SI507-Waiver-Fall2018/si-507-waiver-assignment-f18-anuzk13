# NAME: Ana Maria Cardenas Gasca
# ID: amcard

# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

# input
user = sys.argv[1]
t_number = int(sys.argv[2])

# tweepy auth
consumer_key = 'HnMMVjdbPJfKCZUjvXWqFOOog'
consumer_secret = 'Ap9faqkmoXhTt9j2WNACi2Wh3g4BqTRrl4Mez9cf0H1SJElsOT'
access_token = '2743887840-CQd6NVpYbnFDNIhUSnfemBhgFn8bUMpBgT4r3sN'
access_token_secret = 'fjiVs3pyNHgcr7aaYpCp7abh6xHOVTMnT4sT7IP6iz8lC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_feeds = api.user_timeline(screen_name = user, count = t_number, tweet_mode='extended', include_rts = True)

# verbs, nouns, adjectives distribution calculation
STOP_WORDS = ['http', 'https', 'RT']
VERB_TAG = 'VB'
ADJ_TAG = 'JJ'
NOUN_TAG = 'NN'

tokenized_words =  [token
                     for tweet in user_feeds
                        for token in nltk.tokenize.word_tokenize(tweet.full_text)]
tagged_words = nltk.pos_tag(tokenized_words)

verbs = []
adjectives = []
nouns = []

for tw in tagged_words:
    if (tw[0][0].isalpha() and tw[0] not in STOP_WORDS):
        # VERB, ADJ and NOUN Tags all start with the same two letters so we compare only these
        if (tw[1][:2] == VERB_TAG):
            verbs.append(tw[0])
        elif (tw[1][:2] == ADJ_TAG):
            adjectives.append(tw[0])
        elif (tw[1][:2] == NOUN_TAG):
            nouns.append(tw[0])

verbs_top_five = nltk.FreqDist(verbs).most_common(5)
adjectives_top_five = nltk.FreqDist(adjectives).most_common(5)
nouns_top_five = nltk.FreqDist(nouns).most_common(5)

#original tweets statistics
original_tweets = list(filter(lambda tweet: not tweet.retweeted, user_feeds))
favorite_count = sum(t.favorite_count for t in original_tweets)
retweet_count = sum(t.retweet_count for t in original_tweets)

# print answers
print('USER: {}'.format(user))
print('TWEETS ANALYZED: {}'.format(len(user_feeds)))
print('VERBS: ' + " ".join(['{}({})'.format(item[0],item[1]) for item in verbs_top_five]))
print('NOUNS: ' + " ".join(['{}({})'.format(item[0],item[1]) for item in adjectives_top_five]))
print('ADJECTIVES: ' + " ".join(['{}({})'.format(item[0],item[1]) for item in nouns_top_five]))
print('ORIGINAL TWEETS: {}'.format(len(original_tweets)))
print('TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}'.format(favorite_count))
print('TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}'.format(retweet_count))

# write file
file_name = "noun_data.csv"
file_content = ['Noun,Number'] + list(map(lambda n: '{},{}'.format(n[0],n[1]), nouns_top_five))

with open(file_name, 'w') as file_handle:  
    # set the new output channel
    sys.stdout = file_handle
    for line in file_content:
        print(line)
