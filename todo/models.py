from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True) 
    last_modified = models.DateTimeField(auto_now_add=True) #time
    completed = models.BooleanField(default=False) #status
    important = models.BooleanField(default=False) #important 

    def __str__(self):
        return self.title