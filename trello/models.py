from django.db import models
from django.contrib.auth import get_user_model
from sort_order_field import SortOrderField


# trello list
class Title(models.Model):
    title = models.CharField(max_length=50)
    listSort = SortOrderField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['listSort']


# trello card
class Card(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='cards')
    cardTitle = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    cardSort = SortOrderField()

    def __str__(self):
        return self.cardTitle

    class Meta:
        ordering = ['cardSort']


# trello card - comment
class Comments(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment


# trello backgroundcolor
class Backgroundcolor(models.Model):
    background_color = models.TextField(null=True)

    def __str__(self):
        return self.background_color
