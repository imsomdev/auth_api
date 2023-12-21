from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login',views.login),
    path('signup',views.signup),
    path('test_token',views.test_token)

]