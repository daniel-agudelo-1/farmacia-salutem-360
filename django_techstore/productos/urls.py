from django.urls import path
from .views import index, detalle_producto , buscar_productos, registro_usuario
from . import views
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('detalle/<int:id_producto>/', detalle_producto, name='detalle_producto'),
    path('buscar/', buscar_productos, name='buscar_productos'),
    
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('factura/<int:factura_id>/', views.ver_factura, name='ver_factura'),
    path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(
         template_name='productos/password_reset_done.html'
     ),
     name='password_reset_done'),

path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(
         template_name='productos/password_reset_confirm.html'
     ),
     name='password_reset_confirm'),

path('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(
         template_name='productos/password_reset_complete.html'
     ),
     name='password_reset_complete'),

]