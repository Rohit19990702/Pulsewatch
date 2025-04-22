from django.db import models
class Alert(models.Model):
    message = models.TextField()
    triggered_at = models.DateTimeField(auto_now_add=True)