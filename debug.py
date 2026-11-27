import os
import tweepy

def check(name):
    v = os.environ.get(name, "")
    print(f"{name}: length={len(v)} start={v[:3]} end={v[-3:] if v else ''}")

for k in ["API_KEY","API_SECRET","ACCESS_TOKEN","ACCESS_SECRET"]:
    check(k)

try:
    client = tweepy.Client(
        consumer_key=os.environ["API_KEY"],
        consumer_secret=os.environ["API_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_SECRET"]
    )
    me = client.get_me()
    print(f"SUCCESS: logged in as @{me.data.username}")
except tweepy.TweepyException as e:
    print(f"FAILED: {e}")
    print("If 401 = keys wrong / swapped / space. If 403 = permissions Read-only or app not in Pay Per Use project.")
except Exception as e:
    print(f"OTHER ERROR: {e}")
