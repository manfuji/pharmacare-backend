from django.contrib import admin

from Allmodels.models import Categories, Order, Product, Profile

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("productName", "status")
    list_display_links = ("productName",)


@admin.register(Categories)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("catName",)
    list_display_links = ("catName",)




@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("profileUser", "country")
    list_display_links = ("profileUser",)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("quantity", "owner")
    list_display_links = ("owner",)
