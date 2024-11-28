from django.db import models 
from django.contrib.auth.models import AbstractUser
from .custom_manager import UserManager
from django.utils import timezone



class User(AbstractUser):

    ROLE_CHOICES = (
        (0, 'ADMIN'),
        (1, 'CUSTOMER'),
        (2, 'SELLER'),
        (3, 'MANAGER'),
        (4, 'MARKETER'),
        (5, 'DELIVERY AGENT'),
        (6, 'WAREHOUSE OPERATOR'),
        (10, 'HR'),
    )
  
  
    username = None  # Disable username as we are using email as the identifier
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, max_length=100)
    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)  # Default role is CUSTOMER
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)  # To differentiate between customers and staff
    is_customer = models.BooleanField(default=True)  # To identify if a user is a customer
    is_active = models.BooleanField(default=True)  # For account activation status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.get_role_display()})'
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number']
    objects=UserManager()