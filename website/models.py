from google.appengine.ext import db


class Shop(db.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    taobao_id = db.StringProperty()
    name = db.StringProperty()
    add_date = db.DateTimeProperty(auto_now_add=True)

    def get_taobao_url(self):
        return 'shop%s.taobao.com' % self.taobao_id

