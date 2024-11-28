from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class ConnectionStatus(models.TextChoices):
    NOTCONNECTED = "notcon", "Not connected"
    PENDING = "pen", "Pending"
    CONNECTED = "con", "Connected"

class User_profile(models.Model):
    user = models.ForeignKeyField(User, ondelete = models.CASCADE)
    #profile = cloudinary.imageField()
    headline = models.TextField(null=True, blank = True)
    bio = models.TextField(null=True, blank=True)

    def get_profile_link(self):
        pass

class Connection(models.Model):
    status = models.CharField(
        max_length=10,
        choices=ConnectionStatus.choices,
        default=ConnectionStatus.NOTCONNECTED
        )
    fromUser = models.ForeignKey(User_profile, ondelete = models.CASCADE)
    toUser = models.ForeignKey(User_profile, ondelete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    content = models.TextField(null = True, blank=True)
    #media
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User_profile, on_delete=models.CASCADE)

class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #image
    #video

class comments(models.Model):
    content = models.TextField(null = True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User_profile, on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User_profile, on_delete=models.CASCADE)

class Job(models.Model):
    company_name = models.CharField(max_length=30)


class Experience(models.Model):
    pass

class Education(models.Model):
    pass

class Skill(models.Model):
    name = models.CharField(max_length=40)

class User_skill(models.Model):
    pass

class Message(models.Model):
    pass
