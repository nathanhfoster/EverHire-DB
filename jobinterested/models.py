from django.db import models
from django.conf import settings
from jobs.models import Job

class Jobinterested(models.Model):
	job = models.ForeignKey(
		Job,
		related_name='jobInterested',
		on_delete=models.CASCADE,
		)
	worker = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
        related_name='jobInterestedWorker',
        on_delete=models.CASCADE,)
	date_created = models.DateTimeField(auto_now_add=True)
