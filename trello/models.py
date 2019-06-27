from django.db import models
from django.contrib.auth import get_user_model
from sort_order_field import SortOrderField

class Title(models.Model):
    title = models.CharField(max_length=50)
    listSort = SortOrderField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['listSort']


class Card(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='cards')
    cardTitle = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    cardSort = SortOrderField()

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['cardSort']

class Comments(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment
