Fullstack common code fork
=============

This is a January 2016 fork of the Udacity Fullstack Nanodegree program's common code.

Changes:

(1) The forum web app has been adapted into a shoutbox web app. 

The server is still the same, so as the original author advises: only run it on your localhost.

This is the reason why I have kept the Vagrant VM configuration in the fork. 

(2) A Python script has been written to create the PostgreSQL database for the shoutbox.

createdb.py

(3) The shoutbox HTML and style is handled in a separate file for ease of future UI updates.

shoutboxstyle.py

The next step is to make the shoutbox look good, so this is going to be convenient.


Tree:


----vagrant
      |----catalog
      |      |----README.txt
      |----shoutbox
      |      |----createdb.py
      |      |----shoutbox.py
      |      |----shoutboxdb.py
      |      |----shoutboxstyle.py
      |----tournament
      |      |----tournament.py
      |      |----tournament.sql
      |      |----tournament_test.py
      |----Vagrantfile
      |----pg_config.sh
----README.md
