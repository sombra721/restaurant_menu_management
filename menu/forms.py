#!/usr/bin/env python
# encoding: utf-8

from django import forms
from django.utils.translation import gettext_lazy as _
from menu.models import Food, Restaurant


class CommentForm(forms.Form):

    """Comment Form class clear"""

    visitor = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20, required=False)
    content = forms.CharField(max_length=200, widget=forms.Textarea())

    def clean_content(self):
        """check content if len > 5
        :returns: cleaned content

        """
        content = self.cleaned_data.get('content', '')
        if len(content) < 5:
            raise forms.ValidationError('字數不足')
        return content


class CommentForm(forms.Form):
    visitor = forms.CharField(
        max_length=20,
        label="訪客名稱",
    )
    email = forms.EmailField(
        max_length=255,
        required=False,
        label="Email",
    )
    content = forms.CharField(
        max_length=200,
        widget=forms.Textarea,
        label="評論內容",
    )

    def clean_content(self):
        content = self.cleaned_data.get("content", "")

        if len(content) < 5:
            raise forms.ValidationError("評論內容至少需要五個字。")

        return content


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "phone_number",
            "address",
        ]
        labels = {
            "name": _("餐廳名稱"),
            "phone_number": _("電話"),
            "address": _("地址"),
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            "name",
            "price",
            "comment",
            "is_spicy",
        ]
        labels = {
            "name": _("餐點"),
            "price": _("價格"),
            "comment": _("附註"),
            "is_spicy": _("辣味"),
        }


    def __init__(self, *args, restaurant=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.restaurant = restaurant

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if not name:
            return name

        duplicate_foods = Food.objects.filter(
            restaurant=self.restaurant,
            name__iexact=name,
        )

        if self.instance.pk:
            duplicate_foods = duplicate_foods.exclude(pk=self.instance.pk)

        if duplicate_foods.exists():
            raise forms.ValidationError(
                _("這間餐廳已經有同名的餐點。")
            )

        return name
