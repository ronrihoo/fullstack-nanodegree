#
# DB Forum - a buggy web forum server backed by a good database
#

# The shoutboxdb module is where the database interface code goes.
# The shoutboxstyle module is where the HTML and style code goes.
import shoutboxdb
from shoutboxstyle import HTML_WRAP, POST

# Other modules used to run a web server.
import cgi
from wsgiref.simple_server import make_server
from wsgiref import util

## Request handler for main page
def View(env, resp):
    '''View is the 'main page' of the forum.

    It displays the submission form and the previously posted messages.
    '''
    # get posts from database
    posts = shoutboxdb.FetchPosts()
    # send results
    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)
    return [HTML_WRAP % ''.join(POST % p for p in posts)]

## Request handler for posting - inserts to database
def Post(env, resp):
    '''Post handles a submission of the forum's form.
  
    The message the user posted is saved in the database, then it sends a 302
    Redirect back to the main page so the user can see their new post.
    '''
    # Get post content
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))

    # Next: some quick and lazy hard-code. 'content=%nickname=' is 18 characters,
    # so, if length is 18, post is empty - don't save it.
    if length > 18:
        postdata = input.read(length)
        fields = cgi.parse_qs(postdata)

        try: content = fields['content'][0]; content = content.strip()
        except: content = False

        try: nickname = fields['nickname'][0]; nickname = nickname.strip()
        except: nickname = False

        # If the post is just whitespace, don't save it.
        # and if the nickname is not provided, then save as "Anonymous".
        if (content and not nickname):
            # Save it in the database
            shoutboxdb.MakePost(content, "Anonymous")
        # If the nickname is provided:
        if (content and nickname):
            shoutboxdb.MakePost(content, nickname)
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

## Dispatch table - maps URL prefixes to request handlers
DISPATCH = {'': View,
            'post': Post,
	         }

## Dispatcher forwards requests according to the DISPATCH table.
def Dispatcher(env, resp):
    '''Send requests to handlers based on the first path component.'''
    page = util.shift_path_info(env)
    if page in DISPATCH:
        return DISPATCH[page](env, resp)
    else:
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain')]
        resp(status, headers)    
        return ['Not Found: ' + page]

# Run this bad server only on localhost!
httpd = make_server('', 8000, Dispatcher)
print "Serving HTTP on port 8000..."
httpd.serve_forever()
