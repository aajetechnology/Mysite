from django.db import models
from django.utils.text import slugify
# Create your models here.


class ContactForm(models.Model):
	name = models.CharField(max_length=100)
	email= models.EmailField()
	subject=models.CharField(max_length=300)
	message=models.TextField()

def __self__ (self):
	return f"{self.name} - {self.subject}"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True,
        max_length=200,
        blank=True,
        help_text="Auto-generated from title if left empty"
    )
    content = models.TextField()
    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True
    )
    link = models.URLField(
        blank=True,
        null=True,
        help_text="Optional external link"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Only generate slug if it's not already set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)