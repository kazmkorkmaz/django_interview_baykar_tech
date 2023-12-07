from django.urls import path
from ..views.uav import uav_list, uav_add, uav_update, uav_delete

urlpatterns = [
    path('uavs/list', uav_list, name='uav_list'),
    path('uavs/add/', uav_add, name='uav_add'),
    path('uavs/update/<slug:slug>/', uav_update, name='uav_update'),
    path('uavs/delete/<slug:slug>/', uav_delete, name='uav_delete'),
]
