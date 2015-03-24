from twython import Twython

APP_KEY = 'XXXXX'
APP_SECRET = 'XXXXX'
OAUTH_TOKEN = 'XXXXX'
OAUTH_TOKEN_SECRET = 'XXXXX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

usernames = []

with open("XXXXX", "r") as f:
        lines = f.readlines()

        for line in lines:
                cleaned_line = line.strip()
                usernames.append(cleaned_line)

for username in usernames:
        details = twitter.show_user(screen_name=username)

        profile_image_url = details['profile_image_url']

        output = '{username},{profile_image_url}'.format(username=username, profile_image_url=profile_image_url)
        print output
