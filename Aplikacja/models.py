from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    def get_absolute_url(self):
        return reverse("Aplikacja:post_detail",
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name='comments')

    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Komentarz dodany przez: {self.name} dla posta {self.post}'


# python manage.py runserver