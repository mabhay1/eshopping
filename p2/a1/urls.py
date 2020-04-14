
from django.urls import path
from a1 import views


app_name='a1'

urlpatterns = [
    
    
    path('category/<int:pk>',views.Products.as_view(),name='cat_detail'),
    path('product/<int:pk>',views.ProductDetail.as_view(),name='prod_detail'),
    path('createcart/<int:pk>',views.CreateCart.as_view(),name='createcart'),
    path('displaycart',views.DisplayCart.as_view(),name='displaycart'),
    path('updatecart/<int:pk>',views.UpdateCart.as_view(),name='updatecart'),
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


]
