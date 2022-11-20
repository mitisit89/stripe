from django.urls import path

from .views import buy_item, get_item

app_name = "api"
urlpatterns = [
    path("buy/<int:pk>", buy_item, name="buy"),
    path("item/<int:pk>", get_item, name="item"),
]
