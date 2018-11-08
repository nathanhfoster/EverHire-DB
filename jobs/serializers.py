from rest_framework import serializers
from jobs.models import Job
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','title', 'slug', 'author', 'author_username', 'html', 'tags',
        'date_created','last_modified', 'last_modified_by', 'last_modified_by_username', 'views'
        )
        read_only_fields = ('date_created', 'date_modified, last_modified,last_modified_by')