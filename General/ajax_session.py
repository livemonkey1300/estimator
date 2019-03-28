from .json_import import PRICE_TABLE
from django.urls import reverse
from django.shortcuts import render
from django import template
from django.template import Template
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.template import RequestContext

class AJAX:
    def __init__( self , request , SESSION_NAME , FORM_OBJECT_REFERENCE=False , start_form=False , reset=False , session_process=True ):
        self.request = request
        self.reset = reset
        self.session_name =  SESSION_NAME
        self.Forms = []
        self.session = ''
        self.session_referece = ''
        self.current_field = ''
        self.field = ''
        self.total = 0
        self.save_total = 0
        self.post = False
        self.saved = {}
        self.validated = True
        self.FORM_OBJECT_REFERENCE = FORM_OBJECT_REFERENCE
        self.start_form = start_form
        self.init_process_form(session_process)

    def get_render_extended(self,post_location,template_direction='FORM_TPL/extend.html'):
        template = 'General/%s' % template_direction
        return render(self.request , template , self.get_context(post_location) )

    def get_render_small_form(self,post_location,template_direction='extend.html',form_id=0):
        template = 'General/FORM_TPL/%s' % template_direction
        return mark_safe(render_to_string(template , self.get_context(post_location,form_id=form_id) , request=self.request ))

    def get_render_initial_form(self,post_location,template_direction='inititial_Form.html',sub_form_url=False):
        template = 'General/FORM_TPL/%s' % template_direction
        return mark_safe(render_to_string(template , self.get_context(post_location,sub_form_url) , request=self.request ))


    def get_context(self,post_location,sub_form_url=False,form_id=0):
        context = {
        'form': self.Forms[form_id] ,
        'email': reverse('General:send_email'),
        'pk' : reverse('General:%s' % post_location ) ,
        'call' : reverse('General:call' , kwargs={'form_name': self.session_name }) ,
        'flush' : reverse('General:flush'),
        'total' : self.total ,
        'form_id' : '%s_FORM' % self.session_name ,
        }
        if sub_form_url:
            context.update({ 'sub_form_url' : reverse('General:%s' % sub_form_url ) })
        return context

    def get_estimate_context(self,post_location):
        context = self.get_context(post_location)
        context.update({
        'quote': self.saved
        })
        return { 'valid' : self.validated , 'context' : context }

    def init_process_form(self,session_process):
        if session_process:
            self.start_session_modification()
        else:
            print('ok')

# Set The session to be modified , and set object refence to the current form name
    def start_session_modification(self):
        self.session = self.request.session
        self.session.modified = True
        try:
            self.saved = self.session['saved']
        except KeyError:
            self.session['saved'] = []
            self.saved = self.session['saved']
        try:
            if not self.reset:
                self.session_referece = self.session[self.session_name]
            else:
                self.session[self.session_name] = {}
                self.session_referece = self.session[self.session_name]
        except KeyError:
             self.session[self.session_name] = {}
             self.session_referece = self.session[self.session_name]
        if self.request.method == 'POST':
            self.post = True
        if self.FORM_OBJECT_REFERENCE:
            if self.start_form:
                self.add_form_init_session(self.FORM_OBJECT_REFERENCE)
            else:
                self.add_form(self.FORM_OBJECT_REFERENCE)

# Add Form reference , For pre session population
    def add_form(self,form,instance_ref=False):
        if self.post:
            if instance_ref:
                self.Forms.append(form(self.request.POST,instance=instance_ref))
            else:
                self.Forms.append(form(self.request.POST))
        else:
            try:
                if instance_ref:
                    self.Forms.append(form(instance=instance_ref))
                else:
                    self.Forms.append(form(initial=request.session['respawn'][self.session_name]))
            except Exception as e:
                self.Forms.append(form())


# Fetch the current field refenced price
    def get_current_field_price(self):
        try:
            price = PRICE_TABLE[self.field]['price']
            print(price)
            if price == 'on':
                reference = PRICE_TABLE[self.field]['on']
                return  self.session_referece[reference]['price']
            else:
                return price
        except KeyError:
            try:
                print(self.field)
                print(self.current_field['value'])
                price = PRICE_TABLE[self.field][self.current_field['value']]
                print(price)
                return  price
            except KeyError:
                return 0

    def set_respawn_form_data(self,forms_post_data):
        try:
           self.request.session['respawn'][self.session_name] = forms_post_data
        except KeyError:
           self.request.session['respawn'] = { self.session_name : forms_post_data }

    def init_form_session(self,cache=0):
        posted_fields = {}
        posted_fields_display = {}
        redirect = True
        forms_post_data = {}
        for form in self.Forms:
            if self.post:
                if form.is_valid():
                    current_form = form.cleaned_data
                    forms_post_data.update(current_form)
                    for key , value in current_form.items():
                        self.set_current_field_session( key , value )
                        posted_fields[key] = value
                        posted_fields_display[key] = { 'value' : value , 'data' : self.current_field , 'nice_name' : form.fields[key].label }
                else:
                    self.validated = False
            else:
                for item in form.fields.items():
                    self.set_current_field_session( item[0] ,  item[1].initial  )
                    posted_fields[item[0]] = item[1].initial
                    posted_fields_display[item[0]] = { 'value' : item[1].initial , 'data' : self.current_field , 'nice_name' : item[1].label }
        self.set_session_name_price()
        self.saved[cache] = { self.session_name : { 'post' : posted_fields , 'data' : posted_fields_display }}
        self.set_respawn_form_data(forms_post_data)
        return { 'redirect' : True , 'mail' : True , 'mail_data' : self.saved }


    def add_form_init_session(self,form):
        self.add_form(form)
        self.init_form_session()


    def post_set_current_field_session(self):
         try:
             self.current_field = self.session_referece[self.field]
         except KeyError:
             self.session_referece[self.field] = {}
             self.current_field = self.session_referece[self.field]
             print(self.request.POST.get(self.field))
         self.current_field['value'] = self.request.POST.get(self.field)
         self.current_field['price'] = self.get_current_field_price()
         try:
              self.current_field['current'] = float(self.current_field['value']) * self.current_field['price']
         except Exception as e:
              self.current_field['current'] = self.current_field['price'] *  1

    def initial_set_current_field_session(self , value):
         try:
             self.current_field = self.session_referece[self.field]
         except KeyError:
             self.session_referece[self.field] = {}
             self.current_field = self.session_referece[self.field]
         self.current_field['value'] = value
         self.current_field['price'] = self.get_current_field_price()
         try:
              self.current_field['current'] = float(self.current_field['value']) * self.current_field['price']
         except Exception as e:
              self.current_field['current'] = self.current_field['price'] *  1



# Set all the field necessary value to the session cookie reference
    def set_current_field_session(self , field , value=False):
     remove = False
     self.field = field
     if self.post:
         print(self.field)
         self.post_set_current_field_session()
     else:
         self.initial_set_current_field_session(value)


    def set_session_name_price(self):
      for key , val in self.session_referece.items():
          self.total += float(val['current'])
      self.request.session['total'] = self.total

# return the updated value form the session
    def get_session_updated_json(self):
        self.set_session_name_price()
        return { 'success' : True , 'field' : self.current_field['value'] , 'price' : self.current_field['price'] , 'current' : self.current_field['current'] , 'total'  : self.total , 'saving' : self.save_total }

# process the update an return the updated values
    def quick_update_respond(self , field):
        self.set_current_field_session(field)
        return self.get_session_updated_json()
