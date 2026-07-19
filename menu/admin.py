from django.contrib import admin

from menu.models import Comment, Food, Restaurant


class FoodInline(admin.TabularInline):
    model = Food
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "address",
    )
    search_fields = (
        "name",
        "address",
    )
    inlines = [
        FoodInline,
    ]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "restaurant",
        "price",
        "is_spicy",
    )
    list_filter = (
        "restaurant",
        "is_spicy",
    )
    search_fields = (
        "name",
        "restaurant__name",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "visitor",
        "restaurant",
        "date_time",
    )
    list_filter = (
        "restaurant",
        "date_time",
    )
    search_fields = (
        "visitor",
        "content",
    )
