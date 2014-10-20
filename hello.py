import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Congrats you got the app engine up and running! ')
        self.response.write('Crawl, walk, run haha! ')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)