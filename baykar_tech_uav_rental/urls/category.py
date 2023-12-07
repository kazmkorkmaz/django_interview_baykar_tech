from django.urls import path
from ..views import category

urlpatterns = [
    path('category/list', category.category_list, name='category_list'),
    path('category/add', category.category_add, name='category_add'),
    path('category/update/<slug:slug>/',
         category.category_update, name='category_update'),
    path('category/delete/<slug:slug>/',
         category.category_delete, name='category_delete')
]
