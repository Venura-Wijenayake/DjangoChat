from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
LAST_ACTIVE= (
    ( "A", "Yes" ),
    ( "B", "No" ),
)


EVENT_TYPE= (
    ( "A", "MORNING MEETING"),
    ( "B", "NOOON MEETING"),
    ( "C", "EVENING MEETING"),
)


  
class Conversation(models.Model):
    chat_type = models.CharField(max_length=100)
    status = models.TextField(max_length=100,choices=LAST_ACTIVE,
    default=LAST_ACTIVE[0][0])
    description = models.TextField(max_length=2500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return ( f'{self.id}| {self.chat_type}')
    
    def get_absolute_url(self):
        return reverse('conversationdetail', kwargs={'conversation_id': self.id})
  
class Event(models.Model):
    event_type = models.CharField(max_length=100,choices=EVENT_TYPE, 
    default=EVENT_TYPE[0][0])
    date = models.DateField('Event Date')
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE
  )
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    

    
