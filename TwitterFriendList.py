import twurl2
import urllib
import json
import hidden2
import os
secret=hidden2.oauth1()
tweeturl="https://api.twitter.com/1.1/friends/list.json?"
while True:
    screen_name=raw_input("Enter valid username: ")
    if(len(screen_name)<1):
        break
    twurl=tweeturl+"screen_name="+screen_name+"&count=5"
    #print twurl
    url=twurl2.oauth_req(twurl,secret['token_key'],secret['token_secret'])
    j=json.loads(url)
    #print json.dumps(j, indent=4)
    for u in j['users']:
        print "Name: ", u['name']
        print "Location: ", u['location']
        print "Total followers: ", u['followers_count']
        path=str(os.path.expanduser('~'))+u['name']+"image.jpg"
        try:
            print "Latest Tweet: ", u['status']['text']
        except:
            print "No Latest Tweet"
        #urllib.urlretrieve(u['profile_image_url_https'],path) 
        print "\n"
