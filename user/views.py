from django.shortcuts import render
from .seializers import UserSerializer,UserProfileSerializer,postSerializer,LikesSerializer,PokesSerializer,CommentsSerializer,MessagesSerializer
from .models import User,Userprofile,Post,likes,Pokes,Comments,Messages
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserProfileViews(viewsets.ModelViewSet):
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer

class PostViews(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postSerializer

class LikeViews(viewsets.ModelViewSet):
    queryset = likes.objects.all()
    serializer_class = LikesSerializer

class PokeViews(viewsets.ModelViewSet):
    queryset = Pokes.objects.all()
    serializer_class = PokesSerializer

class CommentsViews(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class MessageViews(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
