PRICE_TABLE = {
  'scheduled_date' :  { 'price' : 0.0 },
  'time_scheduled' :  { 'price' : 0.0 },
  'subject' :  { 'price' : 0.0 },
  'description' :  { 'price' : 0.0 },
  'creator' :  { 'price' : 0.0 },

  #Voip elements
  'number_of_employees' :  { 'price' : 10.0 },
  'phone_lines' :  { 'price' : 3.0 },
  'toll_free' :  { 'price' : 5.0 },
  'fax_numbers' :  { 'price' : 30.0 },


  'business_type' : {
  'Automotive' :  0.0 ,
  'Corporate' :  0.0 ,
  'Education' :  0.0 ,
  'Healthcare' :  0.0 ,
  'Hospitality' :  0.0 ,
  'Manufacturing' :  0.0 ,
  'Technology' :  0.0 ,
},
  'business_name' :  { 'price' : 0.0 },
  'mailbox' :  { 'price' : 3.0 },
  'office_license' :  { 'price' : 1.5 },
  'current_email_provider' :  { 'price' : 0.0 },
  'number_of_employees' :  { 'price' : 0.0 },
  'average_size_of_mailbox' : {
  '5 GB' :  3.0 ,
  '10 GB' :  5.0 ,
  '25 GB' :  7.0 ,
  '50 GB' :  8.0 ,
  '75 GB' :  10.0 ,
},
  'migration_required' : {
  'No' :  0.0 ,
  'Yes' :  10.0 ,
},

  'business_type' : {
  'Automotive' :  0.0 ,
  'Corporate' :  0.0 ,
  'Education' :  0.0 ,
  'Healthcare' :  0.0 ,
  'Hospitality' :  0.0 ,
  'Manufacturing' :  0.0 ,
  'Technology' :  0.0 ,
},
  'business_name' :  { 'price' : 0.0 },
  'extension' :  { 'price' : 5.0 },
  'locations' :  { 'price' : 0.0 },
  'did_existing_local_number' :  { 'price' : 2.0 },
  'did_new_local_number' :  { 'price' : 2.0 },
  'current_phone_provider' :  { 'price' : 0.0 },
  'tfs_existing_toll_free_numbers' :  { 'price' : 5.0 },
  'tfs_new_toll_free_numbers' :  { 'price' : 5.0 },

  'datacenter' : {
  'Brasilia, Brasil' :  0.0 ,
  'Canada/Eastern' :  0.0 ,
  'Los Angeles, CA' :  0.0 ,
  'Mexico City, MX' :  0.0 ,
  'Miami, FL' :  0.0 ,
  'Ottawa, ON' :  0.0 ,
  'Paris, France' :  0.0 ,
  'Vancouver, BC' :  0.0 ,
},
  'operating_system' : {
  'Debian' :  25.0 ,
  'Ubuntu' :  30.0 ,
  'OpenSUSE' :  35.0 ,
  'CentOS' :  40.0 ,
  'SUSE Linux' :  45.0 ,
  'Windows Server' :  75.0 ,
},
  'system_disk' : {
  'SSD ENT Disk' :  0.3 ,
  'HDD SAS Disk' :  5.0 ,
},
  'data_disk' : {
  'SSD ENT Disk' :  0.3 ,
  'HDD SAS Disk' :  5.0 ,
},
  'network_throughput' :  { 'price' : 0.7 },
  'memory' : {
  '2 GB' :  15.0 ,
  '4 GB' :  25.0 ,
  '6 GB' :  35.0 ,
  '8 GB' :  60.0 ,
  '10 GB' :  80.0 ,
  '12 GB' :  100.0 ,
  '14 GB' :  110.0 ,
  '16 GB' :  125.0 ,
  '18 GB' :  135.0 ,
  '20 GB' :  155.0 ,
  '22 GB' :  170.0 ,
  '24 GB' :  190.0 ,
  '26 GB' :  205.0 ,
  '28 GB' :  215.0 ,
  '30 GB' :  225.0 ,
  '32 GB' :  255.0 ,
},
  'vcpu' : {
  '2 vCPU' :  20.0 ,
  '4 vCPU' :  30.0 ,
  '6 vCPU' :  45.0 ,
},
  'quickbooks' :  { 'price' :  0.0  },
  'sage' :  { 'price' :  0.0  },
  'sapbusinessone' :  { 'price' :  0.0  },
  'webrootsecurityendpoint' :  { 'price' :  5.0  },
  'cylanceaiendpointprotection' :  { 'price' :  10.0  },
  'officestandard' :  { 'price' :  25.0  },
  'businesshoursmfest' :  { 'price' :  50.0  },
  'monsunest' :  { 'price' :  90.0  },

}




BUSINESS_TYPE_CHOICE = (
  ( 'Automotive' , 'Automotive' ),
  ( 'Corporate' , 'Corporate' ),
  ( 'Education' , 'Education' ),
  ( 'Healthcare' , 'Healthcare' ),
  ( 'Hospitality' , 'Hospitality' ),
  ( 'Manufacturing' , 'Manufacturing' ),
  ( 'Technology' , 'Technology' ),
  )

  
AVERAGE_SIZE_OF_MAILBOX_CHOICE = (
  ( '5 GB' , '5 GB' ),
  ( '10 GB' , '10 GB' ),
  ( '25 GB' , '25 GB' ),
  ( '50 GB' , '50 GB' ),
  ( '75 GB' , '75 GB' ),
  )

  
MIGRATION_REQUIRED_CHOICE = (
  ( 'No' , 'No' ),
  ( 'Yes' , 'Yes' ),
  )

  

BUSINESS_TYPE_CHOICE = (
  ( 'Automotive' , 'Automotive' ),
  ( 'Corporate' , 'Corporate' ),
  ( 'Education' , 'Education' ),
  ( 'Healthcare' , 'Healthcare' ),
  ( 'Hospitality' , 'Hospitality' ),
  ( 'Manufacturing' , 'Manufacturing' ),
  ( 'Technology' , 'Technology' ),
  )

  

DATACENTER_CHOICE = (
  ( 'Brasilia, Brasil' , 'Brasilia, Brasil' ),
  ( 'Canada/Eastern' , 'Canada/Eastern' ),
  ( 'Los Angeles, CA' , 'Los Angeles, CA' ),
  ( 'Mexico City, MX' , 'Mexico City, MX' ),
  ( 'Miami, FL' , 'Miami, FL' ),
  ( 'Ottawa, ON' , 'Ottawa, ON' ),
  ( 'Paris, France' , 'Paris, France' ),
  ( 'Vancouver, BC' , 'Vancouver, BC' ),
  )

  
OPERATING_SYSTEM_CHOICE = (
  ( 'Debian' , 'Debian' ),
  ( 'Ubuntu' , 'Ubuntu' ),
  ( 'OpenSUSE' , 'OpenSUSE' ),
  ( 'CentOS' , 'CentOS' ),
  ( 'SUSE Linux' , 'SUSE Linux' ),
  ( 'Windows Server' , 'Windows Server' ),
  )

  
SYSTEM_DISK_CHOICE = (
  ( 'SSD ENT Disk' , 'SSD ENT Disk' ),
  ( 'HDD SAS Disk' , 'HDD SAS Disk' ),
  )

  
DATA_DISK_CHOICE = (
  ( 'SSD ENT Disk' , 'SSD ENT Disk' ),
  ( 'HDD SAS Disk' , 'HDD SAS Disk' ),
  )

  
MEMORY_CHOICE = (
  ( '2 GB' , '2 GB' ),
  ( '4 GB' , '4 GB' ),
  ( '6 GB' , '6 GB' ),
  ( '8 GB' , '8 GB' ),
  ( '10 GB' , '10 GB' ),
  ( '12 GB' , '12 GB' ),
  ( '14 GB' , '14 GB' ),
  ( '16 GB' , '16 GB' ),
  ( '18 GB' , '18 GB' ),
  ( '20 GB' , '20 GB' ),
  ( '22 GB' , '22 GB' ),
  ( '24 GB' , '24 GB' ),
  ( '26 GB' , '26 GB' ),
  ( '28 GB' , '28 GB' ),
  ( '30 GB' , '30 GB' ),
  ( '32 GB' , '32 GB' ),
  )

  
VCPU_CHOICE = (
  ( '2 vCPU' , '2 vCPU' ),
  ( '4 vCPU' , '4 vCPU' ),
  ( '6 vCPU' , '6 vCPU' ),
  )

  
  
  





def init_session(request,form_name=False,field=False):
    request.session.modified = True
    field_Name = field['name']
    field_data = field['initial']
    field_type = field['type']
    price = 0
    current = 0
    try:
        session = request.session[form_name]
    except KeyError:
        request.session[form_name] = {}
        session = request.session[form_name]
    try:
        price = float(PRICE_TABLE[field_Name]['price'])
    except KeyError:
        try:
            price = float(PRICE_TABLE[field_Name][field_data])
        except KeyError:
            price = float(0.0)
    try:
         current = float(field_data) *  price
    except Exception as e:
         current = price *  1
    value = field_data
    if field_type == 'checkbox':
        if field_data:
            value = 'on,'
        else:
            value = ''
    try:
        session[field_Name] = { 'price' : price , 'value' : value , 'current' : current }
    except KeyError:
        session[field_Name] = { 'price' : price , 'value' : value , 'current' : current }
    return { 'field' : field_Name , 'data' : session[field_Name] }


def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total


def get_total(request):
  total = 0
  cart = request.session['saved']
  for i in cart:
      tmp_key = list(i.keys())[0]
      try:
          total += i[tmp_key]['total']
      except Exception as e:
          pass
  request.session['total'] = total

def tmp_session(request,form_name,current_form):
    try:
      request.session['tmp'][form_name] = current_form
    except KeyError:
      request.session['tmp'] = { form_name : current_form }

def set_session(form_reference , request=False,form_name=False):
    fields = []
    current_user = request.user
    if request.method == 'POST':
      if form_reference.is_valid():
        current_form = form_reference.cleaned_data
        current_fields = {}
        current_fields_print = {}
        for key , value in current_form.items():
          field = { 'initial' : value , 'name' : key , 'type' : form_reference.fields[key].widget.input_type }
          ajax = init_session(request,form_name,field)
          current_fields[key] = value
          current_fields_print[key] = { 'value' : value , 'data' : ajax['data'] , 'nice_name' : form_reference.fields[key].label }
        try:
            cache = request.session['saved']
            cache.append({ form_name : { 'post' : current_fields , 'data' : current_fields_print , 'total' : get_price(request,form_name) } })
            get_total(request)
            tmp_session(request,form_name,current_form)
        except Exception as e:
            request.session['saved'] = [ { form_name : { 'post' : current_fields , 'data' : current_fields_print ,  'total' : get_price(request,form_name) }} ]
            get_total(request)
            tmp_session(request,form_name,current_form)
        if current_user.is_authenticated:
            form_reference.save()
            return { 'redirect' : True , 'mail' : False }
        else:
            return { 'redirect' : True , 'mail' : True , 'mail_data' : request.session['saved'] }
      else:
        if current_user.is_authenticated:
            return { 'form' : form_reference , 'redirect' : False , 'mail' : False }
        return { 'form' : form_reference , 'redirect' : False }
    else:
      for item in form_reference.fields.items():
          field = { 'initial' : item[1].initial , 'name' : item[0] , 'type' : item[1].widget.input_type }
          try:
              init_session(request,form_name,field)
          except Exception as e:
              pass
          fields.append(field)
    return { 'form' : form_reference , 'redirect' : False }


def update_session(request,form_name=False,field=False):
    remove = False
    if request.method == 'POST' and field and form_name :
      request.session.modified = True
      session = ''
      try:
          session = request.session[form_name]
      except KeyError:
          request.session[form_name] = {}
          session = request.session[form_name]
      try :
        if session[field]['value'] == 'on,':
            remove = True
        session[field]['value'] = request.POST.get(field)
        try:
            if not remove:
                session[field]['price'] = PRICE_TABLE[field][session[field]['value']]
            else:
                session[field]['price'] = 0
        except KeyError:
            try:
                session[field]['price'] = PRICE_TABLE[field]['price']
            except KeyError:
                pass
      except KeyError:
          session[field] = {}
          session[field]['value'] = request.POST.get(field)
          try:
              session[field]['price'] = PRICE_TABLE[field][session[field]['value']]
          except KeyError:
              try:
                  session[field]['price'] = PRICE_TABLE[field]['price']
              except KeyError:
                  session[field]['price'] = 0
          session[field]['current'] = 0
      try:
         session[field]['current'] = float(session[field]['value']) *  session[field]['price']
      except Exception as e:
         session[field]['current'] = session[field]['price'] *  1
    return { 'success' : True , 'field' : session[field]['value'] , 'price' : session[field]['price'] , 'current' : session[field]['current'] , 'total'  : get_price(request,form_name) }