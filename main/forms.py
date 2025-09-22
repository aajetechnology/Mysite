from django import forms
from .models import ContactForm, BlogPost





class ContactForModelForm(forms.ModelForm):
	class Meta:
		model= ContactForm
		fields = ['name', 'email', 'subject', 'message']



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content", "image", "link"]

