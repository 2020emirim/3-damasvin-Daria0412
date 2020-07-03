from django.urls import path

from order.views import *
app_name = 'order'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),  # {% url 'bookmark:list %}
]
