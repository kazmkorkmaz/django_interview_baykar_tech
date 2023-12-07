from django.urls import path
from ..views.rental import rental_list, rental_add, rental_update, rental_delete

urlpatterns = [
    path('rental/list', rental_list, name='rental_list'),
    path('rental/add/', rental_add, name='rental_add'),
    path('rental/<slug:slug>/update/', rental_update, name='rental_update'),
    path('rental/<slug:slug>/delete/', rental_delete, name='rental_delete'),
]
