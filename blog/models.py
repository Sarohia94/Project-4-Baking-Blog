from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField


STATUS = ((0, 'Draft'), (1, 'Published'))


# From Code Institute Blog Walkthrough
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # From Sean, tutor support
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"PostComment {self.body} by {self.name}"

    def number_of_post_comments(self):
        return self.post_comments.count()


# Custom model
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from='recipe_name', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=500, blank=True)
    serves = models.IntegerField()
    prep_time = models.CharField(max_length=15)
    baking_time = models.CharField(max_length=15)
    ingredients = models.TextField(max_length=250)
    special_equipment = models.CharField(max_length=150, blank=True)
    method = models.TextField()
    bakers_tip = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()


class RecipeComment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='recipe_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"RecipeComment {self.body} by {self.name}"

    def number_of_recipe_comments(self):
        return self.recipe_comments.count()
