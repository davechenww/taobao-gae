import webapp2

import settings

from views import *


app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/sign', Guestbook),
    ],
    debug=settings.DEBUG)

