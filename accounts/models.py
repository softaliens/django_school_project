from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Fields corresponding to SignUpForm
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=30, unique=True)
    # Additional fields for UserProfile can be added here
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # bio = models.TextField(blank=True)
    # date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
