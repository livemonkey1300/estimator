from django import template
from django.template import Template
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.urls import reverse

from General.models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE
register = template.Library()

@register.simple_tag(takes_context=True)
def get_menu(context):
  content = {}
  urls = []
  urls.append({ 'Name' : 'TIME_MANAGEMENT' , 'url' : reverse('General:create_time_management') })
  urls.append({ 'Name' : 'EXCHANGE' , 'url' : reverse('General:create_exchange') })
  urls.append({ 'Name' : 'VOIP' , 'url' : reverse('General:create_voip') })
  urls.append({ 'Name' : 'VIRTUAL_MACHINE' , 'url' : reverse('General:create_virtual_machine') })
  content.update( { 'urls' : urls , 'user' : context['request'].user } )
  return mark_safe(render_to_string('General/TAG_TPL/menu_tag.html' , content ))



@register.simple_tag(takes_context=True)
def get_time_management(context):
  current_user = context['request'].user
  obj_list = []
  listing = False
  if current_user.is_superuser:
    obj_list = TIME_MANAGEMENT.objects.all()
    if len(obj_list) > 0:
        listing = True
    content = { 'Title' : 'TIME_MANAGEMENT' , 'obj_list' : obj_list , 'listing' : listing}
  else:
    if current_user.is_authenticated:
      obj_list = TIME_MANAGEMENT.objects.filter(user=current_user)
      if len(obj_list) > 0:
          listing = True
      content = { 'Title' : 'TIME_MANAGEMENT' , 'obj_list' : TIME_MANAGEMENT.objects.filter(user=current_user) , 'listing' : listing }
    else:
      content = { 'Title' : 'TIME_MANAGEMENT' , 'obj_list' : [] , 'listing' : listing }
  return mark_safe(render_to_string('General/TAG_TPL/list_tag.html' , content ))


@register.simple_tag(takes_context=True)
def get_exchange(context):
  current_user = context['request'].user
  obj_list = []
  listing = False
  if current_user.is_superuser:
    obj_list = EXCHANGE.objects.all()
    if len(obj_list) > 0:
        listing = True
    content = { 'Title' : 'EXCHANGE' , 'obj_list' : obj_list , 'listing' : listing}
  else:
    if current_user.is_authenticated:
      obj_list = EXCHANGE.objects.filter(user=current_user)
      if len(obj_list) > 0:
          listing = True
      content = { 'Title' : 'EXCHANGE' , 'obj_list' : EXCHANGE.objects.filter(user=current_user) , 'listing' : listing }
    else:
      content = { 'Title' : 'EXCHANGE' , 'obj_list' : [] , 'listing' : listing }
  return mark_safe(render_to_string('General/TAG_TPL/list_tag.html' , content ))


@register.simple_tag(takes_context=True)
def get_voip(context):
  current_user = context['request'].user
  obj_list = []
  listing = False
  if current_user.is_superuser:
    obj_list = VOIP.objects.all()
    if len(obj_list) > 0:
        listing = True
    content = { 'Title' : 'VOIP' , 'obj_list' : obj_list , 'listing' : listing}
  else:
    if current_user.is_authenticated:
      obj_list = VOIP.objects.filter(user=current_user)
      if len(obj_list) > 0:
          listing = True
      content = { 'Title' : 'VOIP' , 'obj_list' : VOIP.objects.filter(user=current_user) , 'listing' : listing }
    else:
      content = { 'Title' : 'VOIP' , 'obj_list' : [] , 'listing' : listing }
  return mark_safe(render_to_string('General/TAG_TPL/list_tag.html' , content ))


@register.simple_tag(takes_context=True)
def get_virtual_machine(context):
  current_user = context['request'].user
  obj_list = []
  listing = False
  if current_user.is_superuser:
    obj_list = VIRTUAL_MACHINE.objects.all()
    if len(obj_list) > 0:
        listing = True
    content = { 'Title' : 'VIRTUAL_MACHINE' , 'obj_list' : obj_list , 'listing' : listing}
  else:
    if current_user.is_authenticated:
      obj_list = VIRTUAL_MACHINE.objects.filter(user=current_user)
      if len(obj_list) > 0:
          listing = True
      content = { 'Title' : 'VIRTUAL_MACHINE' , 'obj_list' : VIRTUAL_MACHINE.objects.filter(user=current_user) , 'listing' : listing }
    else:
      content = { 'Title' : 'VIRTUAL_MACHINE' , 'obj_list' : [] , 'listing' : listing }
  return mark_safe(render_to_string('General/TAG_TPL/list_tag.html' , content ))


@register.simple_tag(takes_context=True)
def render_field(context,field,field2=False):
    content = { 'field' : field }
    type = field.field.widget.input_type
    call = ''
    csrf_token = ''
    form_id = ''
    try:
        call = context['call']
        csrf_token = context['csrf_token']
        form_id = context['form_id']
    except KeyError:
        pass
    print(type ,field.label )
    content = { 'field' : field , 'call' : call , 'csrf_token' : csrf_token , 'form_id' : form_id }
    if type == 'checkbox':
        return mark_safe(render_to_string('General/TAG_TPL/Field/default_checkbox.html' , content ))
    if type == 'range':
        return mark_safe(render_to_string('General/TAG_TPL/Field/Number_Slider.html' , content ))
    if type == 'number':
        return mark_safe(render_to_string('General/TAG_TPL/Field/Number_PM.html' , content ))
    if type == 'select':
        if field2:
            content.update( { 'field2' : field2 } )
            return mark_safe(render_to_string('General/TAG_TPL/Field/default_select_field_to_field.html' , content ))
        return mark_safe(render_to_string('General/TAG_TPL/Field/default_select.html' , content ))
    return mark_safe(render_to_string('General/TAG_TPL/Field/default.html' , content ))

@register.simple_tag(takes_context=True)
def get_cart_saved(context):
    try:
      content = {}
      cart = context['request'].session['saved']
      total = context['request'].session['total']
      content.update({ 'cart' :  cart , 'total' : total })
      return mark_safe(render_to_string('General/TAG_TPL/cart_tag.html' , content ))
    except Exception as e:
      content = { 'MSG' : 'You Have no item in you cart' }
      return mark_safe(render_to_string('General/TAG_TPL/no_cart_tag.html' , content ))

@register.simple_tag(takes_context=True)
def get_cart_js(context):
      content = {}
      return mark_safe(render_to_string('General/TAG_TPL/JS/cart_js.html' , content ))
