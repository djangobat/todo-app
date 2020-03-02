from django.db import models
from django.conf import settings


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.title


class Task(models.Model):
    COMPLETED = 'C'
    DELETED = 'D'
    ICOMPLETE = 'I'
    CURRENT_STATUS = (
        (ICOMPLETE, '<i class="fas fa-question text-warning"></i>Chưa hoàn thành'),
        (COMPLETED, '<i class="fas fa-check text-success"></i>Đã hoàn thành'),
        (DELETED, '<i class="fas fa-trash text-danger"></i>Đã xóa'),
    )
    topic = models.ForeignKey(Topic, related_name='tasks', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=1, choices=CURRENT_STATUS, default=ICOMPLETE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_completed(self):
        return self.status == self.COMPLETED

    class Meta:
        ordering = ('order', '-created',)