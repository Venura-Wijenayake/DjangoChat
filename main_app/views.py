from django.shortcuts import render, redirect
from .models import Conversation,User,Event

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def chats_index(request):
   return render(request, "chats/index.html")

def chats_detail(request):
   return render(request, "chats/detail.html")

def conversations(request):
   conversations= Conversation.objects.all()
   return render(request, "conversations_index.html",{"conversations":conversations})

def conversations_detail(request, conversation_id):
   conversation = Conversation.objects.get(id=conversation_id)
   id_list = conversation.users.all().values_list('id')
   users_conversation_doesnt_have = User.objects.exclude(id__in=id_list)
   return render(request, 'conversations_detail.html',{"conversation":conversation,
   'users': users_conversation_doesnt_have})


def assoc_user(request, conversation_id, user_id):
  Conversation.objects.get(id=conversation_id).users.add(user_id)
  return redirect('detail', conversation_id=conversation_id)

def unassoc_user(request, conversation_id, user_id):
  Conversation.objects.get(id=conversation_id).users.remove(user_id)
  return redirect('detail', conversation_id=conversation_id)

