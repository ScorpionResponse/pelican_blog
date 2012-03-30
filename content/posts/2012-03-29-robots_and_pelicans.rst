Robots and Pelicans
###################

:date: 2012-03-29
:tags: pelican
:category: coding

My first snag with `Pelican <http://pelican.notmyidea.org/>`_ overcome.  As any
good site creator I wanted to make sure my favicon.ico and robots.txt files
were in place.  Also I despise seeing the 404 errors pop up as I play around
with my site. Pelican doesn't immediately make it obvious how to accomplish
this task.  

With a little bit of Googling, I found `this commit
<https://github.com/ametaireau/pelican/commit/04da794b6bae6f151a946b6edfca7e8d01a6f9f3>`_.
In my /content folder I created a new folder called 'extra' (though that could
have been named anything I figured I would follow the example).  There are two
files in it::

    favicon.ico
    robots.txt

Then we simply add a line to the Pelican settings file::

    FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'), ('extra/favicon.ico', 'favicon.ico'),)

Run a quick ``make html`` and we're ready to roll.
