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

class StudentHomePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('studenthome.html')
        self.response.out.write(template.render(vars))

class StudentLifePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('studentlife.html')
        self.response.out.write(template.render(vars))

class UniversityChoicePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('universitychoice.html')
        self.response.out.write(template.render(vars))

class DevelopSkillsPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('developskills.html')
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

class SafetyPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
    	template = JINJA_ENVIRONMENT.get_template('safety.html')
        self.response.out.write(template.render(vars))

class VisaPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('visa.html')
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

class StudentDetailFormPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'studentdetailform'}
        template = JINJA_ENVIRONMENT.get_template('studentdetailform.html')
        self.response.out.write(template.render(vars))

class CounselorHomePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/counselorhome.html')
        self.response.out.write(template.render(vars))

class CounselorDetailPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/detail.html')
        self.response.out.write(template.render(vars))

class CounselorCostsPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/costs.html')
        self.response.out.write(template.render(vars))

class CounselorSchedulePage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/schedule.html')
        self.response.out.write(template.render(vars))

class CounselorApplyPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/apply.html')
        self.response.out.write(template.render(vars))

class CounselorAboutPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/about.html')
        self.response.out.write(template.render(vars))

class CounselorContactPage(webapp2.RequestHandler):
    def get(self):
        vars = {'page': 'home'}
        template = JINJA_ENVIRONMENT.get_template('counselor/contact.html')
        self.response.out.write(template.render(vars))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/studenthome', StudentHomePage),
    ('/studentlife', StudentLifePage),
    ('/universitychoice', UniversityChoicePage),
    ('/developskills', DevelopSkillsPage),
    ('/apply', ApplyPage),
    ('/applicationform', ApplicationFormPage),
    ('/costs', CostsPage),
    ('/schedule', SchedulePage),
    ('/safety', SafetyPage),
    ('/accommodation', AccommodationPage),
    ('/visa', VisaPage),
    ('/about', AboutPage),
    ('/contact', ContactPage),
    ('/testimonials', TestimonialsPage),
    ('/studentdetailform', StudentDetailFormPage),
    ('/counselorhome', CounselorHomePage),
    ('/counselordetail', CounselorDetailPage),
    ('/counselorapply', CounselorApplyPage),
    ('/counselorcosts', CounselorCostsPage),
    ('/counselorschedule', CounselorSchedulePage),
    ('/counselorabout', CounselorAboutPage),
    ('/counselorcontact', CounselorContactPage),
], debug=True)
