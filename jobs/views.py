from .models import Job
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializers import JobSerializer
from jobs.permissions import IsOwnerOrReadOnly, IsUpdateProfile

class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(JobView, self).get_permissions()