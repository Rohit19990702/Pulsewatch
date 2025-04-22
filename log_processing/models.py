from django.db import models
class Log(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Mood(models.Model):
    mood_type = models.CharField(max_length=20)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)