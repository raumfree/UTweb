from django.views.generic import ListView, DetailView
from .models import *


class Menu(ListView):
    model = Items
    template_name = "Menu/base.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ShowItem(DetailView):
    model = Items
    template_name = 'Menu/content.html'
    slug_url_kwarg = 'content_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['items']
        context['SelectedItem'] = context['object'].pk
        context['SelectedCategory'] = context['object'].cat
        return context

    def get_queryset(self):
        return Items.objects.filter(slug=self.kwargs['content_slug'])
