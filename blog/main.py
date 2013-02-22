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
    def write(self, *a, **kw):
      self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
      return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

def render_post(response, post):
  response.out.write('<b>' + post.subject + '</b><br>')
  response.out.write(post.content)


class MainPage(BaseHandler):
  def get(self):
    self.render('index.html')

####BLOG HANDLERS####
def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("/blog/post.html", p = self)

class BlogFront(BaseHandler):
  def get(self):
    posts = db.GqlQuery("select * from Post order by created desc limit 10")
    self.render('/blog/front.html', posts = posts)

class PostPage(BaseHandler):
  def get(self, post_id):
    key = db.Key.from_path('Post', int(post_id), parent=blog_key())
    post = db.get(key)

    if not post:
      self.error(404)
      return

    self.render("/blog/permalink.html", post = post)

class NewPost(BaseHandler):
  def get(self):
    self.render("/blog/newpost.html")

  def post(self):
    subject = self.request.get('subject')
    content = self.request.get('content')

    if subject and content:
      p = Post(parent = blog_key(), subject = subject, content = content)
      p.put()
      self.redirect('/blog/%s' % str(p.key().id()))
    else:
      error = "subject and content, please!"
      self.render("/blog/newpost.html", subject=subject, content=content, error=error)

class AboutPage(BaseHandler):
  def get(self):
    self.render('about.html')

####OTHER PROJECTS####
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

app = webapp2.WSGIApplication([('/', MainPage), ('/about', AboutPage), 
                                ('/rot13', Rot13), 
                                ('/signup', Signup), 
                                ('/welcome', Welcome),
                                ('/blog/?', BlogFront),
                                ('/blog/([0-9]+)', PostPage),
                                ('/blog/newpost', NewPost)
                                ], 
                                debug=True)
