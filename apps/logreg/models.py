from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 3:
            errors["name"] = "Name must be greater than 2 characters"
        if len(postData['password']) < 5:
            errors["password"] = "Password must be greater than 4 characters"
        return errors
# Create your models here.
    
class User(models.Model):
    name = models.CharField(max_length=45)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 3:
            errors['message'] = "Message must contain more than 2 characters"
        return errors

class Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="message")
    user_who_liked = models.ManyToManyField(User, related_name="liked_message")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()