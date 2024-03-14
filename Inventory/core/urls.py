from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    SignUpView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("add/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
