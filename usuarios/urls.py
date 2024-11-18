from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='listar_usuarios'),
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='detalle_usuario'),
    path('crear/', views.UsuarioCreateView.as_view(), name='crear_usuario'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='eliminar_usuario'),
]