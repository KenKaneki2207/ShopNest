from django.contrib import admin
from .models import Product, Cart, Order, Profile, Support, Reviews

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Support)
admin.site.register(Reviews)