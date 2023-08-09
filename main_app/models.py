from django.db import models
from django.urls import reverse


# Create your models here.
LAST_ACTIVE= (
    ( "A", "Yes" ),
    ( "B", "No" ),
)

CHAT_TYPE= (
    ( "A", "BUSINESS" ),
    ( "B", "PERSONAL" ),
)

EVENT_TYPE= (
    ( "A", "MORNING MEETING"),
    ( "B", "NOOON MEETING"),
    ( "C", "EVENING MEETING"),
)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    last_active = models.TextField(max_length=100,choices=LAST_ACTIVE,
    default=LAST_ACTIVE[0][0])

    def __str__(self):
        return ( f'{self.id}| {self.first_name}')
  
class Conversation(models.Model):
    chat_type = models.CharField(max_length=100,choices=CHAT_TYPE,
    default=CHAT_TYPE[0][0])
    created = models.TextField(max_length=100,choices=LAST_ACTIVE,
    default=LAST_ACTIVE[0][0])

    def __str__(self):
        return ( f'{self.id}| {self.chat_type}')

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
    
class Message(models.Model):
    content=models.CharField(max_length=100000)
    Sent_at=models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
#    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message {self.id}| {self.content}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'message_id': self.id})