from django.db import models
from django.contrib.auth import get_user_model

class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_date', '-create_date']