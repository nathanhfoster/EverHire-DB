from rest_framework import serializers
from jobinterested.models import Jobinterested

class JobinterestedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobinterested
        fields = ('job', 'worker', 'date_created',)
        read_only_fields = ('date_created',)