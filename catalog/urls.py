# catalog/urls.py

from django.urls import path

from .views import (ContactFormView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                    ProductUnpublishView, ProductUpdateView)

app_name = "catalog"


urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactFormView.as_view(), name="contacts"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/unpublish/", ProductUnpublishView.as_view(), name="product_unpublish"),
]
