#!/usr/bin/env python

import requests
r = requests.get('https://www.googleapis.com/youtube/v3/subscriptions?part=snippet&channelId=CHANELL&key=KEY&part=snippet')
print("Status Code:: " + str(r.status_code))
print("Text: " + r.text)

#
# T https://www.googleapis.com/youtube/v3/channels?part=contentDetails&mine=true