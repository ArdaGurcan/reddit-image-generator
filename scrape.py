import os
import praw
import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

load_dotenv()


reddit = praw.Reddit(client_id=os.environ.get("CLIENT_ID"),
                     client_secret=os.environ.get("CLIENT_SECRET"), user_agent=os.environ.get("USER_AGENT"))

subreddit_name = client_secret=os.environ.get("SUBREDDIT")

for post in reddit.subreddit(subreddit_name).top(limit=10, time_filter="all"):
    url = str(post.url)
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
        filename = post.id + ".jpg"
        filepath = f"dataset/{subreddit_name}/{filename}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((512, 512), Image.ANTIALIAS)
        img = img.convert('RGB')
        img.save(filepath, "jpeg")
