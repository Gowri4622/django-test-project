from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('product_api_list/',views.ProductList.as_view()),
    path('product_api_detail/<int:pk>/',views.ProductDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('product_list/',views.ProductListAPI.as_view()),

]
