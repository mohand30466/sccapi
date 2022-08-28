from pyexpat import model
from rest_framework.authtoken.models import Token
from .models import Bussines, BussinesManager, BussinesStaff, ContactUs, HoursCard, Post, Shift, Userprofile,likes,Pokes,Comments,Messages,PlogPost,PlogPostComments

from rest_framework import serializers
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['id','user',"address","phone","profisional","avatar"]
    

class UserSerializer(serializers.ModelSerializer):
    
    #profile = UserProfileSerializer()
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

    
class BussinesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bussines
        fields= ['id','user',"name","bussinessId","catogery","email","phone","locations","serviceTime"]
    
  
class BussinesManagerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BussinesManager
        fields= ['id','user',"bussiness"]
    
  
class BussinesStaffSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BussinesStaff
        fields= ['id',"bussines","name","staffId"]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Shift
        fields= ['id',"bussines","staff","shifts"]
    
class HoursSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HoursCard
        fields= ['id',"staff","shift","day","startAt","finishAt"]
    
  
    