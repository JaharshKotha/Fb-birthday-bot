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


graph = facebook.GraphAPI(access_token='EAACEdEose0cBAI3DSQmfCn9KIV8bLZCTuI7zGVUcFzKUY18y69UjZASH8egvKZBa8Bos0LQ06esvksEATzGG2ln0oIWOMJZATaA7x7TCrFBAwa8qYjmoVdo3f4kb0wCgpMFgXomVvxJHu7cZBQE6nzUFt8Jp0JINBf7M8Qu1oNqm1KIuijQl1BZA9sf4Rg9mcZD')

profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')
print posts


while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
         break
