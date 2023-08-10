from django.contrib import admin
from .models import Conversation,Event


admin.site.register(Conversation)
admin.site.register(Event)