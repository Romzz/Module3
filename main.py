import webapp2
from google.appengine.ext import ndb
import jinja2
import os
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# setting student info in db
class Thesis(ndb.Model):
   year = ndb.StringProperty(indexed=True)
   title = ndb.StringProperty(indexed=True)
   abstract = ndb.StringProperty(indexed=True)
   adviser = ndb.StringProperty(indexed=True)
   section = ndb.StringProperty(indexed=True)
    # date = ndb.DateTimeProperty(auto_now_add=True)

	
# create student page
class NewThesisEntry(webapp2.RequestHandler):
   def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render())
   def post(self):
		entry = Thesis()
		entry.year = self.request.get('year')
		entry.title = self.request.get('title')
		entry.abstract = self.request.get('abstract')
		entry.adviser = self.request.get('adviser')
		entry.put()
		self.redirect('/')

		
app = webapp2.WSGIApplication([
    ('/', NewThesisEntry)
], debug=True)
