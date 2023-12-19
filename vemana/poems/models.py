# poems/models.py
from django.db import models

class Poem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    collected_from = models.CharField(max_length=100, blank=True, null=True)
    collected_by = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
