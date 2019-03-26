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
        self.headers = {'Reply-To': 'adam@dnsnetworks.ca' }
        self.from_email = 'webmaster@dnsnetworks.ca'
        self.content_subtype = "html"
        self.content = ''
        # self.to = ['adam@dnsnetworks.ca','shawn.ebbs@dnsnetworks.ca','natasha@dnsnetworks.ca']
        self.to = ['adam@dnsnetworks.ca']

        self.to_admin = ['adam@dnsnetworks.ca']
        self.from_email_admin = 'webmaster@dnsnetworks.ca'
        self.headers_admin = {'Reply-To': 'adam@dnsnetworks.ca' }

    def set_mail_config(self):
        return { 'first_name' : self.form['your_name'] , 'last_name' : self.form['last_name'] , 'email' : self.form['email'] , 'telephone' : self.form['tel'] }

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
        email = EmailMessage('Quote', self.build_content() , to=self.to ,headers=self.headers)
        email.from_email = self.from_email
        email.content_subtype = self.content_subtype
        email.send()
