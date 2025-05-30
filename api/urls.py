from django.urls import path
from .views import PatientView, DoctorView, MappingView, AdminRegisterView, AdminManageView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin_register/', AdminRegisterView.as_view(), name="admin_register"),
    path('admins/<int:id>/', AdminManageView.as_view(), name="admin_manage"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('patients/', PatientView.as_view()), 
    path('patients/<int:id>/', PatientView.as_view()), 

    path('doctors/', DoctorView.as_view()), 
    path('doctors/<int:id>/', DoctorView.as_view()), 
    
    path('mappings/', MappingView.as_view()),
    path('mappings/<int:id>/', MappingView.as_view()),
]