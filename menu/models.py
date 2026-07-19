#!/usr/bin/env python
# encoding: utf-8

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        """
        :returns: name string
        """
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="foods",
    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True)
    is_spicy = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["restaurant", "name"],
                name="unique_food_name_per_restaurant",
            ),
        ]

    def __str__(self):
        return self.name


class Comment(models.Model):

    """ commment model """

    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("can_comment", "Can comment"),
        )
