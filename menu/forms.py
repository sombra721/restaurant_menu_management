#!/usr/bin/env python
# encoding: utf-8

from django import forms
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
            "name": "餐廳名稱",
            "phone_number": "電話",
            "address": "地址",
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
            "name": "餐點名稱",
            "price": "價格",
            "comment": "餐點說明",
            "is_spicy": "是否為辣味",
        }