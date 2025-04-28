from categories.models import Category
from categories.forms import CategoryForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from products.models import Product


class ListCategoryView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        title = 'Guitar Store'
        context['title'] = title
        return context


class DetailCategoryView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category = self.get_object()

        products = category.products.all()

        context['posts'] = products
        context['title'] = category.title
        return context
