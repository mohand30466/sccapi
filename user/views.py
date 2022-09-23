from django.shortcuts import render
from .seializers import  BussinesSerializer, BussinesStaffSerializer, ContactUsSerializer, HoursSerializer, ShiftSerializer, UserSerializer,UserProfileSerializer,postSerializer,LikesSerializer,PokesSerializer,CommentsSerializer,MessagesSerializer,PlogPostCommentsSerializer,PlogPostSerializer,UpdatepassSerializer
from .models import Bussines, BussinesStaff, ContactUs, HoursCard, Shift, User,Userprofile,Post,likes,Pokes,Comments,Messages,PlogPostComments,PlogPost
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


# Create your views here.
class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(methods=['PUT'], detail=True, serializer_class=UpdatepassSerializer)
    def ChangePass(self,request, pk):
        user = User.objects.get(pk=pk)
        serializer = UpdatepassSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get("oldPassword")):
                return Response({"message":"Password Dosnt Match"},status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(serializer.data.get("newPassword"))
            user.save()
            return Response({"message":"Password is update it"},status=status.HTTP_200_OK)        


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



class BussinessStaffViews(viewsets.ModelViewSet):
    queryset =BussinesStaff.objects.all()
    serializer_class = BussinesStaffSerializer

class ShiftViews(viewsets.ModelViewSet):
    queryset =Shift.objects.all()
    serializer_class = ShiftSerializer

class HoursViews(viewsets.ModelViewSet):
    queryset =HoursCard.objects.all()
    serializer_class = HoursSerializer
