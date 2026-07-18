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
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        """
        :returns: name string
        """
        return self.name

    class Meta:

        """Meta: attribute, options"""

        ordering = ['price']


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
