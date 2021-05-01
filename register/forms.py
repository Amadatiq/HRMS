from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import employee , Department , Leave
from crispy_forms.helper import FormHelper

class DateInput(forms.DateInput):
	input_type= 'date'

class eaddform(forms.ModelForm):
	doj = forms.DateField(widget=DateInput)
	class Meta:
		model=employee
		fields = '__all__'
		labels = {
			'name':'Name',
			'family' : 'Family Members',
			'doj' : 'Date of Joining',
			'exp' : 'Experience',
			'phone':'Contact',
			'address':'Address',
			'position': 'Designation',
			'dept':'Department',
			'cv':'CV',
			'ppic':'Profile Picture',
			'cnic':'CNIC (Only 13 Digits)'
		}
	
class daddform(forms.ModelForm):
	class Meta:
		model=Department
		fields = '__all__'
		labels = {
			'title':'Department'
		}

class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)


		
	
class laddform(forms.ModelForm):
	from_date = forms.DateField(widget=DateInput)
	to_date = forms.DateField(widget=DateInput)
	name = employee.objects.values_list("name", flat=True).distinct()
	class Meta:
		model=Leave
		fields = '__all__'
		date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
		widgets = {
            'from_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'to_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }
		labels = {
			'name':'Employee',
			'type':'Type of Leave',
			'from_date':'From',
			'to_date':'To',
			'reason':'Reason',

		}
