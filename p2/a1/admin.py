from django.contrib import admin
from .models import Category,Product,Cart,CartVariable,UserProfile,Order,OrderUpdates,Review,Checkout,CancelOrder,ReturnOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartVariable)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderUpdates)
admin.site.register(Review)
admin.site.register(Checkout)
admin.site.register(CancelOrder)
admin.site.register(ReturnOrder)

