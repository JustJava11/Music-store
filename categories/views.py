from categories.models import Category
from categories.forms import CategoryForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView


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
