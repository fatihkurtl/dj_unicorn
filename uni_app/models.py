from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    context_object_name = 'todo_items'
    
    def __str__(self):
        return self.title
