from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('not_completed', 'Not Completed')
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_completed')

    def __str__(self):
        return self.name

