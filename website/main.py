import webapp2

import settings

from views import *


app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/submit', SubmitUrl),
    ],
    debug=settings.DEBUG)

