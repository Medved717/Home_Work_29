from .forms import ProductForm, CategoryForm
from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views import View
from .services import CategoryProductService


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publish=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = request.user

        if product.owner != user and not user.groups.filter(name='Модератор продуктов').exists():
            return HttpResponseForbidden('Отсутствуют права на редактирование продукта.')
        return super().dispatch(request, pk)



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class UnpublishProduct(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У Вас нет доступа для снятия продукта с публикации.')
        product.publish = False
        product.save()
        return redirect('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('catalog:product_list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('catalog:product_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'catalog/category_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class CategoryProductView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        return CategoryProductService.view_category_product(category_name)
