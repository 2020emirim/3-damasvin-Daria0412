from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from menu.models import *


class DrinkList(ListView):  # bookmark_list.html
    model = Drink
    paginate_by = 3

class CoffeeCreateView(CreateView):  # bookmark_form.html
    model = Coffee
    fields = '__all__'  # <from>태그가 들어가는 곳에 넣어줌
    template_name = 'drink_create.html' 
    success_url = reverse_lazy('menu:list')

class BubbleteaCreateView(CreateView):  # bookmark_form.html
    model = Bubbletea
    fields = '__all__'  # <from>태그가 들어가는 곳에 넣어줌
    template_name = 'drink_create.html' 
    success_url = reverse_lazy('menu:list')


class DrinkUpdateView(UpdateView):
    model = Drink
    fields = '__all__' # <form>가 있을 때 쓴다
    template_name_suffix = '_update'    #bookmark_update.html
    success_url = reverse_lazy('menu:list')

class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = reverse_lazy('menu:list')