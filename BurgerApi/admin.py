from django.contrib import admin
from BurgerApi.models import UserProfile, Order, CustomerDetail, Ingredient

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(CustomerDetail)
admin.site.register(Ingredient)
