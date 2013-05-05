import urllib

import webapp2

from google.appengine.api import users

import settings

from models import *


class MainPage(webapp2.RequestHandler):

    def get(self):
        shops = Shop.all().order('taobao_id').fetch(5)

        template_values = {
            'shops': shops,
            'settings': settings
        }

        template = settings.JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class SubmitUrl(webapp2.RequestHandler):

    def post(self):
        url = self.request.get('url').strip()
        valid = True

        template_values = {
            'url': url,
            'valid': valid,
            'settings': settings
        }

        template = settings.JINJA_ENVIRONMENT.get_template('submit.html')
        self.response.write(template.render(template_values))

