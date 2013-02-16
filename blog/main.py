import webapp2

import cgi

from scripts.rot13 import rot13

def escape_html(s):
  return cgi.escape(s, quote = True)

form1 = '''
<html>
  <head>
    <title>StumblinGrumblin.com</title>
  </head>
  <body>
    <h1>STUMBLINGRUMBLIN.COM <br> HOMEPAGE</h1>
    <a href="/rot13">Caesar Cipher Project</a>
    <br>
    <a href="/signup">Signup Page</a>
    <br>
    <form action="http:/ww.google.com/search">
    <h3>Search for something on Google</h3>
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
      <textarea name="text" style="height: 100px; width: 400px;">%(output)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>
</html>
'''

form3 = '''
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tbody><tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="">
          </td>
          <td class="error">
            
          </td>
        </tr>
      </tbody></table>

      <input type="submit">
    </form>

</body></html>
'''

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(form1)

class Rot13(webapp2.RequestHandler):
  def write_form(self, output=""):
    self.response.out.write(form2 %{"output": escape_html(output)})

  def get(self):
    self.write_form()

  def post(self):
    sin = self.request.get("text")
    ciph = rot13(sin)
    self.write_form(ciph)

class Signup(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(form3)


app = webapp2.WSGIApplication([('/', MainPage),
  ('/rot13', Rot13), ('/signup', Signup)], debug=True)
