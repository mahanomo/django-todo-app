from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # jwt url
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # user registration
    path('registration/',views.RegisterViewToken.as_view(),name='registration'),
    # user profile
    path('profile/',views.ProfileViewToken.as_view(),name='profile'),
    # user login 
    path('login/',views.CustomAuthToken.as_view(),name='login'),
    # user logout
    # path('logout/',views.LogoutViewToken.as_view(),name='logout'),
    ]