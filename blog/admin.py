from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Category, Tag, Level

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Level)