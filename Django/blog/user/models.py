# user/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    class Meta:
        permissions = [
            ("can_view_profiles", "Can view user profiles"),
            ("can_edit_profiles", "Can edit user profiles"),
        ]

    def __str__(self):
        return self.user.username
