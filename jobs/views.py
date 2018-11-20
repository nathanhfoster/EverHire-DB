from .models import Job
from jobinterested.models import Jobinterested
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import JobSerializer
from jobinterested.serializers import JobinterestedSerializers
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


    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def all(self, request):
        qs = Job.objects.all().filter(status=0)
        serializer = JobSerializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[permission_classes])
    def interested(self, request, pk):
        qs = Jobinterested.objects.all().filter(job=pk)
        serializer = JobinterestedSerializers(qs, many=True)
        return Response(serializer.data)

