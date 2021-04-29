from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from auth.views import RegisterView, CheckInviteCodeView, CheckEmailExistsView

app_name = 'auth'

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', RegisterView.as_view(), name='register'),
    path('email/used', CheckEmailExistsView.as_view(), name='email_already_used'),
    path('invite/<code>', CheckInviteCodeView.as_view(), name='check_invite')
]
