from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, CartItem

class MerchShopList(views.ListView):
    model = Product
    template_name = 'merchshop/product_list.html'
    context_object_name = 'products'

class CartView(views.ListView):
    model = CartItem
    template_name = 'merchshop/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = sum(item.product.price * item.quantity for item in context['cart_items'])
        context['total_price'] = total_price
        return context

class AddToCartView(views.View):
    def get(self, request, product_id, *args, **kwargs):
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')

class RemoveFromCartView(views.View):
    def get(self, request, item_id, *args, **kwargs):
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return redirect('cart')

class CreateProductView(views.CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    template_name = 'merchshop/create_product.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merch_shop_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perms'] = self.request.user.has_perm('merchshop.add_product')
        return context

class DetailsProductView(views.DetailView):
    model = Product
    template_name = 'merchshop/details_product.html'



class UpdateProductView(views.UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']


    def get_success_url(self):
        return redirect('merch_shop_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perms'] = self.request.user.has_perm('merchshop.change_product')
        return context
class DeleteProductView(views.DeleteView):
    model = Product
    success_url = 'merch_shop_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perms'] = self.request.user.has_perm('merchshop.delete_product')
        return context


