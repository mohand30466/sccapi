from importlib.metadata import requires
from pyexpat import model
from rest_framework.authtoken.models import Token
from .models import Bussines,ToDoList,Invoice, BussinesStaff, ContactUs, HoursCard, Invoices, Post, Shift, Userprofile,likes,Pokes,Comments,Messages,PlogPost,PlogPostComments,Paysleeve

from rest_framework import serializers
from .models import User


class UpdatepassSerializer(serializers.Serializer):
    oldPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)


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
    
  

class BussinesStaffSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BussinesStaff
        fields= ['id',"bussines","name","staffId","job"]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Shift
        fields= ['id',"bussines","staff","shifts"]
    
class HoursSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HoursCard
        fields= ['id',"staff","shift","day","startAt","finishAt"]
    
  
    
class InvoicesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Invoices
        fields= ['id',"bussiness","invoiceType","issueAt","reciverName","reciverId","reciverEmail","invoiceDetail","invoiceAmount","invoiceTax","paymentTill"]
    
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Invoice
        fields= ['id',"bussiness","invoiceType","issueAt","reciverName","reciverId","reciverEmail","invoiceDetail","invoiceAmount","invoiceTax","paymentTill"]
    
  
    
    
class PaysleeveSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Paysleeve
        fields= ['id',"bussiness","startAt","month","name","visaId","regularHours","extraHours","weekendHours","transportations","hoursFee","tax","finalAmount"]
    
  
class ToDoListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ToDoList
        fields= ['id',"user","actions","time","isFinish"]
    
  
    