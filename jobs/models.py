from django.db import models
from django.conf import settings

class Job(models.Model):
    address = models.CharField(null=True, blank=False, max_length=250)
    image = models.TextField(blank=True)
    title = models.CharField(null=True, blank=False, max_length=250)
    description = models.TextField(null=True, blank=False)
    lat = models.DecimalField(max_digits=17, decimal_places=14)
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    phone_number = models.CharField(null=True, blank=False, max_length=12)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='jobAuthorName',
        on_delete=models.CASCADE,)
    def author_username(self):
        return self.author. get_username()
    author_username.short_description = 'Username' 
    tags = models.CharField(max_length=128, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='jobModifier',
        on_delete=models.CASCADE,)
    def last_modified_by_username(self):
        return self.last_modified_by. get_username()