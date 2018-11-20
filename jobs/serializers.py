from rest_framework import serializers
from jobs.models import Job
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'address', 'title', 'description', 'lat', 'lng', 'phone_number', 'author', 'author_username', 'tags',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'status', 'worker'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')