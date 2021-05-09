from django.urls import path
from django.conf import settings
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'posapp'
urlpatterns = [
    path('',views.posapp, name='posapp'),
    path('itemList',views.itemList, name='item_list'),
    path('itemAdd',views.itemAdd, name='item_add'),
    path('<int:id>/', views.itemUpdate, name="item_update"),
    path('itemDelete/<str:pk>', views.itemDelete, name="item_delete"),
    path('confirm_order', views.confirm_order, name='confirm_order')
]