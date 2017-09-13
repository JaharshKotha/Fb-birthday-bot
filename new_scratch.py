import facebook
import requests

def some_action(post):
    msg=post['message']
    print msg+"\n"
    bdaywords = ["happy","bday","birthday","returns","many","hbd"]
    sm = msg.split(" ");
    for s in sm :
        if (s.lower() in bdaywords):
            print post['id']
            graph.put_object(parent_object=post['id'], connection_name='comments', message='Thank you!')


graph = facebook.GraphAPI(access_token='')

profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')
print posts


while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
         break
