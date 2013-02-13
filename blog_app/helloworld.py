import webapp2

form= """
<head>
	<title>Caesar Cipher</title>
</head>
<body>
	<h2>Enter some text to Caesar Cipher</h2>
	<form method="post">
		<textarea name="text" style="height: 100px; width: 400px;"></textarea>
		<br>
		<input type="submit">
	</form>
</body>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
      #self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self):
		q = self.request.get("q")
		self.response.out.write(q)
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
('/testform',TestHandler)],
debug=True)
