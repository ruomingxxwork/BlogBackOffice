from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        db_table = "Category"

    name = models.CharField(max_length=100)


class Tag(models.Model):
    class Meta:
        db_table = "Tag"

    name = models.CharField(max_length=70)


class Level(models.Model):
    class Meta:
        db_table = "Level"

    name = models.CharField(max_length=70)


class Blog(models.Model):
    class Meta:
        db_table = "Blog"

    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
