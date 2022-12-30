from django.contrib import admin
from django.urls import path
from app_crud_cvb import views as vw

urlpatterns = [
    # path('', vw.VW_index, name='URL_index'),
    path('', vw.Read.as_view(), name='URL_read'),
    path('create/', vw.Create.as_view(), name='URL_create'),
    path('update/<int:pk>/', vw.Update.as_view(), name='URL_update'),
    path('delete/<int:pk>/', vw.Delete.as_view(), name='URL_delete'),
]