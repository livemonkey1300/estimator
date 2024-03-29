from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE
from .forms import TIME_MANAGEMENT_Form ,EXCHANGE_Form ,VOIP_Form ,VIRTUAL_MACHINE_Form , MAILME , VOIP_Extend_Form , DATA_DISK_Form , VIRTUAL_MACHINE_Instance_Form , SYSTEM_DISK_Form
from .forms import Applications_Form , Management_Form

from .json_import import update_session , get_price , get_extended , set_rebate
from .mail_quote  import Mailer
from .ajax_session import AJAX as ajax
from .ajax_session import FORM_INIT

def index(request):
  context = {}
  context.update({ 'time_management' : { 'item' : TIME_MANAGEMENT.objects.all() }})
  context.update({ 'exchange' : { 'item' : EXCHANGE.objects.all() }})
  context.update({ 'voip' : { 'item' : VOIP.objects.all() }})
  context.update({ 'virtual_machine' : { 'item' : VIRTUAL_MACHINE.objects.all() }})
  return render(request, 'General/Main.html', context )

def flush_save(request):
    request.session.modified = True
    request.session.pop('saved', None)
    request.session['total'] = 0
    content = { 'MSG' : 'You Have no item in you cart' }
    return render( request, 'General/TAG_TPL/no_cart_tag.html'  , content )

def show_email(request):
    cart = request.session['saved']
    total = request.session['total']
    flush = reverse('General:flush')
    form = MAILME()
    return render(request, 'General/Main/mail.html', { 'quote' : cart  ,  'mail_form' : form , 'flush' : flush , 'total' :  total })



def mail_form(request,contact=False):
    form = FORM_INIT(request,default_post_url='mail_form')
    form.add_form(MAILME,context_name='mail_form',template_name='mail_form')
    context = form.get_form()
    if form.valid:
        mail_form = Mailer(request,context['ref_mail_form'])
        mail_form.send()
        if contact:
            mail_form.send_admin()
    return render(request,  'General/Main/mail_form.html', context )

# Email quote
def send_email(request):
    cart = request.session['saved']
    total = request.session['total']
    flush = reverse('General:flush')
    return render(request, 'General/Main/mail.html', { 'quote' : cart , 'flush' : flush , 'total' :  total })


def discount(request,form_name='VOIP'):
    return HttpResponse(json.dumps(set_rebate(request,form_name)), content_type="application/json")


def create_time_management(request):
    flush = reverse('General:flush')
    location = reverse('General:create_time_management')
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    context = { 'APP' : 'TIME_MANAGEMENT' }
    if request.method == 'POST':
        form_request = TIME_MANAGEMENT_Form(request.POST)
        form = form_request.get_field(request)
        if form['redirect']:
          if form['mail']:
            context.update( { 'quote' : form['mail_data'] , 'flush' : flush , 'total' :  get_price(request,'TIME_MANAGEMENT') } )
            return render(request, 'General/Main/mail.html', context )
          else:
            return redirect('General:index')
        else:
          context.update( {'form': form['form'] , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  })
          return render(request, 'General/form.html', context )
    else:
        try:
          session = request.session['tmp']['TIME_MANAGEMENT']
          form_request = TIME_MANAGEMENT_Form(initial=session)
        except KeyError:
          form_request = TIME_MANAGEMENT_Form()
        form = form_request.get_field(request)
        context.update( {'form': form['form'] , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  } )
        return render(request, 'General/form.html', context )


def edit_time_management(request,pk):
  if request.user.is_authenticated:
    time_management_instance = get_object_or_404(TIME_MANAGEMENT, pk=pk)
    if request.method == 'POST':
        form = TIME_MANAGEMENT_Form(request.POST,instance=time_management_instance)
        form.get_field(request)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = TIME_MANAGEMENT_Form(instance=time_management_instance)
        form.get_field(request)
    location = reverse('General:edit_time_management' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  } )
  else:
    return redirect('General:index')


def create_exchange(request):
    flush = reverse('General:flush')
    location = reverse('General:create_exchange')
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    context = { 'APP' : 'EXCHANGE' }
    if request.method == 'POST':
        form_request = EXCHANGE_Form(request.POST)
        form = form_request.get_field(request)
        if form['redirect']:
          if form['mail']:
            context.update( { 'quote' : form['mail_data'] , 'flush' : flush , 'total' :  get_price(request,'EXCHANGE') } )
            return render(request, 'General/Main/mail.html', context )
          else:
            return redirect('General:index')
        else:
          context.update( {'form': form['form'] , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  })
          return render(request, 'General/form.html', context )
    else:
        try:
          session = request.session['tmp']['EXCHANGE']
          form_request = EXCHANGE_Form(initial=session)
        except KeyError:
          form_request = EXCHANGE_Form()
        form = form_request.get_field(request)
        context.update( {'form': form['form'] , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  } )
        return render(request, 'General/form.html', context )


def edit_exchange(request,pk):
  if request.user.is_authenticated:
    exchange_instance = get_object_or_404(EXCHANGE, pk=pk)
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST,instance=exchange_instance)
        form.get_field(request)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = EXCHANGE_Form(instance=exchange_instance)
        form.get_field(request)
    location = reverse('General:edit_exchange' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  } )
  else:
    return redirect('General:index')


def create_voip(request,extend=False):
    context = { 'APP' : 'VOIP' }
    ajax_handler = ajax(request,'VOIP',VOIP_Form)
    if request.method == 'POST':
        if extend:
            ajax_handler.add_form_init_session(VOIP_Extend_Form)
        else:
            ajax_handler.init_form_session()
        validation = ajax_handler.get_estimate_context('create_voip')
        if validation['valid']:
          context.update( validation['context'] )
          return render(request, 'General/Main/mail.html', context )
        else:
          return redirect('General:index')
    else:
        ajax_handler.add_form_init_session(VOIP_Form)
        context.update(ajax_handler.get_context('create_voip'))
        context.update({'VOIP_FORM' : ajax_handler.get_render_initial_form('create_voip','inititial_card_form.html',sub_form_url='create_voip_extend')})
        return render(request, 'General/voip_calc.html', context )

def create_voip_extend(request):
    return ajax(request,'VOIP',VOIP_Extend_Form,start_form=True).get_render_extended('create_voip_extend')

def edit_voip(request,pk):
  if request.user.is_authenticated:
    voip_instance = get_object_or_404(VOIP, pk=pk)
    if request.method == 'POST':
        form = VOIP_Form(request.POST,instance=voip_instance)
        form.get_field(request)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VOIP_Form(instance=voip_instance)
        form.get_field(request)
    location = reverse('General:edit_voip' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VOIP' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VOIP')  } )
  else:
    return redirect('General:index')


def create_virtual_machine(request):
    context = { 'APP' : 'VIRTUAL_MACHINE' }
    ajax_handler = ajax(request,'VIRTUAL_MACHINE',VIRTUAL_MACHINE_Form)
    ajax_handler.add_form(DATA_DISK_Form)
    ajax_handler.add_form(VIRTUAL_MACHINE_Instance_Form)
    ajax_handler.add_form(SYSTEM_DISK_Form)
    ajax_handler.add_form(Applications_Form)
    ajax_handler.add_form(Management_Form)
    if request.method == 'POST':
        ajax_handler.init_form_session()
        validation = ajax_handler.get_estimate_context('create_virtual_machine')
        if validation['valid']:
          context.update( validation['context'] )
          return render(request, 'General/Main/mail.html', context )
        else:
          return redirect('General:index')
    else:
        ajax_handler.add_form_init_session(VIRTUAL_MACHINE_Form)
        context.update(ajax_handler.get_context('create_virtual_machine'))
        context.update({'VM_FORM' : ajax_handler.get_render_small_form('create_virtual_machine')})
        context.update({'DATA_DISK' : ajax_handler.get_render_small_form('create_virtual_machine','disk_type.html',form_id=1)})
        context.update({'Instance_Type' : ajax_handler.get_render_small_form('create_virtual_machine','Instance_Type.html',form_id=2)})
        context.update({'SYSTEM_DISK' : ajax_handler.get_render_small_form('create_virtual_machine','system_disk_type.html',form_id=3)})
        context.update({'Applications' : ajax_handler.get_render_small_form('create_virtual_machine','extend_app.html',form_id=4)})
        context.update({'Management' : ajax_handler.get_render_small_form('create_virtual_machine','extend_managed.html',form_id=5)})
        return render(request, 'General/vm_calc.html', context )



def edit_virtual_machine(request,pk):
  if request.user.is_authenticated:
    virtual_machine_instance = get_object_or_404(VIRTUAL_MACHINE, pk=pk)
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST,instance=virtual_machine_instance)
        form.get_field(request)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VIRTUAL_MACHINE_Form(instance=virtual_machine_instance)
        form.get_field(request)
    location = reverse('General:edit_virtual_machine' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VIRTUAL_MACHINE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VIRTUAL_MACHINE')  } )
  else:
    return redirect('General:index')




def ajax_call(request,form_name=False,field=False,field2=False):
    updates = ajax(request,form_name)
    updates.set_current_field_session(field)
    if field2:
        updates.set_current_field_session(field2)
    return HttpResponse(json.dumps(updates.get_session_updated_json()), content_type="application/json")
