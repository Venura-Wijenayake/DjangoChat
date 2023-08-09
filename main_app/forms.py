from django.forms import ModelForm
from .models import Conversation

class Conversation(ModelForm):
  class Meta:
    model = Conversation
    fields = ['business', 'personal']