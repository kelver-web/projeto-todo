from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Task(models.Model):
    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    