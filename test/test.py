import os
import webapp2
import jinja2
import re

from google.appengine.ext import db

from string import letters
import hashlib
import hmac
import random

from scripts.rot13 import *
from scripts.validate import *

secret = "Open_Sesame_Seed"

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
  autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))

####Hash Functions
def hash_str(s):
  return hashlib.md5(s).hexdigest()

def hmac_str(val):
  return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def make_secure_val(s):
  return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
  val = h.split('|')[0]
  if h == make_secure_val(val):
    return val

class MainPage(Handler):
  def get(self):
    self.render("index.html")

class LoginPage(Handler):
  def get(self):
    self.render("login-form.html")

class Signup(Handler):
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


class Welcome(Handler):
  def get(self):
    username = self.request.get('username')
    if valid_username(username):
      self.render('welcome.html', username = username)
    else:
      self.redirect('/signup')

app = webapp2.WSGIApplication([('/', MainPage), 
  ('/login', LoginPage), ('/signup', Signup), ('/welcome', Welcome)], debug=True)
