from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cliente/', views.cadastro_cliente, name="cadastro_cliente"),
    path('login_cliente/', views.login_cliente, name="login_cliente"),
    path('sucesso', views.sucesso_cad, name="sucesso")
]