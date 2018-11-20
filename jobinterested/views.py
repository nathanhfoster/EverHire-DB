from .models import Jobinterested
from django.shortcuts import render
from jobs.models import Job
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import JobInterestedSerializer

class JobinterestedView:
	serializer_class = JobInterestedSerializer