import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegisterForm



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def chats_index(request):
  # chats = Chat.objects.filter(heading=request.heading)
  # Another query
  # cats = request.user.cat_set.all()
  return render(request, 'chats/index.html')

@login_required
def viewProfile(request):
   user = request.user
   return render(request, 'user/profile.html', {'user':user})

@login_required
def chats_detail(request, chat_id):
  chat = Chat.objects.get(id=chat_id)
  # First, create a list of the toy ids that the cat DOES have
  id_list = chat.toys.all().values_list('id')
  # Query for the toys that the cat doesn't have
  # by using the exclude() method vs. the filter() method
  toys_chat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  feeding_form = FeedingForm()
  return render(request, 'chats/detail.html', {
    'chat': chat, 'feeding_form': feeding_form
  })

class ChatCreate(LoginRequiredMixin, CreateView):
  model = Chat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    # self.request.user is the logged in user
    form.instance.user = self.request.user
    # Let the CreateView's form_valid method
    # do its regular work (saving the object & redirecting)
    return super().form_valid(form)


class ChatUpdate(LoginRequiredMixin, UpdateView):
  model = Chat
  fields = ['breed', 'description', 'age']

class ChatDelete(LoginRequiredMixin, DeleteView):
  model = Chat
  success_url = '/chats'

# @login_required
# def add_feeding(request, chat_id):
#   # create a ModelForm instance using 
#   # the data that was submitted in the form
#   form = FeedingForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # We want a model instance, but
#     # we can't save to the db yet
#     # because we have not assigned the
#     # cat_id FK.
#     new_feeding = form.save(commit=False)
#     new_feeding.cat_id = cat_id
#     new_feeding.save()
#   return redirect('detail', cat_id=cat_id)

# class ToyList(LoginRequiredMixin, ListView):
#   model = Toy

# class ToyDetail(LoginRequiredMixin, DetailView):
#   model = Toy

# class ToyCreate(LoginRequiredMixin, CreateView):
#   model = Toy
#   fields = '__all__'

# class ToyUpdate(LoginRequiredMixin, UpdateView):
#   model = Toy
#   fields = ['name', 'color']

# class ToyDelete(LoginRequiredMixin, DeleteView):
#   model = Toy
#   success_url = '/toys'

# @login_required
# def assoc_toy(request, cat_id, toy_id):
#   Chat.objects.get(id=cat_id).toys.add(toy_id)
#   return redirect('detail', cat_id=cat_id)

# @login_required
# def unassoc_toy(request, cat_id, toy_id):
#   Cat.objects.get(id=cat_id).toys.remove(toy_id)
#   return redirect('detail', cat_id=cat_id)

# @login_required
# def add_photo(request, cat_id):
#   # photo-file maps to the "name" attr on the <input>
#   photo_file = request.FILES.get('photo-file', None)
#   if photo_file:
#     s3 = boto3.client('s3')
#     # Need a unique "key" (filename)
#     # It needs to keep the same file extension
#     # of the file that was uploaded (.png, .jpeg, etc.)
#     key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#     try:
#       bucket = os.environ['S3_BUCKET']
#       s3.upload_fileobj(photo_file, bucket, key)
#       url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#       Photo.objects.create(url=url, cat_id=cat_id)
#     except Exception as e:
#       print('An error occurred uploading file to S3')
#       print(e)
#   return redirect('detail', cat_id=cat_id)
class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    # print(form)
    if form.is_valid():
      # Save the user to the db
      
      user = form.save()
      print(user)
      # Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  form = RegisterForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)