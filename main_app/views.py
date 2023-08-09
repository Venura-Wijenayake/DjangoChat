from django.shortcuts import render #, redirect
from .models import Conversation,User,Event,Message

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def chats_index(request):
   return render(request, "chats/index.html")

def chats_detail(request):
   return render(request, "chats/detail.html")

def conversations(request):
   return render(request, "conversations_index.html")

# def conversations_detail(request, conversation_id):
#   builder = Builder.objects.get(id=builder_id)
#   id_list = builder.contractors.all().values_list('id')
#   contractors_builder_doesnt_have = Contractor.objects.exclude(id__in=id_list)
#   propertydetails_form = PropertyDetailsForm()
#   return render(request, 'builders/detail.html', { 
#     'builder': builder ,"propertydetails_form" : propertydetails_form,
#     'contractors': contractors_builder_doesnt_have                                             
#     })