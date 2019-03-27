from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template

from django.core.mail import EmailMessage

class Mailer:
    def __init__( self , request , form ):
        self.request = request
        self.form = form.cleaned_data
        # self.headers = {'Reply-To': 'sales@dnsnetworks.ca' }
        self.headers = {'Reply-To': 'sales@dnsnetworks.ca' }
        self.from_email = 'sales@dnsnetworks.ca'
        self.content_subtype = "html"
        self.content = ''
        # self.to = ['adam@dnsnetworks.ca','shawn.ebbs@dnsnetworks.ca','natasha@dnsnetworks.ca']
        self.to = []

        self.to_admin = ['sales@dnsnetworks.ca']
        self.from_email_admin = ''
        self.headers_admin = {'Reply-To': '' }

    def set_mail_config(self):
        self.from_email_admin = self.form['email']
        self.headers_admin = {'Reply-To': self.form['email'] }
        self.to = [self.form['email']]
        return { 'first_name' : self.form['your_name'] , 'last_name' : self.form['last_name'] , 'email' : self.form['email'] , 'telephone' : eval(self.form['tel']) }

    def build_content(self):
        cart = self.request.session['saved']
        total = self.request.session['total']
        context = { 'quote' : cart   , 'total' :  total }
        context.update(self.set_mail_config())
        template = get_template('General/Main/mail.html')
        content = template.render(context)
        return content

    def send(self):
        # self.set_mail_config()
        email = EmailMessage('Estimate', self.build_content() , to=self.to ,headers=self.headers)
        email.from_email = self.from_email
        email.content_subtype = self.content_subtype
        email.send()

    def send_admin(self):
        # self.set_mail_config()
        email = EmailMessage('Estimate %s' % self.from_email_admin , self.build_content() , to=self.to_admin ,headers=self.headers_admin)
        email.from_email = self.from_email_admin
        email.content_subtype = self.content_subtype
        email.send()
