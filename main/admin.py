from django.contrib import admin

# Register your models here.
from .models import ContactForm, BlogPost

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # fields to show in admin list
    search_fields = ('title', 'content')   # enable search
    list_filter = ('created_at',)  