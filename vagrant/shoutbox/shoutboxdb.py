import time
import psycopg2
import bleach

# Fetch posts from database.
def FetchPosts():
    db = psycopg2.connect("dbname = shoutbox")
    c = db.cursor()
    query = "select * from posts order by time desc;"
    c.execute(query)
    rows = c.fetchall() 
    posts = [{'content': str(row[0]), 'nickname': str(row[1]), 'time': str(row[2])} for row in rows]
    posts.sort(key=lambda row: row['time'], reverse=True)
    db.close()
    return posts

# Make a post to the database
def MakePost(content, nickname):
    try:
        # clean content
        try: 
            bleach.clean(content)
        except:
            print "Error: content bleach failed."
            return

        # clean nickname
        try: 
            bleach.clean(nickname)
        except:
            print "Error: nickname bleach failed."
            return

        # connect to database and add content
        try: 
            db = psycopg2.connect("dbname = shoutbox")
            c = db.cursor()
            t = time.strftime('%c', time.localtime())
            c.execute("insert into posts (content, nickname, time) values (%s, %s, %s);", 
                      (content, nickname, t)
                     )
            db.commit()
            db.close()
        except:
            print "Error: connection or database failure."
            return

    except:
      print "Error: an unexpected failure has occurred."
      return

    return

# Clean up an arbitrary type of post
def CleanContent(content):
    db = psycopg2.connect("dbname = shoutbox")
    c = db.cursor()
    query = "delete from posts where content like %s;"
    c.execute(query, (content,))
    db.commit()
    db.close()
    return
