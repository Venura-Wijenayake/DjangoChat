from django.contrib import admin
from .models import Chat
from .models import *
 
# TAVY FORUM CODE
admin.site.register(forum)
admin.site.register(Discussion)

# Register your models here.
admin.site.register(Chat)
# admin.site.register(Feeding)
# admin.site.register(Toy)
# admin.site.register(Photo)