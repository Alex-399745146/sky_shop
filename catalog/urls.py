# catalog/urls.py

from django.urls import path

from .views import ProductListView, ProductDetailView, ContactTemplateView


app_name = "catalog"


urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="catalog_detail"),
    path("contacts/", ContactTemplateView.as_view(), name="contact"),
]
