from .models import User
from jobs.models import Job
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from jobs.serializers import JobSerializer
from user.permissions import IsUpdateProfile, IsStaffOrTargetUser


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):

        # allow an authenticated user to create via POST
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PATCH':
            self.permission_classes = (permissions.IsAuthenticated, IsUpdateProfile,)
        return super(UserView, self).get_permissions()


    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def myjobs(self, request):
        qs = Job.objects.all().filter(author=self.request.user).filter(status=0)
        serializer = JobSerializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[permission_classes])
    def mydonejobs(self, request):
        qs = Job.objects.all().filter(author=self.request.user).filter(status=-1)
        serializer = JobSerializer(qs, many=True)
        return Response(serializer.data)


