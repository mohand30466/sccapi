from django.shortcuts import render
from .seializers import BussinesManagerSerializer, BussinesSerializer, BussinesStaffSerializer, ContactUsSerializer, UserSerializer,UserProfileSerializer,postSerializer,LikesSerializer,PokesSerializer,CommentsSerializer,MessagesSerializer,PlogPostCommentsSerializer,PlogPostSerializer
from .models import Bussines, BussinesManager, BussinesStaff, ContactUs, User,Userprofile,Post,likes,Pokes,Comments,Messages,PlogPostComments,PlogPost
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

class PlogPostViews(viewsets.ModelViewSet):
    queryset = PlogPost.objects.all()
    serializer_class = PlogPostSerializer

class PlogPostcommetsViews(viewsets.ModelViewSet):
    queryset = PlogPostComments.objects.all()
    serializer_class = PlogPostCommentsSerializer

class ContactUsViews(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class BussinessUsViews(viewsets.ModelViewSet):
    queryset = Bussines.objects.all()
    serializer_class = BussinesSerializer

class BussinessManagerViews(viewsets.ModelViewSet):
    queryset = BussinesManager.objects.all()
    serializer_class = BussinesManagerSerializer

class BussinessStaffViews(viewsets.ModelViewSet):
    queryset =BussinesStaff.objects.all()
    serializer_class = BussinesStaffSerializer

# class ShiftViews(viewsets.ModelViewSet):
#     queryset =Shift.objects.all()
#     serializer_class = ShiftSerializer
