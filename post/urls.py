from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_partial_update, post_list_create, post_delete, post_rud

urlpatterns = [
    path('list/', post_list),
    path('detail/<int:pk>/', post_detail),
    path('create/', post_create),
    path('update/<int:pk>/', post_update),
    path('update/partial/<int:pk>/', post_partial_update),
    path('list-create/', post_list_create),
    path('delete/<int:pk>/', post_delete),
    path('rud/<int:pk>/', post_rud),

]