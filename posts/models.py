from django.db import models

class PostModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:30]
