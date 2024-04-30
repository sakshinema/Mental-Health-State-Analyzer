from twitter_sentiment.twitter import TwitterClient
import json
from flask import jsonify

# Create your views here.
from rest_framework import views
from rest_framework.response import Response

def strtobool(v):
    return v.lower() in ["yes", "true", "t", "1"]

def parse_env_json():
    with open("E:\projects\psychological-ai-backend\\api\\twitter_sentiment\.env.json") as f: #change
        return json.load(f)

api = TwitterClient('Donald Trump', **parse_env_json())

class TwitterView(views.APIView):

    def post(self, request):
        data = request.data
        print(data)
        retweets_only = "no"
        api.set_retweet_checking(strtobool(retweets_only.lower()))
        with_sentiment = "yes"
        api.set_with_sentiment(strtobool(with_sentiment.lower()))
        query = data["query"]
        api.set_query(query)
        api.set_tweetcount(int(data["tweetCount"]))

        tweets = api.get_tweets()
        print("{} tweets".format(len(tweets)))

        return Response({'data': tweets, 'count': len(tweets)})
