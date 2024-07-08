from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('galeria/', views.galeria, name='galeria'),
    path('tienda/', views.tienda, name='tienda'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registro/', views.register, name='registro'),  # Asegúrate de que esta línea esté presente

    path('', views.index, name='index'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuario/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),


]
