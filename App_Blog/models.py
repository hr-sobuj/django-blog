from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_author")
    blog_title=models.CharField(max_length=250,verbose_name="Put Blog Title")
    slug = models.SlugField(max_length = 250,unique=True)
    blog_content=models.TextField(verbose_name="What is on your mind?")
    blog_image= models.ImageField(upload_to="blog_images", verbose_name="image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering=['-publish_date']
    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="blog_comment")
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_comment")
    comment=models.TextField(verbose_name="Write Your comment")
    comment_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering=['-comment_date']

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="liked_blog")
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="liker_user")

    def __str__(self):
        return self.user+" likes "+self.blog
    
    
    
    
    
    
    
    