from django import forms
from django.forms import ModelForm

from .models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from .json_import import set_session



class TIME_MANAGEMENT_Form(forms.ModelForm):
  class Meta:
    model = TIME_MANAGEMENT
    fields = (
    'scheduled_date',
    'time_scheduled',
    'subject',
    'description',
    'creator',
    )

  def get_field(self,request=False):
      if request:
        return set_session(self,request,'TIME_MANAGEMENT')
      else:
        return { 'success' : False }


class EXCHANGE_Form(forms.ModelForm):
  class Meta:
    model = EXCHANGE
    fields = (
	'business_type',
    'business_name',
    'mailbox',
    'office_license',
    'current_email_provider',
    'number_of_employees',
	'average_size_of_mailbox',
	'migration_required',
    )

  def get_field(self,request=False):
      if request:
        return set_session(self,request,'EXCHANGE')
      else:
        return { 'success' : False }


class VOIP_Form(forms.ModelForm):
  class Meta:
    model = VOIP
    fields = (
	'business_type',
    'business_name',
    'extension',
    'locations',
    'did_existing_local_number',
    'did_new_local_number',
    'fax_numbers',
    'current_phone_provider',
    'number_of_employees',
    'tfs_existing_toll_free_numbers',
    'tfs_new_toll_free_numbers',
    )

  def get_field(self,request=False):
      if request:
        return set_session(self,request,'VOIP')
      else:
        return { 'success' : False }


class VIRTUAL_MACHINE_Form(forms.ModelForm):
  class Meta:
    model = VIRTUAL_MACHINE
    fields = (
	'datacenter',
	'operating_system',
	'system_disk',
	'data_disk',
    'network_throughput',
	'memory',
	'vcpu',
    'quickbooks',
    'sage',
    'sapbusinessone',
    'webrootsecurityendpoint',
    'cylanceaiendpointprotection',
    'officestandard',
    'businesshoursmfest',
    'monsunest',
    )

  def get_field(self,request=False):
      if request:
        return set_session(self,request,'VIRTUAL_MACHINE')
      else:
        return { 'success' : False }






class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2', )

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'first_name','last_name')