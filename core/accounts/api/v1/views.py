from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegistrationSerializer,CustomAuthTokenSerializer,ProfileSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.views import ObtainAuthToken

User = get_user_model()

class RegisterViewToken(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            data={"email":email,"token":token,"id":user_obj.id}
            return Response(data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    
class ProfileViewToken(TokenObtainPairView):
    serializer_class = ProfileSerializer    

class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user_id': user.pk,
        'email': user.email
        })
    
# class ChangePasswordView(generics.GenericAPIView):
#     model= 
#     serializer_class = 
#     permission_classes= 
#     def post()