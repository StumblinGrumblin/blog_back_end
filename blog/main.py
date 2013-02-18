import os
import re
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db

from scripts.rot13 import rot13

from scripts.validate import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(BaseHandler):
  def get(self):
    self.render('index.html')

class AboutPage(BaseHandler):
  def get(self):
    self.render('about.html')

class Rot13(BaseHandler):
  
  def get(self):
    self.render('rot13.html')

  def post(self):
    rotty =''
    text = self.request.get('text')
    if text:
      rotty = rot13(text)
    self.render('rot13.html', text = rotty)


class Signup(BaseHandler):
  def get(self):
    self.render('signup.html')

  def post(self):
    have_error = False
    username = self.request.get('username')
    password = self.request.get('password')
    verify = self.request.get('verify')
    email = self.request.get('email')

    params = dict(username = username, email = email)

    if not valid_username(username):
      params['error_username'] = "That's not a valid username"
      have_error = True

    if not valid_password(password):
      params['error_password'] = "That wasn't a valid password."
      have_error = True
    elif password != verify:
      params['error_verify'] = "Your passwords didn't match."
      have_error = True

    if not valid_email(email):
      params['error_email'] = "That's not a valid email."
      have_error = True

    if have_error:
      self.render('signup.html', **params)
    else:
      self.redirect('/welcome?username=' + username)


class Welcome(BaseHandler):
  def get(self):
    username = self.request.get('username')
    if valid_username(username):
      self.render('welcome.html', username = username)
    else:
      self.redirect('/signup')

app = webapp2.WSGIApplication([('/', MainPage), ('/about', AboutPage), ('/rot13', Rot13), ('/signup', Signup), ('/welcome', Welcome)], debug=True)
