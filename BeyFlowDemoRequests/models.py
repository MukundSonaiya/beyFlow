from __future__ import unicode_literals
from django.db import models

class DemoRequest(models.Model):
	demoRequestId	= models.AutoField(primary_key=True, db_column="demo_request_id")
	firstName 		= models.CharField("First name", db_column="first_name",max_length=25, blank = False, null=False)
	lastName 		= models.CharField("Last name", db_column="last_name",max_length=25, blank = False, null=False)
	email 			= models.CharField("Email", db_column="email",max_length=100, blank = False, null=False)
	jobTitle 		= models.CharField("Job title", db_column="job_title",max_length=30, blank = True, null=True)
	workPhoneNumber = models.CharField("Work phone number", db_column="work_phone_number",max_length=15, blank = True, null=True)
	company 		= models.CharField("Company", db_column="company",max_length=60, blank = True, null=True)
	message 		= models.TextField("Message", db_column="message",max_length=5000, blank = False, null=False)
	canReceiveMails = models.BooleanField("Can receive mails", db_column="can_receive_mails", default= False)
	demoRequestCreatedDate = models.DateField(auto_now = False, auto_now_add=True, db_column="demo_request_created_date")
	demoRequestUpdatedDate = models.DateField(auto_now = True, auto_now_add=False, db_column="demo_request_updated_date")

	def __str__(self):
		return str(self.demoRequestId)

	def __unicode__(self):
		return str(self.demoRequestId)

