from django.contrib import admin
from .models import Post, Category, Autors, Publisher

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Autors)
admin.site.register(Publisher)
