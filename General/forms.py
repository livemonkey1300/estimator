from django import forms
from django.forms import ModelForm

from .models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from .json_import import set_session



class MAILME(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'your@email.com'}),required=True)
    tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),required=False)

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
      'number_of_employees',
      'phone_lines',
      'toll_free',
      'fax_numbers'
    )

    widgets = {
            'number_of_employees' : forms.NumberInput(attrs={'type': 'range' , 'min' : 1 , 'max' : 2000 }),
            'phone_lines' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 200 }),
            'toll_free' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 50 }),
            'fax_numbers' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 20 }),
    }

  def get_field(self,request=False):
      if request:
        return set_session(self,request,'VOIP')
      else:
        return { 'success' : False }

class VOIP_Extend_Form(forms.ModelForm):
  class Meta:
    model = VOIP
    fields = (
      'extension',
      'locations',
      'did_new_local_number',
      'current_phone_provider',
      'tfs_new_toll_free_numbers',
    )

    widgets = {
            'extension' : forms.NumberInput(attrs={'type': 'range' , 'min' : 1 , 'max' : 1000 }),
            'locations' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 100 }),
            'tfs_new_toll_free_numbers' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 50 }),
            'did_new_local_number' : forms.NumberInput(attrs={'type': 'range'  , 'min' : 1 , 'max' : 50 }),
    }

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
