from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name
    
    

class Post(models.Model):
    
    AUTHOR_CHOICES = [
        ('admin', 'Admin'),
        ('paloma gatabaki', 'Paloma Gatabaki'),
    ]
    
    CATEGORY_CHOICES= [
        ('press release', 'Press Release'),
        ('opinion', 'Opinion'),
        ('notice', 'Notice'),
    ]
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = RichTextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICES, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Press Release')
    custom_author = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Updates on every save

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


