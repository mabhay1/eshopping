from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,RedirectView,UpdateView,DeleteView
from .forms import SignUpForm,UpdateForm,ReviewForm
from django.urls import reverse_lazy,reverse
from .models import Category,Product,Cart,CartVariable,Order,UserProfile,Review,Checkout,CancelOrder,ReturnOrder
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
# Create your views here.



class IndexView(ListView):
    model=Category
    template_name='a1/index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context
    


class SignUpView(SuccessMessageMixin,CreateView):
    form_class=SignUpForm
    template_name='a1/signup.html'
    success_url=reverse_lazy('login')
    success_message = "you are registered"

class ViewProfile(DetailView):
    model=UserProfile
    template_name="a1/view_profile.html" 
    context_object_name="userprofile" 

class LoginFormView(SuccessMessageMixin,LoginView):
    template_name = 'a1/login.html'
    success_message = "Successfully logged in."
    def get_success_url(self):
        return reverse('home')  


class LogoutFormView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logged out.')
        return response        
        


class UpdateProfile(SuccessMessageMixin,UpdateView):
    
    template_name="a1/update_profile.html"
    model=UserProfile 
    form_class=UpdateForm
    success_message = "your profile is updated"

    

class Products(DetailView):
    model=Category

class ProductDetail(DetailView):
    model=Product    

class CreateCart(LoginRequiredMixin,RedirectView):
    login_url='login'
    def get_redirect_url(self,*args,**kwargs):
        return reverse('home')

    def get(self,request,*args,**kwargs):
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        
        var1=CartVariable.objects.get_or_create(user_id=user_profile.user_ptr_id)[0]
        product=get_object_or_404(Product,pk=self.kwargs.get('pk'))
        
        if var1.a!=product.name:
            Cart.objects.create(user=user_profile,product=product,total_price=product.price)
            messages.success(self.request,' one quantity of product is added to cart go to cart to add more quantity ')
            var1.total_qty=var1.total_qty+1
            var1.total_price=var1.total_price+product.price
           
        var1.a=product.name
        var1.save()
        return super().get(request,*args,**kwargs)

class DisplayCart(LoginRequiredMixin,ListView):
    login_url='login'
    model=Cart
    def get_queryset(self):
        queryset=super().get_queryset()
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        return queryset.filter(user_id=user_profile.user_ptr_id)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        try:
            ch=Checkout.objects.get(user_id=user_profile.user_ptr_id)
        except Checkout.DoesNotExist:
            context['status']='create'  
        else:
            context['status']='update' 
            context['ch']=ch    
        cart4=CartVariable.objects.get_or_create(user_id=user_profile.user_ptr_id)[0]
        # context['qty']=cart4.total_qty
        context['price_total']=cart4.total_price
        return context   

class UpdateCart(LoginRequiredMixin,RedirectView):
    login_url='login'
    def get_redirect_url(self,*args,**kwargs):
        return reverse('a1:displaycart')    
    def post(self,request,*args,**kwargs):
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        var3=CartVariable.objects.get(user_id=user_profile.user_ptr_id)
        cart1=Cart.objects.get(id=self.kwargs.get('pk'))
        cart1.quantity=int(self.request.POST.get('qty'))
    
        cart1.total_price=cart1.quantity*(cart1.product.price)
    
        cart1.save()
        messages.success(self.request,'the cart is updated')
        var3.total_qty=0
        var3.total_price=0
        for qnty in Cart.objects.filter(user_id=user_profile.user_ptr_id):
            var3.total_qty=var3.total_qty+qnty.quantity
            var3.total_price=var3.total_price+qnty.total_price
        var3.save()
        return super().post(request,*args,**kwargs)  

class DeleteCartItem(LoginRequiredMixin,RedirectView):
    login_url="login"
    def get_redirect_url(self,*args,**kwargs):
        return reverse('a1:displaycart')  

    def get(self,request,*args,**kwargs):
        cart2=Cart.objects.get(id=self.kwargs.get('pk'))
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        var2=CartVariable.objects.get(user_id=user_profile.user_ptr_id)
        
        # var2.total_qty=var2.total_qty-cart2.quantity
        # var2.total_price=var2.total_price-cart2.total_price
        cart2.delete()
        messages.success(self.request,'the cart item is deleted')
        var2.a=""
        
        var2.total_qty=0
        var2.total_price=0
        for qnty in Cart.objects.filter(user_id=user_profile.user_ptr_id):
            var2.total_qty=var2.total_qty+qnty.quantity
            var2.total_price=var2.total_price+qnty.total_price
        
        
        var2.save()
        

        return super().get(request,*args,**kwargs) 

class PlaceOrder(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
            return reverse('home')
    def get(self,request,*args,**kwargs):
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        cart5=Cart.objects.filter(user_id=user_profile.user_ptr_id)
        var5=CartVariable.objects.get_or_create(user=user_profile)[0]
        for cart in cart5:
            try:
                Order.objects.create(user_id=user_profile.user_ptr_id,product=cart.product,quantity=cart.quantity,total_price=cart.total_price)
                
            except:
                
                messages.warning(self.request,'your order is not placed') 
                break 
            else:
                messages.success(self.request,f'your order of {cart.product.name} has been placed')
                cart.delete()      
            
         
        var5.delete()

        return super().get(request,*args,**kwargs)                



class YourOrder(LoginRequiredMixin,ListView):
    model=Order                 
    login_url='login'
    template_name='a1/your_order.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        lis=[]
        
        cn=CancelOrder.objects.filter(order__user_id=user_profile.user_ptr_id)
        rn=ReturnOrder.objects.filter(order__user_id=user_profile.user_ptr_id)    
        for i in cn:
            lis.append(i.order_id)
    
        return queryset.filter(user_id=user_profile.user_ptr_id).exclude(id__in=lis)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        ret_list=[]
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        rn=ReturnOrder.objects.filter(order__user_id=user_profile.user_ptr_id)
        for i in rn:
            ret_list.append(i.order_id)  
        context['ret_list']=ret_list         
        return context    

class OrderDetail(DetailView):
    model=Order
    template_name='a1/order_detail.html'        
    
class ReviewView(SuccessMessageMixin,CreateView):
    model=Review
    form_class=ReviewForm
    success_message = "thanks for your review your review is added"
    def form_valid(self,form):
        
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        

        status=False
        

        a=user_profile.order_set.filter(product_id=self.kwargs.get('pk'))
        print(a)
        for i in a:
            # print(i.orders.all().latest("updates_date"))
            try:
                if i.orders.all().latest("updates_date").delivered:
                    status=True
                    break
            except:
                pass

         
        if status:
            try:
                Review.objects.get(user_id=user_profile.user_ptr_id,product_id=self.kwargs.get('pk'))
                
            except Review.DoesNotExist :
                self.object = form.save(commit=False)
                self.object.user_id = user_profile.user_ptr_id
                self.object.product_id=self.kwargs.get('pk')
                return super().form_valid(form) 
        
            except :
                pass   
            else:
                messages.warning(self.request,'you have already given review for this product')
                print(type(self.kwargs.get('pk')))
                #
                return HttpResponseRedirect(reverse("a1:prod_detail",kwargs={'pk':self.kwargs.get('pk')}))
        else:
            messages.warning(self.request,'you have not purchased this product')
            return HttpResponseRedirect(reverse("a1:prod_detail",kwargs={'pk':self.kwargs.get('pk')}))
        
class CheckoutCreateView(CreateView):
    model=Checkout
    fields=['address','city','state','zipcode','name_on_card','credit_card_no','ex_month','ex_year','cvv']
    def form_valid(self,form):
        self.object = form.save(commit=False)
        user_profile=UserProfile.objects.get(username=self.request.user.username)
        self.object.user_id = user_profile.user_ptr_id
        return super().form_valid(form) 

    
class UpdateCheckout(UpdateView):
    model=Checkout
    fields=['address','city','state','zipcode','name_on_card','credit_card_no','ex_month','ex_year','cvv']
    

class CancelOrderView(SuccessMessageMixin,CreateView):
    model=CancelOrder
    fields=['reason']
    success_message = "your order is canceled"
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.order_id=self.kwargs.get('pk')
        return super().form_valid(form)    

class ReturnOrderView(SuccessMessageMixin,CreateView):
    model=ReturnOrder
    fields=['reason']
    success_message = "your order is returned"
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.order_id=self.kwargs.get('pk')
        return super().form_valid(form)  

         
