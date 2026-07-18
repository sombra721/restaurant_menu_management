from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from menu.forms import CommentForm, FoodForm, RestaurantForm
from menu.models import Comment, Food, Restaurant
from menu.permissions import user_can_comment


class MenuView(DetailView):

    """show restaurant menu"""

    model = Restaurant
    template_name = 'menu.html'
    context_object_name = 'restaurant'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch

        :request: request
        :returns: return origin dispatch
        """
        return super(MenuView, self).dispatch(request, *args, **kwargs)


class RestaurantsView(ListView):

    """return restaurant list"""

    model = Restaurant
    template_name = 'restaurants_list.html'
    context_object_name = 'restaurants'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch

        :request: request
        :returns: return origin dispatch
        """
        return super(RestaurantsView, self).dispatch(request, *args, **kwargs)


@staff_member_required
def restaurant_create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)

        if form.is_valid():
            restaurant = form.save()
            return redirect("restaurant_detail", pk=restaurant.pk)
    else:
        form = RestaurantForm()

    return render(
        request,
        "restaurant_form.html",
        {
            "form": form,
            "page_title": "新增餐廳",
        },
    )


@staff_member_required
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == "POST":
        form = RestaurantForm(
            request.POST,
            instance=restaurant,
        )

        if form.is_valid():
            restaurant = form.save()
            return redirect("restaurant_detail", pk=restaurant.pk)
    else:
        form = RestaurantForm(instance=restaurant)

    return render(
        request,
        "restaurant_form.html",
        {
            "form": form,
            "restaurant": restaurant,
            "page_title": "修改餐廳",
        },
    )


@staff_member_required
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == "POST":
        restaurant.delete()
        return redirect("restaurant_list")

    return render(
        request,
        "confirm_delete.html",
        {
            "object": restaurant,
            "object_type": "餐廳",
            "cancel_url_name": "restaurant_detail",
        },
    )


class CommentView(FormView, SingleObjectMixin):

    """View associated with form"""

    form_class = CommentForm
    template_name = 'comments.html'
    success_url = '/comment/'
    initial = {'content': u'我沒意見'}
    model = Restaurant
    context_object_name = 'r'

    def form_valid(self, form):
        """form is validated, so use form data to create comment

        :form: validated form
        :returns: origin form_valid

        """
        Comment.objects.create(
            visitor=form.cleaned_data['visitor'],
            email=form.cleaned_data['email'],
            content=form.cleaned_data['content'],
            date_time=timezone.localtime(timezone.now()),
            restaurant=self.get_object()
        )
        return self.render_to_response(self.get_context_data(
                form=self.form_class(initial=self.initial))
        )

    def get_context_data(self, **kwargs):
        """ assign attribute "object" that indicates the query object

        :returns: origin context get from get_context_data with additional object parameter

        """
        self.object = self.get_object()
        return super(CommentView, self).get_context_data(object=self.object, **kwargs)

    @method_decorator(user_passes_test(user_can_comment, login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        """ return decorated dispatch

        :request: request
        :returns: return origin dispatch
        """
        return super(CommentView, self).dispatch(request, *args, **kwargs)


def welcome(request):
    """Display a welcome page, optionally using user_name from query string."""

    user_name = request.GET.get("user_name", "")

    if user_name:
        return HttpResponse(f"Welcome!~{user_name}")

    return render(request, "welcome.html")


def register(request):
    """Register a new user."""

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "register.html",
        {
            "form": form,
        },
    )


@staff_member_required
def food_create(request, restaurant_pk):
    restaurant = get_object_or_404(
        Restaurant,
        pk=restaurant_pk,
    )

    if request.method == "POST":
        form = FoodForm(request.POST)

        if form.is_valid():
            # food needs to belong to a restaurant
            food = form.save(commit=False)
            food.restaurant = restaurant
            food.save()

            return redirect(
                "restaurant_detail",
                pk=restaurant.pk,
            )
    else:
        form = FoodForm()

    return render(
        request,
        "food_form.html",
        {
            "form": form,
            "restaurant": restaurant,
            "page_title": "新增餐點",
        },
    )


@staff_member_required
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        form = FoodForm(
            request.POST,
            instance=food,
        )

        if form.is_valid():
            food = form.save()

            return redirect(
                "restaurant_detail",
                pk=food.restaurant.pk,
            )
    else:
        form = FoodForm(instance=food)

    return render(
        request,
        "food_form.html",
        {
            "form": form,
            "food": food,
            "restaurant": food.restaurant,
            "page_title": "修改餐點",
        },
    )


@staff_member_required
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    restaurant_pk = food.restaurant.pk

    if request.method == "POST":
        food.delete()

        return redirect(
            "restaurant_detail",
            pk=restaurant_pk,
        )

    return render(
        request,
        "confirm_delete.html",
        {
            "object": food,
            "object_type": "餐點",
            "restaurant": food.restaurant,
            "cancel_url_name": "restaurant_detail",
        },
    )


class IndexView(TemplateView):
    template_name = "index.html"