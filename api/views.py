from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import generics, mixins, status 
from rest_framework.response import Response

from .models import User, Doctor, Patient, Mapping
from .serializers import UserSerializer, DoctorSerializer, PatientSerializer, MappingSerializer, UserRegisterSerializer

class AdminRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AdminManageView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    permission_classes = [IsAdminUser] # for ease of review only; this should be changed to superuser(whole project )

    queryset = User.objects.all()
    serializer_class = UserSerializer 
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        # user detail : if id is provided 
        id = kwargs.get('id') 
        if id:
            return self.retrieve(request, *args, kwargs)
        # user list : if no id is provided  
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({
                'Details': "id required to update a user."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({
                'Details': "id required to update a user."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PatientView(
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    permission_classes = [IsAdminUser]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        # user detail : if id is provided 
        id = kwargs.get('id') 
        if id:
            return self.retrieve(request, *args, kwargs)
        # user list : if no id is provided  
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({
                'Details': "id required to update a user."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({
                'Details': "id required to update a user."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({
                'Details': "id required to update a user."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.destroy(request, *args, **kwargs)


class DoctorView(
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    # authentications: defined in settings

    # permission: AdminOnly 
    permission_class = [IsAdminUser]

    # additional info
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

    # handlers 
    def get(self, request, *args, **kwargs):
        if kwargs.get("id"):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if not id:
            return Response({
                "details":"id is needed for updation."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args ,**kwargs)

    def patch(self, request, *args, **kwargs):
        if not id:
            return Response({
                "details":"id is needed for updation."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MappingView(
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    # authentication: defined in settings

    # permissions : Admin only 
    permission_classes = [IsAdminUser] 

    # additional info
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer 
    lookup_field = 'id'

    # handlers 
    def get(self, request, *args, **kwargs):
        if kwargs.get("id"):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if not id:
            return Response({
                "details":"id is needed for updation."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args ,**kwargs)

    def patch(self, request, *args, **kwargs):
        if not id:
            return Response({
                "details":"id is needed for updation."
            }, status=status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)