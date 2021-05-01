from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import datetime
#from user import models as user_models
from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class Department(models.Model):
	title = models.CharField(max_length=100)
	def __str__(self):
		return self.title


class Position(models.Model):
	title = models.CharField(max_length=100)
	def __str__(self):
		return self.title

class employee(models.Model):
	name = models.CharField(max_length=100 , null=True)
	fname = models.CharField(max_length=100 , null=True)
	family = models.IntegerField()
	doj = models.DateField(("Date"), default=timezone.now())
	exp = models.IntegerField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: '03XXxxxxxxx'  Enter 11 Digits.")
	phone = models.CharField(validators=[phone_regex] , max_length=14 , default='' , null=True)
	cnic_regex = RegexValidator(regex=r'^^.{4}\+?1?\d{9,15}$', message="Format: 'xxxxxxxxxxxxx' Enter 13 Digits CNIC (Numbers only).")
	cnic = models.CharField(validators=[cnic_regex] , max_length=13 , default="" , null=True)
	address = models.CharField(max_length=250, null=True)
	position = models.ForeignKey('Position' , on_delete=models.CASCADE , default="" , null=True)
	dept = models.ForeignKey('Department' , on_delete=models.CASCADE , default="" , null=True)
	cv = models.FileField(upload_to='pics' , null=True , unique=True)
	ppic = models.ImageField(upload_to='pics' , null=True)
	matric =models.CharField(max_length=100, blank=True, default="", null=True)
	fsc = models.CharField(max_length=100, blank=True, default="", null=True)
	bs = models.CharField(max_length=100, blank=True, default="", null=True)
	ms= models.CharField(max_length=100, blank=True, default="", null=True)
	phd= models.CharField(max_length=100, blank=True, default="", null=True)
	lannual=60
	lsick=20
	lcasual=20
	def __str__(self):
		return '{} {} ({})'.format(self.position, self.name, self.dept) 
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["qs_json"] = json.dumps(list(Info.objects.values()))
		return context

# # Leave Khaata
# class Leave(models.Model):
	# choice = (
	# 	("Annual","Annual"),
	# 	("Sick","Sick"),
	# 	)
# 	employee = models.ForeignKey('employee' , on_delete= models.CASCADE , default="")
# 	lfrom = models.DateField()
# 	lto = models.DateField()
	# ltype = models.CharField(max_length=100 , choices=choice , default=1)
# 	days=models.IntegerField(default=0)
# 	reason = models.TextField()
# 	def __str__(self):
# 		return '{} {} {}'.format(self.position, self.dept, self.name) 

class eremove(object):
	"""docstring for dremove"""
	def __init__(self, arg):
		super(dremove, self).__init__()
		self.arg = arg

class LeaveType(models.Model):
	title=models.CharField(max_length=20 , default='')
	numbers=models.IntegerField()
	def __str__(self):
		return self.title
class Leave(models.Model):
	employee= models.ForeignKey(employee, on_delete=models.CASCADE , default="")
	type= models.ForeignKey(LeaveType, on_delete=models.CASCADE , default=0)
	from_date= models.DateField(default=datetime.date.today)
	to_date= models.DateField(default=datetime.date.today)
	reason= models.CharField(max_length=1200, default='')


# 

