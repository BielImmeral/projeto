from django.db import models
from friends.models import Friend

class TextBlock(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='texts')
    content = models.TextField()
    is_locked = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=128, blank=True)
    password_hint = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Texto {self.order} - {self.friend.name}"
