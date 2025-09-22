from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForModelForm, BlogPostForm 
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogPost


# Create your views here

def index(request):
    return render(request, 'main/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            send_mail(
                subject=contact.subject,
                message=f"""
                Yoo Prince, you have a message from a client!
                From: {contact.name} <{contact.email}>

                Message:
                {contact.message}
                """,
                from_email=settings.EMAIL_HOST_USER,  # ✅ fixed typo
                recipient_list=['emmanueloluwatofunmiagbaje@gmail.com'],
                fail_silently=False,
            )

            form.save()  # save in database (optional)
            return redirect('success')  # ✅ fixed indentation

    else:
        form = ContactFormModelForm()

    return render(request, 'main/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'main/success.html')

def dashboard(request):
    posts = BlogPost.objects.all().order_by("-created_at")

    if request.method == "POST":
        if 'delete_post_id' in request.POST:
            # Handle delete
            post_id = request.POST.get('delete_post_id')
            post_to_delete = get_object_or_404(BlogPost, id=post_id)
            post_to_delete.delete()
            return redirect("dashboard")

        # Handle new post creation
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            print(form.errors)  # DEBUG: print errors to console
    else:
        form = BlogPostForm()

    return render(request, "main/dashboard.html", {
        "form": form,
        "posts": posts
    })


def blog_list(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "main/blog_list.html", {"posts": posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, "main/blog_detail.html", {"post": post})

