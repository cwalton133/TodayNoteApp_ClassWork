from django.db import models
from django.contrib.auth.models import User

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Notebook(TimestampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notebooks")

    def __str__(self):
        return self.name

class NoteCategory(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Note(TimestampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name="notes")
    category = models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="notes")
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
