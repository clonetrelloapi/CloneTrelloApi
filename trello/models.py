from django.db import models
from django.contrib.auth import get_user_model

class Title(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='cards')
    content = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-update_date', '-create_date']

class Comments(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
