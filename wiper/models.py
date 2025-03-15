from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class PDFCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PDFCategory"
        verbose_name_plural = "PDF Categories"

    def __str__(self):
        return self.name


class PDFDocument(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('PDFCategory', on_delete=models.SET_NULL, blank=True, null=True )
    file = models.FileField(upload_to='pdfs/')  # Uploads to media/pdfs/

    class Meta:
        verbose_name = "PDFDocument"
        verbose_name_plural = "PDF Documents"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='author_images/', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            new_slug = base_slug
            counter = 1
            while Author.objects.filter(slug=new_slug).exists():
                new_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = new_slug  # Assign unique slug before saving

        super().save(*args, **kwargs)  # Save only once

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Post Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = RichTextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,
                               related_name="posts")  # One-to-Many relationship
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True, related_name="posts")
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
