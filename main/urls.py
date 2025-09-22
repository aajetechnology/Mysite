from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact_view, name="contact"),
    path("blog_list/", views.blog_list, name="post_list"),
    path("blog/<int:pk>/", views.blog_detail, name="post_detail"), 
    path("dashboard/", views.dashboard, name="dashboard"),  
    
]
