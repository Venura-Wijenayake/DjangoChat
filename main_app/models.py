from django.db import models
from django.urls import reverse
# from datetime import date
from django.contrib.auth.models import User


class Conversation(models.Model):
    chat_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return ( f'{self.id}| {self.chat_type}')
    
    def get_absolute_url(self):
        return reverse('conversation_detail', kwargs={'group_id': self.id})


class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})