
from django.urls import path
from a1 import views


app_name='a1'

urlpatterns = [
    
    
    path('category/<int:pk>',views.Products.as_view(),name='cat_detail'),
    path('product/<int:pk>',views.ProductDetail.as_view(),name='prod_detail'),
    
    path('createcart',views.createcart,name='createcart'),
    path('displaycart',views.DisplayCart.as_view(),name='displaycart'),
    
    path('updatecart',views.updatecart,name='updatecart'),
    path('delete/<int:pk>',views.DeleteCartItem.as_view(),name='deletecartitem'),
    
    path('placeorder',views.PlaceOrder.as_view(),name='placeorder'),
    path('yourorder',views.YourOrder.as_view(),name='yourorder'),
    path('view_profile/<int:pk>',views.ViewProfile.as_view(), name='profile'),
    path('update_profile/<int:pk>',views.UpdateProfile.as_view(), name='update_profile'),
    path('order_detail/<int:pk>',views.OrderDetail.as_view(),name='order_detail'),
    path('product/<int:pk>/review/',views.ReviewView.as_view(),name="add_review"),
    path('checkout/',views.CheckoutCreateView.as_view(),name='checkout'),
    path('update/<int:pk>',views.UpdateCheckout.as_view(),name='update_checkout'),
    path('cancelorder/<int:pk>',views.CancelOrderView.as_view(),name="cancelorder"),
    path('returnorder/<int:pk>',views.ReturnOrderView.as_view(),name="returnorder"),
    path('seller',views.SellerIndex.as_view(),name="sellerindex"),

    path('business_detail',views.BusinessCreateView.as_view(),name="business_detail"),
    path('bank_detail',views.BankDetailCreateView.as_view(),name="bank_detail"),
    path('prod_create',views.ProductCreateView.as_view(),name="prod_create"),
    path('cat_create',views.CategoryCreateView.as_view(),name="cat_create"),
    path('your_products',views.SellerProducts.as_view(),name='your_products'),
    path('bankup/<int:pk>',views.BankDetailUpdateView.as_view(),name='bankup'),
    path('businessup/<int:pk>',views.BusinessUpdateView.as_view(),name='businessup')

]
