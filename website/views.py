import urllib

import webapp2

from google.appengine.api import users

import settings

from models import *


class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name')
        greetings_query = Greeting.all().ancestor(
                guestbook_key(guestbook_name)).order('-date')
        greetings = greetings_query.fetch(5)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            'settings': settings
        }

        template = settings.JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name')
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user().nickname()

        greeting.content = self.request.get('content').strip()
        if greeting.content:
            greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

