from django.db import models

# Todoのモデルを作っている。
class Todo(models.Model):
    author=models.CharField(max_length=20)
    title=models.CharField(max_length=50)
    content=models.TextField()
    
    def __str__(self):
        return self.title