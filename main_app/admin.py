from django.contrib import admin
from .models import User, Conversation, Message,Event
admin.site.register(User)

admin.site.register(Message)
admin.site.register(Conversation)
admin.site.register(Event)