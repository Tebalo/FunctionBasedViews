from django.contrib import admin
from .models import Question, GeeksModel
# Register your models here.
"""
Make the geeks modifiable in the Admin
Tell the admin that Question and GeeksModel objects have 
admin interface, geeks/admin.py
"""
admin.site.register(Question)
admin.site.register(GeeksModel)
