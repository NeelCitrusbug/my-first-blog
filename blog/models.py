from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    """
    it's post model which has author, title, text, created_date, published_date fields
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=255, default="categorynotselected")

    def publish(self):
        """we can publish the post using this method"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """returns the object name as title of the post"""
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_list")
