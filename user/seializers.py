from pyexpat import model
from rest_framework.authtoken.models import Token
from .models import Post, Userprofile,likes,Pokes,Comments,Messages

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "first_name","last_name","email","password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user_token = Token.objects.create(user=user)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['id',"user","address","phone","profisional","avatar"]
    



class postSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Post
        fields= ['id','user',"title","dis",'location','image',"time"]
                

        
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = likes
        fields = ['id',"user","post","like"]
          
class PokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokes
        fields = ['id',"user","post","poke"]
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id',"user","comment"]
          
class postSerializer(serializers.ModelSerializer):
    class Meta:
        my_like = LikesSerializer()
        my_poke = PokesSerializer()
        my_comments = CommentsSerializer()
        
        model = Post
        fields= ['id','user',"title","dis",'location','image',"time","my_like","my_poke","my_comments"]
                
        
class MessagesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Messages
        fields= ['id','sender',"reciver","message"]
    
