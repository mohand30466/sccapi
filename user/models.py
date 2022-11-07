import email
from django.db import models
from django.contrib.auth import models as auth_models
import datetime

# Create your models here.

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
    location = models.CharField(max_length=550, blank=False)
    image = models.ImageField(upload_to=uploadto, default=False, blank= True)
    time = models.DateTimeField()
    
    
    def __str__(self):
        return self.title
   
class Userprofile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE, default=True)
    address = models.CharField(max_length=255,blank=True)
    phone = models.CharField(max_length=255,blank=True)
    profisional = models.CharField(max_length=255,blank=True)
    avatar = models.ImageField(upload_to=uploadto,default=True, blank=True)
    
    def __str__(self):
        return f"{self.user}+{self.avatar}"


class likes(models.Model):
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,default=True,related_name="my_like", on_delete=models.CASCADE)
    like = models.BooleanField(default=False, blank=False)
    
    
    def __str__(self):
        return f"{self.user}  like  {self.post}"
  
class Pokes(models.Model):
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,default=True,related_name="my_poke", on_delete=models.CASCADE)
    poke = models.BooleanField(default=False, blank=False)
    
    
    def __str__(self):
        return f"{self.user}  poke  {self.post}"
        
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
    # createdAt=models.DateTimeField(auto_now_add=True)
    
    
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

class Bussines(models.Model):
    user = models.ForeignKey(User,default=True, related_name="owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    bussinessId = models.CharField(max_length=255, blank=True)
    catogery = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    locations = models.CharField(max_length=255, blank=True)
    serviceTime = models.TextField(max_length=2255, blank=True)
    
    
    def __str__(self):
        return self.name



class BussinesStaff(models.Model):
    bussines = models.ForeignKey(Bussines,default=True, related_name="busnessStaf", on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=False) 
    staffId = models.CharField(max_length=255,blank=False, unique=True) 
    job = models.CharField(max_length=255,blank=False, default=True) 
   
    def __str__(self):
        return f"{self.name}"



class Shift(models.Model):

    STATUS = (
       ('MOR', 'Morning'),
       ('EVE', 'Evening'),
   )   
    bussines = models.ForeignKey(Bussines,default=True, related_name="bussinesShift", on_delete=models.CASCADE)
    staff = models.ForeignKey(BussinesStaff,default=True, related_name="bussinesStaff", on_delete=models.CASCADE)
    shifts = models.CharField(max_length=255,choices=STATUS,default='MOR',)
   
    def __str__(self):
        return  self.shifts 


class HoursCard(models.Model):
      
    staff = models.ForeignKey(BussinesStaff,default=True, related_name="dailyHoursCard", on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift,default=True, related_name="dailyShift", on_delete=models.CASCADE)
    day = models.DateField(default=True)
    startAt = models.TimeField(default=True )
    finishAt = models.TimeField(default=True)
   
   
    def __str__(self):
        return  f"{self.staff} hours card "


class Invoices(models.Model):
      
    bussines = models.ForeignKey(Bussines,default=True, related_name="myInvoices", on_delete=models.CASCADE)
    invoiceType = models.CharField(max_length=255, blank=False)
    # issueAt = models.DateField(default=True)
    # reciverName = models.CharField(max_length=255,blank=False)
    # reciverId = models.CharField(max_length=255,blank=False)
    # reciverEmail = models.CharField(max_length=255,blank=False)
    # invoiceDetail = models.TextField(max_length=255,blank=False)
    # invoiceAmount = models.CharField(max_length=255,blank=False)
    # invoiceTax = models.BooleanField(default=True)
    # paymentTill = models.DateField(default=True)
    
    
    def __str__(self):
        return self.invoiceType
    
class Kabla(models.Model):
    # bussines = models.ForeignKey(Bussines,default=True, related_name="KablaBusness", on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=False)
    employeeid = models.CharField(max_length=255,blank=False)
   
    def __str__(self):
        return f"{self.name}"    


class Paysleeve(models.Model):
      
    bussiness = models.ForeignKey(Bussines,default=True, related_name="Paysleevebussiness", on_delete=models.CASCADE)
    startAt = models.DateField(default=True)
    month = models.DateField(default=True)
    name = models.CharField(max_length=255,blank=False)
    visaId = models.CharField(max_length=255,blank=False)
    regularHours = models.CharField(max_length=255,blank=False)
    extraHours = models.CharField(max_length=255,blank=True)
    weekendHours = models.CharField(max_length=255,blank=True)
    transportations = models.CharField(max_length=255,blank=True)
    hoursFee = models.CharField(max_length=255,blank=False)
    tax = models.CharField(max_length=255,blank=False)
    finalAmount = models.CharField(max_length=255,blank=False)
    
    
    def __str__(self):
        return self.name


class ToDoList(models.Model):
  
    user = models.ForeignKey(User,default=True, related_name="list", on_delete=models.CASCADE)
    actions = models.CharField(max_length=255,blank=False)
    time = models.TimeField(default=True)
    isFinish = models.BooleanField(default=False)
   
    
    def __str__(self):
        return  self.actions


