from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.ContactsTemplateView.as_view(), name='contact'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', cache_page(60 * 15)(views.ProductDetailView.as_view()), name='product_detail'),
    path('product_form/', views.ProductCreateView.as_view(), name='product_create'),
    path('product_form/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product_unpublished/<int:pk>', views.UnpublishProduct.as_view(), name='product_unpublish'),

    path('category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category_form/<int:pk>', views.ProductUpdateView.as_view(), name='category_update'),
    path('category_form/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
]
