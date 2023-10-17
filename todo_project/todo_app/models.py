from django.db import models
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # set up current datetime
    closed_at = models.DateTimeField(null=True, blank=True, default= None)

    def save(self, *args, **kwargs):
        if self.completed and self.closed_at is None:
            self.closed_at = timezone.now()
        elif not self.completed:
            self.closed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title