from importlib.metadata import requires
from pyexpat import model
from rest_framework.authtoken.models import Token
from .models import ContactUs, Post, Userprofile,likes,Comments,Messages,PlogPost,PlogPostComments

from rest_framework import serializers
from .models import User


class UpdatepassSerializer(serializers.Serializer):
    oldPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['id','user',"address","phone","avatar"]
    

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', "first_name","last_name","email","password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user_token = Token.objects.create(user=user)
        return user




class postSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Post
        fields= ['id','user',"title","dis",'image']
                

        
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = likes
        fields = ['id',"user","post","like"]
          

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id',"user","comment"]
          
class postSerializer(serializers.ModelSerializer):
    class Meta:
        my_like = LikesSerializer()
        my_comments = CommentsSerializer()
        model = Post
        fields= ['id','user',"title","dis",'image',"my_like","my_comments"]
                
        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Messages
        fields= ['id','sender',"reciver","message"]


class PlogPostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PlogPost
        fields= ['id','user',"title", "image","content"]


class PlogPostCommentsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PlogPostComments
        fields= ['id','plogPost',"user","comment"]
    

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ContactUs
        fields= ['id','emailAddress',"title","subject"]

  