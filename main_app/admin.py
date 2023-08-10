from django.contrib import admin
from .models import Member, Conversation, Message,Event
admin.site.register(Member)

admin.site.register(Message)
admin.site.register(Conversation)
admin.site.register(Event)