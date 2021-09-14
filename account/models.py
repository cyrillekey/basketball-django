from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import requests
from decouple import config
# Create your models here.
def TestNumber(number):
    if number[0] != '0':
        raise ValidationError("Invalid phone number")
    else:    
        number='254'+number[1:]
        r=requests.get('http://apilayer.net/api/validate?access_key='+config('ACCESS_KEY')+'&number='+number+'')
        data=r.json()
        if((data['valid'])):
            return True
        else:
            raise ValidationError("Invalid phone number")
    

class MyaccountManager(BaseUserManager):
    def create_user(self,email,username,phone_number,password=None):
        #check if all needed credentials are provided that are needed to register a user
        if not email:
            #return error if email is not provided
            raise ValueError("Users must have an email")
        if not username:
            #return error is username is not provided
            raise ValueError("Users must have a username")
            #crete a user
        if not phone_number:
            raise ValueError("Users must have a phone number") 
            
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number
        )    
        #set the user password
        user.set_password(password)
        user.save(using=self._db)
        return user
     #same method as before but create a user with super priviledges
    def create_superuser(self,email,username,phone_number,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phone_number=phone_number
        ) 
        user.is_admin=True
        user.is_staff=True
        user.is_supperuser=True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name="email",max_length=60,unique=True)
    username=models.CharField(verbose_name="username", max_length=30,unique=True)
    phone_number=models.CharField(verbose_name="phone_number",max_length=10,unique=False,validators=[TestNumber])
    date_joined=models.DateTimeField(verbose_name="date-joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last-login",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_password=models.CharField(max_length=50)
    user_passwordRepeat=models.CharField(max_length=50)

    #field that will be used when user wants to sign in
    USERNAME_FIELD= "email"
    #field that is required when user signs up
    REQUIRED_FIELDS=["username","phone_number"]
    #create a user
    objects=MyaccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True 