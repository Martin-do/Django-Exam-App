
from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField

User = get_user_model()
# Create your models here.
class English19(models.Model):
    question = models.TextField(blank=True)
    question_img = models.ImageField(blank=True)
    
    option1 = models.TextField(blank=True)
    option1_img = models.ImageField(blank=True)
    
    option2 = models.TextField(blank=True)
    option2_img = models.ImageField(blank=True)
    
    option3 = models.TextField(blank=True)
    option3_img = models.ImageField(blank=True)
    
    option4 = models.TextField(blank=True)
    option4_img = models.ImageField(blank=True)
    
    right_answer = models.TextField(default="", blank=True)
    right_answer_img = models.ImageField(default="", blank=True)
    
    has_img = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.user()
    
class Candidate(models.Model):
    user = models.CharField(max_length=20)
    email = models.EmailField()
    # user_answer = models.TextField()
    score = models.IntegerField(default=0)
    # test = ForeignKey(English19, on_delete=models.CASCADE, default="1", null=True)
    
class Answers(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question_number = models.IntegerField()
    answer = models.TextField()
    
    