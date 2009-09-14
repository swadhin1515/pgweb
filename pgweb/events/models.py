from django.db import models
from django.contrib.auth.models import User
from datetime import date
from pgweb.util.bases import PgModel

from core.models import Country

class Event(models.Model, PgModel):
	submitter = models.ForeignKey(User, null=False, blank=False)
	approved = models.BooleanField(null=False, blank=False, default=False)

	org = models.CharField(max_length=50, null=False, blank=False)
	title = models.CharField(max_length=100, null=False, blank=False)
	city = models.CharField(max_length=50, null=False, blank=False)
	state = models.CharField(max_length=50, null=False, blank=True)	
	country = models.ForeignKey(Country, null=False, blank=False)
	
	training = models.BooleanField(null=False, blank=False, default=False)
	startdate = models.DateField(null=False, blank=False)
	enddate = models.DateField(null=False, blank=False)
	
	summary = models.TextField(blank=False, null=False)
	details = models.TextField(blank=False, null=False)
	
	send_notification = True
	
	def __unicode__(self):
		return "%s: %s" % (self.startdate, self.title)

	@property
	def displaydate(self):
		if self.startdate == self.enddate:
			return self.startdate
		else:
			return "%s &ndash; %s" % (self.startdate, self.enddate)
	
	@property
	def locationstring(self):
		#FIXME, deal with state etc
		return "%s, %s" % (self.city, self.country)

	class Meta:
		ordering = ('startdate',)

