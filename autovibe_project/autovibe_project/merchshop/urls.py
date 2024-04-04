from django.urls import path
from .views import MerchShopList, CartView, AddToCartView, RemoveFromCartView, CreateProductView, UpdateProductView, \
    DeleteProductView, DetailsProductView

urlpatterns = [
    path('', MerchShopList.as_view(), name='merch_shop_list'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('details_product/<int:pk>/', DetailsProductView.as_view(), name='details_product'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('delete_product/', DeleteProductView.as_view(), name='delete_product'),

    path('cart/', CartView.as_view(), name='cart'),
    path('add_item/<int:product_id>/', AddToCartView.as_view(), name='add_item'),
    path('remove_item/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_item'),
]