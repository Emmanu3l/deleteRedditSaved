# look up or create your "developed application" on https://www.reddit.com/prefs/apps/
# select "script" as your application type
# no need to change anything aside from using e.g. http://localhost:8080 as your redirect uri
# get client_id (listed below "personal use script" in your "developed applications" list) and client_secret from there

import praw

username = input("Enter your username: ")
password = input("Enter your password: ")
client_id = input("Enter your client_id [check reddit.com/prefs/apps]: ")
client_secret = input("Enter your client_secret [check reddit.com/prefs/apps]: ")

r = praw.Reddit(client_id=client_id,
                client_secret=client_secret,
                password=password,
                user_agent="saved post deleter",
                username=username)
print("Deleting posts for u/" + r.user.me().name)

for saved in r.user.me().saved(limit=100):
    if isinstance(saved, praw.models.Submission):
        r.submission(id=saved.id).unsave()
    elif isinstance(saved, praw.models.Comment):
        r.comment(id=saved.id).unsave()
