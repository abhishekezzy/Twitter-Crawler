# -*- coding: utf-8 -*-
import oauth2
import oauth
import urllib
import json
import hidden2
secrets=hidden2.oauth1()
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=secrets['consumer_key'],secret= secrets['consumer_secret'])
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
#timeline = oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=abhishek_ezzy&count=2', secrets['token_key'],secrets['token_secret'])
#j=json.loads(timeline)
#print json.dumps(j,indent=4)
#k= j[0]["user"]["profile_image_url_https"]
#urllib.urlretrieve(k,"C:\\Users\\Abhishek\\Desktop\\Python\\myimage.jpg")