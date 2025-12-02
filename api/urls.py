from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('processar/', views.processar_view),
    path('CRUD/', views.CRUD),
    path('editar/<int:id>/', views.editar_view, name="editar"),
    path('editar/', views.editar)
]