from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    auther = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 250)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments = True)

    def get_absolute_url(self):
        return reverse("post_detail", kwarg = {'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blogapp.Post', related_name = 'comments', on_delete= models.CASCADE)
    auther = models.CharField(max_length = 250)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
        
    def __str__(self):
        return self.text