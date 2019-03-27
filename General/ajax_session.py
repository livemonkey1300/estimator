from .json_import import PRICE_TABLE
from django.urls import reverse
from django.shortcuts import render

class AJAX:
    def __init__( self , request , Form_Session , initial_form=False , start_form=False , reset=False , session_process=True ):
        self.request = request
        self.reset = reset
        self.Form_Session =  Form_Session
        self.Forms = []
        self.session = ''
        self.session_form_referece = ''
        self.current_field = ''
        self.field = ''
        self.total = 0
        self.save_total = 0
        self.post = False
        self.saved = {}
        self.validated = True
        self.initial_form = initial_form
        self.start_form = start_form
        self.form_init(session_process)

    def get_render(self,post_location,template_direction='FORM_TPL/extend.html'):
        template = 'General/%s' % template_direction
        return render(self.request , template , self.get_context(post_location) )

    def get_context(self,post_location):
        context = {
        'form': self.Forms[0] ,
        'email': reverse('General:send_email'),
        'pk' : reverse('General:%s' % post_location ) ,
        'call' : reverse('General:call' , kwargs={'form_name': self.Form_Session }) ,
        'flush' : reverse('General:flush'),
        'total' : self.total ,
        }
        return context

    def get_estimate_context(self,post_location):
        context = self.get_context(post_location)
        context.update({
        'quote': self.saved
        })
        return { 'valid' : self.validated , 'context' : context }

    def form_init(self,session_process):
        if session_process:
            self.init_session_change()
        else:
            print('ok')

# Set The session to be modified , and set object refence to the current form name
    def init_session_change(self):
        self.session = self.request.session
        self.session.modified = True
        try:
            self.saved = self.session['saved']
        except KeyError:
            self.session['saved'] = []
            self.saved = self.session['saved']
        try:
            if not self.reset:
                self.session_form_referece = self.session[self.Form_Session]
            else:
                self.session[self.Form_Session] = {}
                self.session_form_referece = self.session[self.Form_Session]
        except KeyError:
             self.session[self.Form_Session] = {}
             self.session_form_referece = self.session[self.Form_Session]
        if self.request.method == 'POST':
            self.post = True
        if self.initial_form:
            if self.start_form:
                self.add_form_set(self.initial_form)
            else:
                self.add_form(self.initial_form)

# Add Form reference , For pre session population
    def add_form(self,form,param=False):
        if self.post:
            self.Forms.append(form(self.request.POST))
        else:
            try:
                self.Forms.append(form(initial=request.session['tmp'][self.Form_Session]))
            except Exception as e:
                self.Forms.append(form())


# Fetch the current field refenced price
    def get_price_table(self):
        try:
            return  PRICE_TABLE[self.field]['price']
        except KeyError:
            return 0

    def set_tmp_form_session(self,current_forms):
        try:
           self.request.session['tmp'][self.Form_Session] = current_forms
        except KeyError:
           self.request.session['tmp'] = { self.Form_Session : current_forms }

    def set_form_session(self,cache=0):
        current_fields = {}
        current_fields_print = {}
        redirect = True
        current_forms = {}
        for form in self.Forms:
            if self.post:
                if form.is_valid():
                    current_form = form.cleaned_data
                    current_forms.update(current_form)
                    for key , value in current_form.items():
                        self.update_form_session( key , value )
                        current_fields[key] = value
                        current_fields_print[key] = { 'value' : value , 'data' : self.current_field , 'nice_name' : form.fields[key].label }
                else:
                    self.validated = False
            else:
                for item in form.fields.items():
                    self.update_form_session( item[0] ,  item[1].initial  )
                    current_fields[item[0]] = item[1].initial
                    current_fields_print[item[0]] = { 'value' : item[1].initial , 'data' : self.current_field , 'nice_name' : item[1].label }
        self.get_price_form()
        self.saved[cache] = { self.Form_Session : { 'post' : current_fields , 'data' : current_fields_print }}
        self.set_tmp_form_session(current_forms)
        return { 'redirect' : True , 'mail' : True , 'mail_data' : self.saved }


    def add_form_set(self,form):
        self.add_form(form)
        self.set_form_session()


    def post_update_form_session(self):
         try:
             self.current_field = self.session_form_referece[self.field]
         except KeyError:
             self.session_form_referece[self.field] = {}
             self.current_field = self.session_form_referece[self.field]
         self.current_field['value'] = self.request.POST.get(self.field)
         self.current_field['price'] = self.get_price_table()
         try:
              self.current_field['current'] = float(self.current_field['value']) * self.current_field['price']
         except Exception as e:
              self.current_field['current'] = self.current_field['price'] *  1

    def initial_update_form_session(self , value):
         try:
             self.current_field = self.session_form_referece[self.field]
         except KeyError:
             self.session_form_referece[self.field] = {}
             self.current_field = self.session_form_referece[self.field]
         self.current_field['value'] = value
         self.current_field['price'] = self.get_price_table()
         try:
              self.current_field['current'] = float(self.current_field['value']) * self.current_field['price']
         except Exception as e:
              self.current_field['current'] = self.current_field['price'] *  1



# Set all the field necessary value to the session cookie reference
    def update_form_session(self , field , value=False):
     remove = False
     self.field = field
     if self.post:
         self.post_update_form_session()
     else:
         self.initial_update_form_session(value)


    def get_price_form(self):
      for key , val in self.session_form_referece.items():
          self.total += float(val['current'])
      self.request.session['total'] = self.total

# return the updated value form the session
    def get_updated_form_session(self):
        self.get_price_form()
        return { 'success' : True , 'field' : self.current_field['value'] , 'price' : self.current_field['price'] , 'current' : self.current_field['current'] , 'total'  : self.total , 'saving' : self.save_total }

# process the update an return the updated values
    def quick_update_respond(self , field):
        self.update_form_session(field)
        return self.get_updated_form_session()
