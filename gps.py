import os
import urllib

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render({}))

class LifePlanPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('lifeplan.html')
        self.response.out.write(template.render({}))

class EnterpriseProjectPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('enterpriseproject.html')
        self.response.out.write(template.render({}))

class CulturePage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('culture.html')
        self.response.out.write(template.render({}))

class ApplyPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('apply.html')
        self.response.out.write(template.render({}))

class ApplicationFormPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('applicationform.html')
        self.response.out.write(template.render({}))

class FeePage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('fee.html')
        self.response.out.write(template.render({}))

class CostsPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('costs.html')
        self.response.out.write(template.render({}))

class SchedulePage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('schedule.html')
        self.response.out.write(template.render({}))

class ScholarshipPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('scholarship.html')
        self.response.out.write(template.render({}))

class EnquiryPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('enquiry.html')
        self.response.out.write(template.render({}))

class AccommodationPage(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('accommodation.html')
        self.response.out.write(template.render({}))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/lifeplan', LifePlanPage),
    ('/enterpriseproject', EnterpriseProjectPage),
    ('/culture', CulturePage),
    ('/apply', ApplyPage),
    ('/applicationform', ApplicationFormPage),
    ('/fee', FeePage),
    ('/costs', CostsPage),
    ('/schedule', SchedulePage),
    ('/scholarship', ScholarshipPage),
    ('/enquiry', EnquiryPage),
    ('/accommodation', AccommodationPage),
], debug=True)