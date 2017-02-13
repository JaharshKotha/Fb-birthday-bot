"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    #print "we will be printing the posts one bybone\n"
   # x="test"
    msg=post['message']
    bdaywords = ["happy","bday","birthday","returns","many"]
    if( (x) in msg):
        print post['id']
        graph.put_object(parent_object=post['id'], connection_name='comments', message='First!')




# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBANDoqCRV4t9xA8vI0qSLGfWgDnc6W23hv7dmUUWIcZAEJN2FhR09W82yi6PW9aAq3doxwPACgMCntxnHa0PCQRVOH0rKz39545u3aQZAPb0sNcdt0eZCSO46z8MNssMSbz4wDanVmlnpyvb0ZAdlRZA1sklW9XzMdoamwYRPPO2jPyfS82HDUqXi6ZAHD9mCVqlefmkeNXQOoWbCNVw7cZD'
# Look at Bill Gates's profile for this example by using his Facebook id.
user = '636517556'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')
print posts

#graph.put_object("me", "feed", message="This is an automated test of the Graph-SDK with Python (v2.8)")

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
