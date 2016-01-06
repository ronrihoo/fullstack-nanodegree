# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Python ShoutBox</title>
    <style>
      h1, form, div { text-align: center; }
      textarea#content { width: 400px; height: 75px; }
      textarea#nickname { width: 314px; height: 15px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
      em.nickname { color: #FF9900}
    </style>
  </head>

  <body>
    <div>
      <h1>Python ShoutBox</h1>
          <!-- post content will go here -->
          %s
      <form method=post action="/post">
        <div><textarea id="content" name="content"></textarea></div>
        <div>Nickname <textarea id="nickname" name="nickname"></textarea></div>
        <div><button id="go" type="submit">Shout</button></div>
      </form>
    </div>
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''                                                            \
          <div class=post>[<em class=date>%(time)s</em>]              \
                          <em class=nickname>%(nickname)s</em>:       \
                          %(content)s                                 \
          </div>
       '''