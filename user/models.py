import email
from django.db import models
from django.contrib.auth import models as auth_models
import datetime



class UserManager(auth_models.BaseUserManager):
    
    def create_user(self, first_name:str,last_name:str, email:str,password:str=None,is_staff=False,is_superuser=False) -> "User":
        
        if not email:
            raise ValueError("user must have an email")
        if not first_name:
            raise ValueError("user must have first_name")
        if not last_name:
            raise ValueError("user must have last name")
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
        
    def create_superuser(self, first_name:str,last_name:str, email:str,password:str) -> "User":
        user = self.create_user(
            first_name= first_name,
            last_name= last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user
        
        
    
class User(auth_models.AbstractUser):
    first_name= models.CharField(verbose_name="first name", max_length=255)
    last_name= models.CharField(verbose_name="last name", max_length=255)
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    password= models.CharField(max_length=255, unique=False)
    username= None
    
    objects= UserManager()
    
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= ["first_name","last_name"]

  



def uploadto(instance,filename):
    return f"{instance.user}/{filename}"

class Post(models.Model):
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False)
    dis = models.CharField(max_length=550, blank=False)
    image = models.ImageField(upload_to=uploadto, default=False, blank= True)
    
    def __str__(self):
        return self.title
   
class Userprofile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE, default=True)
    address = models.CharField(max_length=255,blank=True)
    phone = models.CharField(max_length=255,blank=True)
    avatar = models.ImageField(upload_to=uploadto,default=True, blank=True)
    
    def __str__(self):
        return f"{self.user}+{self.avatar}"


class likes(models.Model):
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,default=True,related_name="my_like", on_delete=models.CASCADE)
    like = models.BooleanField(default=False, blank=False)
    
    
    def __str__(self):
        return f"{self.user}  like  {self.post}"
  
class Comments(models.Model):
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,default=True,related_name="my_comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=False)
    
    
    def __str__(self):
        return self.comment
        
        
class Messages(models.Model):
    sender = models.ForeignKey(User,default=True, related_name="sender", on_delete=models.CASCADE)
    reciver = models.ForeignKey(User,default=True,related_name="reciver", on_delete=models.CASCADE)
    message = models.TextField(max_length=555, blank=False)
   
    def __str__(self):
        return self.message
    
        
class PlogPost(models.Model):
    user = models.ForeignKey(User,default=True, related_name="writer", on_delete=models.CASCADE)
    title = models.CharField(max_length=250,blank=False)
    image = models.ImageField(upload_to=uploadto, default=False, blank= True)
    content = models.TextField(max_length=2000, blank=False)
    
    
    def __str__(self):
        return self.title
    

class PlogPostComments(models.Model):
    plogPost = models.ForeignKey(PlogPost,default=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User,default=True,related_name="user_coments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=False)
    
    
    def __str__(self):
        return self.comment

class ContactUs(models.Model):
    emailAddress =  models.EmailField(max_length=255,blank=False)
    title = models.CharField(max_length=255, blank=False)
    subject = models.TextField(max_length=2255, blank=False)
    
    
    def __str__(self):
        return self.title
