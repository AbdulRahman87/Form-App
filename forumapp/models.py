from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=255, default='')
    cat_desc = models.CharField(max_length=1000, default='')
    cat_img = models.ImageField(upload_to='cat_images/images',null=True, blank=True)

    def __str__(self):
        return self.cat_name

class Question(models.Model):
    ques_id = models.AutoField(primary_key=True)
    ques_parent = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    ques_title = models.CharField(max_length=255, default='')
    ques_desc = models.TextField(default='')
    ques_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ques_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.ques_title

class question_reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    reply_parent = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    reply_desc = models.TextField(default='')
    reply_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reply_time = models.DateTimeField(default=now)
    reply_category = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.reply_desc[:15]
    

class user_details(models.Model):
    _user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_img = models.ImageField(upload_to='user_img/images', default='IMG/user.png', null=False, blank=False)
    private_profile = models.CharField(max_length=5, default="off")

class ContactUs(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, null=False)
    name = models.CharField(max_length=250, default="Unknown")
    email = models.EmailField(max_length=125, default='')
    phone = models.IntegerField()
    query = models.TextField(default="")

    def __str__(self):
        return self.name