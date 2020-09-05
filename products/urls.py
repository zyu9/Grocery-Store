from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path("view-cart", views.view_cart),
    path("order-placed", views.order_placed)
]