from django.db import models
# Create your models here.

class Post(models.Model):
    post_SrNo = models.AutoField
    post_title = models.CharField(max_length=150)
    post_about = models.CharField(max_length=50)
    post_content = models.TextField()
    post_pubDate = models.DateTimeField()
    post_authorName = models.CharField(max_length=50)
    def __str__(self):
        return self.post_title

class Contact(models.Model):
    Id = models.AutoField
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    timeStamp = str(models.DateTimeField(auto_now_add=True, blank=True))
    def __str__(self):
        return self.name+" - "+self.email
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    comm = models.TextField()
    def __str__(self):
        return self.name+ '-'+ self.email