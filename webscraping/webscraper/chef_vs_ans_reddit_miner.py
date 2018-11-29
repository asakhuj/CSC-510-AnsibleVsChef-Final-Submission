'''
@author: atrivedi
'''
import pandas as pd
import praw
import time

start = time.time()

# praw api to connect to reddit
reddit = praw.Reddit(client_id='#INSERT_YOUR_ID', \
                     client_secret='#INSERT_YOUR_SECRET_KEY', \
                     user_agent='#YOUR_APP_NAME', \
                     username='#YOUR_USER_NAME', \
                     password='#YOUR_PASSWORD')

# define subreddits intersted in
subreddit_sysadmin = reddit.subreddit('sysadmin')
subreddit_devops = reddit.subreddit('devops')
subreddit_linuxadmin = reddit.subreddit("linuxadmin")
subreddit_ansible = reddit.subreddit("ansible")
subreddit_aws = reddit.subreddit("aws")
subreddit_chef = reddit.subreddit("chef_opscode")

def scrape_topics_and_comments(subreddit, description, comments_from_each_thread, search_query="ansible vs chef"):
    for submissions in subreddit.search(search_query):
        if submissions.selftext:
            description.append(submissions.selftext)
        for comment in submissions.comments:
            comments_from_each_thread.append(comment.body)


description = []
comments_from_each_thread = []

print("Start populating contents")
scrape_topics_and_comments(subreddit_sysadmin, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

scrape_topics_and_comments(subreddit_devops, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

scrape_topics_and_comments(subreddit_linuxadmin, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

scrape_topics_and_comments(subreddit_ansible, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

scrape_topics_and_comments(subreddit_aws, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

scrape_topics_and_comments(subreddit_chef, description, comments_from_each_thread)
print(len(description), len(comments_from_each_thread))

print(f"It took {time.time() - start}")

print(description)
df = pd.DataFrame({"comments":comments_from_each_thread})
# print(df.head(10))
df.to_csv(".dataset/reddit_ansible_vs_chef.csv")
