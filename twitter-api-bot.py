## Twiter Bot

## Lindsey Norberg, Chloe Dearman, and Julia Schopper
## DS 3002 Final Project


# Importing all the ncessary packages
import tweepy
import logging
import time
from random import randint
import os


# Creating an api object using Twitter credentials
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler("GmMOXHJWAoFGpNQEquvGq6GDL", 
                           "DMuGIVLTdBnQ7BPp39INL2DSCaQv7jnzvxCWIoDn44fZE2rRHs")
auth.set_access_token("1445456363149090817-Cdz2z2a2j5Pc0sbOjX7wZPr08AMyc4", 
                      "t5h1HFWnCJn2rVtCmvW0se5CR9RgJUvsolt1qkj8cTsK8")

# Creating the api object; this will be a global variable used in our bot
api = tweepy.API(auth)


"""
This will be a helper function for the sake of code reusability. It will check the replying user is not the current user 
and if the user is not currently following them, then will follow them if not. 
"""
def check_user(tweet):
    if tweet.user != api.get_user(screen_name = "lmnorberg3"):
        if not tweet.user.following:
            tweet.user.follow() 


def check_mentions(api, keywords, since_id):

    logger.info("Retrieving mentions")
    new_since_id = since_id
    
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if "help" in tweet.text.lower():
            logger.info("Answering to " + tweet.user.name)
            check_user(tweet)
            api.update_status(
                status= "REF: " + str(randint(0, 100)) + " Hey there! DM us for any help related questions.",
                in_reply_to_status_id = tweet.id, 
                auto_populate_reply_metadata=True)
            
        if "info" in tweet.text.lower():
            logger.info("Answering to " + tweet.user.name)
            check_user(tweet)
            api.update_status(
                status= "REF: " + str(randint(0, 100)) + " Hey there! DM us for more information.",
                in_reply_to_status_id = tweet.id, 
                auto_populate_reply_metadata=True)
            
        # This is where we will handle the actual keywords givin in the function 
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info("Answering to " + tweet.user.name)
            check_user(tweet)
            api.update_status(
                status= "REF: " + str(randint(0, 100)) + " Big uva hoops fan! So excited for the game.",
                in_reply_to_status_id = tweet.id, 
                auto_populate_reply_metadata=True)
    return new_since_id

def main():
    global api
    since_id = 1
    while True:
        since_id = check_mentions(api, ["wahoos", "hoos", 
                                       "uva", "basketball", "hoops", "wahoowa", "uva", "cavaliers"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
