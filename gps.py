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
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(vars))

class LifePlanPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('lifeplan.html')
        self.response.out.write(template.render(vars))

class EnterpriseProjectPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('enterpriseproject.html')
        self.response.out.write(template.render(vars))

class CulturePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('culture.html')
        self.response.out.write(template.render(vars))

class ApplyPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('apply.html')
        self.response.out.write(template.render(vars))

class ApplicationFormPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('applicationform.html')
        self.response.out.write(template.render(vars))

class FeePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('fee.html')
        self.response.out.write(template.render(vars))

class CostsPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('costs.html')
        self.response.out.write(template.render(vars))

class SchedulePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('schedule.html')
        self.response.out.write(template.render(vars))

class ScholarshipPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('scholarship.html')
        self.response.out.write(template.render(vars))

class EnquiryPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('enquiry.html')
        self.response.out.write(template.render(vars))

class AccommodationPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('accommodation.html')
        self.response.out.write(template.render(vars))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'about'}
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.out.write(template.render(vars))

class ContactPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'contact'}
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.out.write(template.render(vars))

class TestimonialsPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'testimonial'}
        template = JINJA_ENVIRONMENT.get_template('testimonials.html')
        self.response.out.write(template.render(vars))


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
    ('/about', AboutPage),
    ('/contact', ContactPage),
    ('/testimonials', TestimonialsPage),
], debug=True)
