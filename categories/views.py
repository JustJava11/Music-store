from categories.models import Category
from categories.forms import CategoryForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from products.models import Product

class CreateCategoryView(CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        title = 'Create Category'
        context['title'] = title
        return context


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

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'categories/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        title = 'Guitar Store'
        context['title'] = title
        return context

class DeleteCategoryView(DetailView):
    model = Category
    template_name = 'categories/category_delete.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        title = 'Guitar Store'
        context['title'] = title
        return context
