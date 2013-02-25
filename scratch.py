

   ''' visits = 0
    visit_cookie_str = self.request.cookies.get('visits')
    if visit_cookie_str:
      cookie_val = check_secure_val(visit_cookie_str)
      if cookie_val:
        visits = int(cookie_val)

    visits += 1

    new_cookie_val = make_secure_val(str(visits))

    self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

    if visits > 100:
      self.write("You rock!")
    else:
      self.write("You've been here %s times!" % visits)'''


	'''def get(self):
		self.render("signup.html")

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

###Validation Code
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	def valid_username(username):
		return username and USER_RE.match(username)

	PASS_RE = re.compile(r"^.{3,20}$")
	def valid_password(password):
		return password and PASS_RE.match(password)

	EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
	def valid_email(email):
		return not email or EMAIL_RE.match(email)'''



    self.response.headers['Content-Type'] = 'text/plain'
    visits = self.request.cookies.get('visits', '0')
    if visits.isdigit():
      visits = int(visits) + 1
    else:
      visits = 0

    self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)
    self.write("You have been here %s times!" % visits)