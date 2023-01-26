
from rest_framework.schemas import get_schema_view
from django import urls
from django.urls import include, path
from rest_framework import routers
from Allmodels.models import Product

from Logic.views import CategoryApi, GetOrder, OrderApi, ProductApi, Products, ProductsCategory, ProfileApiView, GetProfileApi

app_name = "Logic"
router = routers.DefaultRouter()
router.register("products", Products, "products")
router.register("categories", CategoryApi, "categories")
# router.register("orders", GetOrder, "orders")


urlpatterns = [
    path("product/", ProductApi.as_view()),
    path("product/category/", ProductsCategory.as_view()),
    path("profile/", ProfileApiView.as_view()),
    path("getprofile/", GetProfileApi.as_view()),
    path("order/", OrderApi.as_view()),
    path("orders/", GetOrder.as_view()),


]

urlpatterns += router.urls
