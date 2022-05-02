from django.db import models    
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
          author = models.ForeignKey(User, on_delete = models.CASCADE)
          title = models.CharField(max_length = 50)
          description = models.TextField()
          hashtag = models.CharField(max_length = 20)
          created_at = models.DateTimeField(auto_now_add = True)
          updated_at = models.DateTimeField(auto_now = True)
    
          def _str_(self):
              return self.title + "\n" + self.description + self.hashtag

      