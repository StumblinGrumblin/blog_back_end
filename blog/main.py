import webapp2

from scripts.rot13 import rot13

form1 = '''
<html>
  <head>
    <title>StumblinGrumblin.com</title>
  </head>
  <body>
    <h1>STUMBLINGRUMBLIN.COM <br> HOMEPAGE</h1>
    <form action="http:/ww.google.com/search">
      <input name="q">
      <input type="submit">
    </form>
  </body>
</html>
'''

form2 = '''
<html>
  <head>
    <title>Caesar Cipher</title>
  </head>
  <body>
    <h2>Enter some text to Caesar Cipher</h2>
    <form method="post">
      <textarea name="text" style="height: 100px; width: 400px;">%(cipher)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>
</html>
'''

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(form1)

class Rot13(webapp2.RequestHandler):
  def write_form(self, cipher=""):
    self.response.out.write(form2 %{"cipher": cipher})

  def get(self):
      self.write_form()

  def post(self):
    self.write_form("Bob Dole")

###ROT13 cipher###
#x = "Hello!"

#print rot13(x)

app = webapp2.WSGIApplication([('/', MainPage),
  ('/rot13', Rot13)], debug=True)
