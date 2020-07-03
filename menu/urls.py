from django.urls import path

from menu.views import *
app_name = 'menu'

urlpatterns = [
    path('', DrinkList.as_view(), name='list'),  # {% url 'bookmark:list %}
    path('add_coffee/', CoffeeCreateView.as_view(), name='add_coffee'),
    path('add_bubbletea/', BubbleteaCreateView.as_view(), name='add_bubbletea'),
    path('update/<int:pk>/', DrinkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DrinkDeleteView.as_view(), name='delete'),
]
